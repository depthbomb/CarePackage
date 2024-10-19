using System.Security.Principal;

namespace CarePackage.Utils;

public static class Identity
{
    public static bool IsAdministrator => new WindowsPrincipal(WindowsIdentity.GetCurrent()).IsInRole(WindowsBuiltInRole.Administrator);
}
