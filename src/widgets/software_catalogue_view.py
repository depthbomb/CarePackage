from typing import cast, Optional
from src.enums import SettingsKeys
from src.lib.theme import ThemeUtil
from src.lib.settings import Settings
from src.lib.software_spec import SoftwareSpec
from PySide6.QtWidgets import QMenu, QListView, QApplication, QStyledItemDelegate, QStyleOptionViewItem
from PySide6.QtGui import QFont, QIcon, QPixmap, QPainter, QKeyEvent, QMouseEvent, QFontMetrics, QDesktopServices
from PySide6.QtCore import (
    Qt,
    QUrl,
    QSize,
    QRect,
    Signal,
    QRectF,
    QModelIndex,
    QAbstractListModel,
    QPersistentModelIndex,
    QSortFilterProxyModel,
)

class SoftwareCatalogueModel(QAbstractListModel):
    SoftwareRole = int(Qt.ItemDataRole.UserRole) + 1
    SelectedRole = SoftwareRole + 1

    def __init__(self, software: tuple[SoftwareSpec, ...], parent=None):
        super().__init__(parent)
        self._software = software
        self._selected: set[tuple[str, str]] = set()

    def rowCount(self, parent=QModelIndex()) -> int:
        return 0 if parent.isValid() else len(self._software)

    def data(self, index: QModelIndex, role=Qt.ItemDataRole.DisplayRole):
        if not index.isValid() or not 0 <= index.row() < len(self._software):
            return None

        software = self._software[index.row()]
        if role == Qt.ItemDataRole.DisplayRole:
            return software.name
        if role == Qt.ItemDataRole.ToolTipRole:
            details = [category.value for category in software.category]
            if software.is_deprecated:
                details.append('Deprecated')
            if software.is_archive:
                details.append('Compressed archive')
            if software.is_unreliable:
                details.append('May not download reliably')
            return f'{software.name}\n{", ".join(details)}'
        if role == self.SoftwareRole:
            return software
        if role == self.SelectedRole:
            return self._identity(software) in self._selected

        return None

    def flags(self, index: QModelIndex):
        if not index.isValid():
            return Qt.ItemFlag.NoItemFlags
        return Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsSelectable

    def set_selected(self, software: set[SoftwareSpec]):
        selected = {self._identity(item) for item in software}
        if selected == self._selected:
            return

        self._selected = selected
        if self._software:
            self.dataChanged.emit(
                self.index(0, 0),
                self.index(len(self._software) - 1, 0),
                [self.SelectedRole],
            )

    @staticmethod
    def _identity(software: SoftwareSpec) -> tuple[str, str]:
        return software.module, software.class_name


class SoftwareCatalogueFilterModel(QSortFilterProxyModel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._category = ''
        self._search_text = ''

    def set_filters(self, category: str, search_text: str):
        category = category or ''
        search_text = search_text.strip().casefold()
        if category == self._category and search_text == self._search_text:
            return

        self._category = category
        self._search_text = search_text
        self.invalidateFilter()

    def visible_software(self) -> list[SoftwareSpec]:
        return [
            cast(SoftwareSpec, self.index(row, 0).data(SoftwareCatalogueModel.SoftwareRole))
            for row in range(self.rowCount())
        ]

    def filterAcceptsRow(self, source_row: int, source_parent: QModelIndex) -> bool:
        source = self.sourceModel()
        if source is None:
            return False

        index = source.index(source_row, 0, source_parent)
        software = cast(SoftwareSpec, index.data(SoftwareCatalogueModel.SoftwareRole))
        matches_category = not self._category or any(category.name == self._category for category in software.category)
        matches_search = self._search_text in software.name.casefold()
        return matches_category and matches_search


class SoftwareCatalogueDelegate(QStyledItemDelegate):
    RowHeight = 64

    def __init__(self, parent=None):
        super().__init__(parent)
        self._pixmaps: dict[tuple[str, int], QPixmap] = {}

    def sizeHint(self, option: QStyleOptionViewItem, index: QModelIndex) -> QSize:
        return QSize(option.rect.width(), self.RowHeight)

    def paint(self, painter: QPainter, option: QStyleOptionViewItem, index: QModelIndex):
        software = cast(SoftwareSpec, index.data(SoftwareCatalogueModel.SoftwareRole))
        selected = bool(index.data(SoftwareCatalogueModel.SelectedRole))
        rect = option.rect

        painter.save()
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        if selected:
            shade = 150 if ThemeUtil.style_supports_dark_mode() else 175
            painter.fillRect(rect, ThemeUtil.get_accent_color_shade(ThemeUtil.Mode.Lighter, shade))
        elif self._is_hovered(index):
            painter.fillRect(rect, QApplication.palette().window())

        icon_rect = QRect(rect.left() + 12, rect.center().y() - 16, 32, 32)
        painter.drawPixmap(icon_rect, self._pixmap(f':images/software/{software.icon}', 32))

        content_right = rect.right() - 12
        if not selected and Settings().get(SettingsKeys.ShowCategoryBadges, True, bool):
            content_right = self._paint_category_badges(painter, software, rect, content_right)

        status_icons = []
        if software.is_deprecated:
            status_icons.append(':icons/warning.ico')
        if software.is_archive:
            status_icons.append(':icons/zip.ico')
        if software.is_unreliable:
            status_icons.append(':icons/error.ico')

        name_font = QFont(option.font)
        name_font.setPointSize(13)
        name_font.setBold(selected)
        painter.setFont(name_font)
        painter.setPen(
            ThemeUtil.get_accent_color_shade(ThemeUtil.Mode.Darker, 500)
            if selected else option.palette.text().color()
        )

        name_x = icon_rect.right() + 12
        status_width = len(status_icons) * 24
        available_name_width = max(0, content_right - name_x - status_width)
        metrics = QFontMetrics(name_font)
        display_name = metrics.elidedText(software.name, Qt.TextElideMode.ElideRight, available_name_width)
        name_rect = QRect(name_x, rect.top(), available_name_width, rect.height())
        painter.drawText(name_rect, Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter, display_name)

        status_x = name_x + metrics.horizontalAdvance(display_name) + 8
        for path in status_icons:
            status_rect = QRect(status_x, rect.center().y() - 8, 16, 16)
            painter.drawPixmap(status_rect, self._pixmap(path, 16))
            status_x += 24

        painter.restore()

    def _is_hovered(self, index: QModelIndex) -> bool:
        view = self.parent()
        return bool(view and getattr(view, 'hovered_index', QPersistentModelIndex()) == index)

    def _paint_category_badges(self, painter: QPainter, software: SoftwareSpec, rect: QRect, right: int) -> int:
        badge_font = QFont(painter.font())
        badge_font.setBold(True)
        badge_font.setPixelSize(10)
        metrics = QFontMetrics(badge_font)
        painter.setFont(badge_font)

        for category in reversed(software.category):
            width = max(48, metrics.horizontalAdvance(category.value) + 16)
            badge_rect = QRectF(right - width + 1, rect.center().y() - 15, width, 30)
            painter.setPen(Qt.PenStyle.NoPen)
            painter.setBrush(ThemeUtil.get_accent_color_name())
            painter.drawRoundedRect(badge_rect, 15, 15)
            painter.setPen(ThemeUtil.get_foreground_color())
            painter.drawText(badge_rect, Qt.AlignmentFlag.AlignCenter, category.value)
            right -= width + 3

        return right - 9

    def _pixmap(self, path: str, size: int) -> QPixmap:
        key = path, size
        if key not in self._pixmaps:
            source = QPixmap(path)
            self._pixmaps[key] = source.scaled(
                size,
                size,
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation,
            )
        return self._pixmaps[key]


class SoftwareCatalogueView(QListView):
    software_activated = Signal(object)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setItemDelegate(SoftwareCatalogueDelegate(self))
        self.setSelectionMode(QListView.SelectionMode.NoSelection)
        self.setUniformItemSizes(True)
        self.setVerticalScrollMode(QListView.ScrollMode.ScrollPerPixel)
        self.setMouseTracking(True)
        self.viewport().setCursor(Qt.CursorShape.PointingHandCursor)
        self._hovered_index = QPersistentModelIndex()

        self._context_software = cast(Optional[SoftwareSpec], None)
        self._context_menu = QMenu(self)
        self._homepage_action = self._context_menu.addAction(QIcon(':images/open.png'), 'Homepage')
        self._homepage_action.triggered.connect(self._open_context_homepage)

    def mousePressEvent(self, event: QMouseEvent):
        index = self.indexAt(event.position().toPoint())
        if not index.isValid():
            super().mousePressEvent(event)
            return

        self.setCurrentIndex(index)
        software = cast(SoftwareSpec, index.data(SoftwareCatalogueModel.SoftwareRole))
        if event.button() == Qt.MouseButton.LeftButton:
            self.software_activated.emit(software)
        elif event.button() == Qt.MouseButton.RightButton:
            self._context_software = software
            self._context_menu.exec(event.globalPosition().toPoint())
        else:
            super().mousePressEvent(event)

    def mouseMoveEvent(self, event: QMouseEvent):
        self._set_hovered_index(self.indexAt(event.position().toPoint()))
        super().mouseMoveEvent(event)

    def leaveEvent(self, event):
        self._set_hovered_index(QModelIndex())
        super().leaveEvent(event)

    def keyPressEvent(self, event: QKeyEvent):
        if event.key() in (Qt.Key.Key_Enter, Qt.Key.Key_Return, Qt.Key.Key_Space):
            index = self.currentIndex()
            if index.isValid():
                self.software_activated.emit(index.data(SoftwareCatalogueModel.SoftwareRole))
                event.accept()
                return
        super().keyPressEvent(event)

    def refresh_badges(self):
        self.viewport().update()

    @property
    def hovered_index(self) -> QPersistentModelIndex:
        return self._hovered_index

    def _set_hovered_index(self, index: QModelIndex):
        hovered_index = QPersistentModelIndex(index)
        if hovered_index != self._hovered_index:
            self._hovered_index = hovered_index
            self.viewport().update()

    def _open_context_homepage(self):
        if self._context_software is not None:
            QDesktopServices.openUrl(QUrl(self._context_software.homepage))
