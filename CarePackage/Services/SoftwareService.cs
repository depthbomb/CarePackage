using System.Reflection;
using CarePackage.Controls;

namespace CarePackage.Services;

public class SoftwareService
{
    private readonly IServiceProvider   _serviceProvider;
    private readonly List<BaseSoftware> _definitions;

    public SoftwareService(IServiceProvider serviceProvider)
    {
        _serviceProvider = serviceProvider;
        _definitions     = [];
    }

    public IReadOnlyList<BaseSoftware> GetDefinitions(bool force = false)
    {
        LoadDefinitions(force);

        return _definitions.OrderByDescending(d => d.Name).ToList().AsReadOnly();
    }

    public IReadOnlyList<SoftwareCategory> GetCategories() => Enum.GetValues<SoftwareCategory>().AsReadOnly();

    private void LoadDefinitions(bool force = false)
    {
        if (_definitions.Count != 0 && !force) return;
        if (force) _definitions.Clear();
        
        var ass   = Assembly.GetExecutingAssembly();
        var types = ass.GetTypes().Where(t => t.IsSubclassOf(typeof(BaseSoftware)) && !t.IsAbstract);
        foreach (var type in types)
        {
            BaseSoftware instance;
            var          constructors = type.GetConstructors();
            if (constructors.Any(c => c.GetParameters().Length > 0))
            {
                // Some software classes require DI and thus have a constructor that takes a single argument of
                // IServiceProvider. So we check if the current iteration class has any constructors and instantiate it
                // with the IServiceProvider instance.

                instance = (BaseSoftware)Activator.CreateInstance(type, _serviceProvider)!;
            }
            else
            {
                instance = (BaseSoftware)Activator.CreateInstance(type)!;
            }
            
            _definitions.Add(instance);
        }
    }

    public SoftwareListItem CreateListItemControl(BaseSoftware software)
        => ActivatorUtilities.CreateInstance<SoftwareListItem>(_serviceProvider, software);
}
