* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/AssetBundles-Dependencies.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [Assets and media](https://docs.unity3d.com/6000.0/Documentation/Manual/assets-and-media.html)
  * [Combining assets into bundles](https://docs.unity3d.com/6000.0/Documentation/Manual/assetbundles-section.html)
  * Handling dependencies between AssetBundles


[](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetBundles-Native.html)
Loading assets from AssetBundles
[](https://docs.unity3d.com/6000.0/Documentation/Manual/assetbundles-optimizing.html)
Optimizing AssetBundles
# Handling dependencies between AssetBundles
AssetBundles become dependent on others when their objects reference objects in another bundle. If a referenced object is not assigned to any AssetBundle, Unity duplicates and embeds it in the dependent bundles during the build. If multiple bundles reference the same unassigned object, each bundle contains its own copy, increasing memory usage. 
To load dependent AssetBundles, ensure dependencies are loaded into memory before accessing their dependent bundles. For example, if **Bundle 1** contains a material that reference a texture in **Bundle 2** , load **Bundle 2** into memory before accessing the material from **Bundle 1**. Unity does not automatically resolve dependencies. To manage dependencies at runtime, you can use the `AssetBundleManifest`. For more information, refer to [Loading assets from AssetBundles](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetBundles-Native.html).
## Avoiding duplicated information across AssetBundles
By default, Unity does not optimize duplicate data across AssetBundles. For example, if two AssetBundles each containing a **Prefab** An asset type that allows you to store a GameObject complete with components and properties. The prefab acts as a template from which you can create new object instances in the scene. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Prefabs.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Prefab) referencing the same unassigned material, Unity embeds a copy of the material in both bundles. This increases install size, runtime memory usage, and affects batching, because Unity treats each copy as unique.
### Optimization tips
Assign shared assets to a common AssetBundle to avoid duplication. During the build, Unity automatically includes dependencies in the assigned AssetBundle. This significantly reduces the size of other AssetBundles. For example:
  * Extract a shared Material and its dependencies into a `modulesmaterials` AssetBundle.
  * Prefab bundles then only reference the `modulesmaterials` AssetBundle, reducing their size.


## Runtime loading
When using a common AssetBundle for shared assets, load it into memory before loading AssetBundles that depend on it. In the following example, the shared Material is loaded correctly because its AssetBundle (`materialsAB`) is loaded first:
```
using System.IO;
using UnityEngine;

public class InstantiateAssetBundles : MonoBehaviour
{
    void Start()
    {
        var materialsAB = AssetBundle.LoadFromFile(Path.Combine(Application.dataPath, Path.Combine("AssetBundles", "modulesmaterials")));
        var moduleAB = AssetBundle.LoadFromFile(Path.Combine(Application.dataPath, Path.Combine("AssetBundles", "example-prefab")));

        if (materialsAB == null || moduleAB == null)
        {
            Debug.Log("Failed to load AssetBundle!");
            return;
        }
        var prefab = moduleAB.LoadAsset<GameObject>("example-prefab");
        Instantiate(prefab);
    }
}


```

## Assetbundle unloading
Properly manage dependencies when unloading AssetBundles to prevent crashes or undefined behavior. Dependent AssetBundles must not remain loaded after their dependencies are unloaded. Reloading dependencies separately can also cause issues.
### Example unload strategy: reference counting
Implement a reference-counting system to track and safely unload AssetBundles only when they are no longer in use.
The following example tracks dependencies and safely unloads unused AssetBundles:
```
using System.Collections.Generic;
using System.IO;
using UnityEngine;

public class AssetBundleManager
{
    private string assetBundlesDirectory;
    private AssetBundleManifest assetBundleManifest;
    private Dictionary<string, int> assetBundleReferenceCounts = new Dictionary<string, int>();
    private Dictionary<string, AssetBundle> loadedAssetBundles = new Dictionary<string, AssetBundle>();

    public void Initialize(string manifestBundlePath, string assetBundlesDirectory)
    {
        this.assetBundlesDirectory = assetBundlesDirectory;
        AssetBundle manifestBundle = AssetBundle.LoadFromFile(manifestBundlePath);
        assetBundleManifest = manifestBundle.LoadAsset<AssetBundleManifest>("AssetBundleManifest");
        manifestBundle.Unload(false);
    }

    public AssetBundle LoadBundle(string bundlePath)
    {
        AssetBundle bundle = LoadAssetBundleIfNotLoaded(bundlePath);
        IncrementReferenceCount(bundle.name);

        string[] dependencyBundleNames = assetBundleManifest.GetAllDependencies(bundle.name);
        foreach (string dependency in dependencyBundleNames)
        {
            string dependencyBundlePath = getAssetBundlePathFromName(dependency);
            LoadAssetBundleIfNotLoaded(dependencyBundlePath);
            IncrementReferenceCount(dependency);
        }

        return bundle;
    }

    private AssetBundle LoadAssetBundleIfNotLoaded(string bundlePath)
    {
        if (!loadedAssetBundles.TryGetValue(bundlePath, out AssetBundle bundle))
        {
            // For simplicity, this example only shows the case of synchronous loading, but support for
            // LoadFromFileAsync() and the other load methods could also be added with similar code.
            bundle = AssetBundle.LoadFromFile(bundlePath);
            
            if (bundle == null)
            {
                throw new System.Exception($"Failed to load AssetBundle at path {bundlePath}");
            }
            loadedAssetBundles.Add(bundlePath, bundle);
        }

        return bundle;
    }


    public void UnloadBundle(AssetBundle bundle)
    {
        string[] dependencyBundleNames = assetBundleManifest.GetAllDependencies(bundle.name);

        DecrementRefCount(bundle.name);
        foreach (string dependency in dependencyBundleNames)
        {
            DecrementRefCount(dependency);
        }

        List<string> bundlesToUnload = new List<string>();
        foreach (KeyValuePair<string, AssetBundle> loadedBundleEntry in loadedAssetBundles)
        {
            if (assetBundleReferenceCounts[loadedBundleEntry.Value.name] <= 0)
            {
                bundlesToUnload.Add(loadedBundleEntry.Key);
            }
        }

        foreach (string bundlePath in bundlesToUnload)
        {
            loadedAssetBundles[bundlePath].Unload(true);
            loadedAssetBundles.Remove(bundlePath);
        }
    }

    private string getAssetBundlePathFromName(string name)
    {
        return Path.Combine(assetBundlesDirectory, name);
    }

    private void IncrementReferenceCount(string bundleName)
    {
        if (assetBundleReferenceCounts.ContainsKey(bundleName))
        {
            assetBundleReferenceCounts[bundleName]++;
        }
        else
        {
            assetBundleReferenceCounts[bundleName] = 1;
        }
    }

    private void DecrementRefCount(string bundleName)
    {
        if (assetBundleReferenceCounts.ContainsKey(bundleName))
        {
            assetBundleReferenceCounts[bundleName]--;
        }
        else {
            string errorMessage = $"Attempted to decrement reference count for non-existent bundle: {bundleName}";
            throw new KeyNotFoundException(errorMessage);
        }
    }
}

```

**Note:** When using [LZ4 compressed and uncompressed](https://docs.unity3d.com/6000.0/Documentation/Manual/assetbundles-compression-format.html) AssetBundles, [`AssetBundle.LoadFromFile`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundle.LoadFromFile.html) only loads the catalog of its content in memory, but not the content itself. To check if this is happening, use the [Memory Profiler](https://docs.unity3d.com/Packages/com.unity.memoryprofiler@latest) package to inspect memory usage.
## Additional resources
  * [`AssetBundleManifest`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundleManifest.html)
  * [Loading assets from AssetBundles](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetBundles-Native.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetBundles-Native.html)
Loading assets from AssetBundles
[](https://docs.unity3d.com/6000.0/Documentation/Manual/assetbundles-optimizing.html)
Optimizing AssetBundles
