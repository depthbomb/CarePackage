﻿//------------------------------------------------------------------------------
// <auto-generated>
//     This code was generated by a tool.
//     Runtime Version:4.0.30319.42000
//
//     Changes to this file may cause incorrect behavior and will be lost if
//     the code is regenerated.
// </auto-generated>
//------------------------------------------------------------------------------

namespace CarePackage.Resources {
    using System;
    
    
    /// <summary>
    ///   A strongly-typed resource class, for looking up localized strings, etc.
    /// </summary>
    // This class was auto-generated by the StronglyTypedResourceBuilder
    // class via a tool like ResGen or Visual Studio.
    // To add or remove a member, edit your .ResX file then rerun ResGen
    // with the /str option, or rebuild your VS project.
    [global::System.CodeDom.Compiler.GeneratedCodeAttribute("System.Resources.Tools.StronglyTypedResourceBuilder", "17.0.0.0")]
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute()]
    [global::System.Runtime.CompilerServices.CompilerGeneratedAttribute()]
    internal class Strings {
        
        private static global::System.Resources.ResourceManager resourceMan;
        
        private static global::System.Globalization.CultureInfo resourceCulture;
        
        [global::System.Diagnostics.CodeAnalysis.SuppressMessageAttribute("Microsoft.Performance", "CA1811:AvoidUncalledPrivateCode")]
        internal Strings() {
        }
        
        /// <summary>
        ///   Returns the cached ResourceManager instance used by this class.
        /// </summary>
        [global::System.ComponentModel.EditorBrowsableAttribute(global::System.ComponentModel.EditorBrowsableState.Advanced)]
        internal static global::System.Resources.ResourceManager ResourceManager {
            get {
                if (object.ReferenceEquals(resourceMan, null)) {
                    global::System.Resources.ResourceManager temp = new global::System.Resources.ResourceManager("CarePackage.Resources.Strings", typeof(Strings).Assembly);
                    resourceMan = temp;
                }
                return resourceMan;
            }
        }
        
        /// <summary>
        ///   Overrides the current thread's CurrentUICulture property for all
        ///   resource lookups using this strongly typed resource class.
        /// </summary>
        [global::System.ComponentModel.EditorBrowsableAttribute(global::System.ComponentModel.EditorBrowsableState.Advanced)]
        internal static global::System.Globalization.CultureInfo Culture {
            get {
                return resourceCulture;
            }
            set {
                resourceCulture = value;
            }
        }
        
        /// <summary>
        ///   Looks up a localized string similar to CarePackage.
        /// </summary>
        internal static string AppTitle {
            get {
                return ResourceManager.GetString("AppTitle", resourceCulture);
            }
        }
        
        /// <summary>
        ///   Looks up a localized string similar to Clear {0} items.
        /// </summary>
        internal static string ClearSelectionButtonNonEmptyText {
            get {
                return ResourceManager.GetString("ClearSelectionButtonNonEmptyText", resourceCulture);
            }
        }
        
        /// <summary>
        ///   Looks up a localized string similar to Clear Selection.
        /// </summary>
        internal static string ClearSelectionButtonText {
            get {
                return ResourceManager.GetString("ClearSelectionButtonText", resourceCulture);
            }
        }
        
        /// <summary>
        ///   Looks up a localized string similar to Download &amp;&amp; Install Selected.
        /// </summary>
        internal static string DownloadAndInstallButtonText {
            get {
                return ResourceManager.GetString("DownloadAndInstallButtonText", resourceCulture);
            }
        }
        
        /// <summary>
        ///   Looks up a localized string similar to You are about to download some compressed archives.
        /// </summary>
        internal static string DownloadingArchiveNotificationHeading {
            get {
                return ResourceManager.GetString("DownloadingArchiveNotificationHeading", resourceCulture);
            }
        }
        
        /// <summary>
        ///   Looks up a localized string similar to One or more programs you selected will be downloaded as compressed archives that will need to be extracted afterwards.
        ///Would you like to open the folder containing these archives once the remaining programs have finished installing?.
        /// </summary>
        internal static string DownloadingArchiveNotificationText {
            get {
                return ResourceManager.GetString("DownloadingArchiveNotificationText", resourceCulture);
            }
        }
        
        /// <summary>
        ///   Looks up a localized string similar to Downloading selected software....
        /// </summary>
        internal static string DownloadStartedStatusStripText {
            get {
                return ResourceManager.GetString("DownloadStartedStatusStripText", resourceCulture);
            }
        }
        
        /// <summary>
        ///   Looks up a localized string similar to Waiting.
        /// </summary>
        internal static string Waiting {
            get {
                return ResourceManager.GetString("Waiting", resourceCulture);
            }
        }
    }
}
