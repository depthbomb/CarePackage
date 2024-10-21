namespace CarePackage;

public static class ArgParser
{
    private static readonly Dictionary<string, object> Args = new(StringComparer.OrdinalIgnoreCase);

    public static void AddArg<T>(string name, string shortName, T defaultValue)
    {
        Args[name]      = defaultValue;
        Args[shortName] = defaultValue;
    }

    public static void ParseArgs(string[] arguments)
    {
        for (int i = 0; i < arguments.Length; i++)
        {
            var arg = arguments[i].TrimStart('/', '-');
            if (Args.TryGetValue(arg, out object? value))
            {
                var valueType = value.GetType();
                if (valueType == typeof(bool))
                {
                    Args[arg] = true;
                }
                else if (valueType == typeof(List<int>) && i + 1 < arguments.Length)
                {
                    Args[arg] = arguments[++i].Split(',').Select(int.Parse).ToList();
                }
                else if (valueType == typeof(List<string>) && i + 1 < arguments.Length)
                {
                    Args[arg] = arguments[++i].Split(',').ToList();
                }
                else if (valueType == typeof(int) && i + 1 < arguments.Length)
                {
                    Args[arg] = int.Parse(arguments[++i]);
                }
                else if (valueType == typeof(string) && i + 1 < arguments.Length)
                {
                    Args[arg] = arguments[++i];
                }
            }
        }
    }

    public static T GetArg<T>(string name)
    {
        if (Args.TryGetValue(name, out object? argValue) && argValue is T value)
        {
            return value;
        }

        throw new ArgumentException($"Argument '{name}' not found or is of incorrect type.");
    }
}
