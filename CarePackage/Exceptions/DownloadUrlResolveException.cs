using System.Diagnostics.CodeAnalysis;

namespace CarePackage.Exceptions;

public class DownloadUrlResolveException : Exception
{
    public DownloadUrlResolveException() { }

    public DownloadUrlResolveException(string? message) : base(message) { }

    public DownloadUrlResolveException(string? message, Exception inner) : base(message, inner) { }

    public static void ThrowIf([DoesNotReturnIf(true)] bool predicate, string? message = null)
    {
        if (predicate)
        {
            Throw(message);
        }
    }

    public static void ThrowUnless([DoesNotReturnIf(false)] bool predicate, string? message = null)
    {
        if (!predicate)
        {
            Throw(message);
        }
    }

    [DoesNotReturn]
    private static void Throw() => throw new DownloadUrlResolveException();

    [DoesNotReturn]
    private static void Throw(string? message) => throw new DownloadUrlResolveException(message);

    [DoesNotReturn]
    private static void Throw(string? message, Exception inner) => throw new DownloadUrlResolveException(message, inner);
}
