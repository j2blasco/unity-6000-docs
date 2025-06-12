* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/AssetBundles-Native.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [Assets and media](https://docs.unity3d.com/6000.0/Documentation/Manual/assets-and-media.html)
  * [Combining assets into bundles](https://docs.unity3d.com/6000.0/Documentation/Manual/assetbundles-section.html)
  * Loading assets from AssetBundles


[](https://docs.unity3d.com/6000.0/Documentation/Manual/assetbundles-file-format.html)
AssetBundle file format reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetBundles-Dependencies.html)
Handling dependencies between AssetBundles
# Loading assets from AssetBundles
To load assets from an AssetBundle, you must first load the AssetBundle itself and then load the assets from it.
## Loading AssetBundles
You can use the following APIs to load AssetBundles:
  * The static Load methods on the [`AssetBundle`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundle.html) class, for example [`AssetBundle.LoadFromFile`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundle.LoadFromFile.html). This class has a range of loading methods depending on the AssetBundle location and whether you want to load it synchronously or asynchronously.
  * The [UnityWebRequest](https://docs.unity3d.com/6000.0/Documentation/Manual/web-request.html) support for AssetBundles, for example [`UnityWebRequestAssetBundle.GetAssetBundle`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequestAssetBundle.GetAssetBundle.html).


Refer to the API references for these classes for the full range of AssetBundle loading methods available and usage examples.
## Loading assets
Once an AssetBundle is loaded, you can use the `AssetBundle` class to load individual assets from it as follows.
Use `LoadAsset` to load a single asset, for example the root **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) of a **prefab** An asset type that allows you to store a GameObject complete with components and properties. The prefab acts as a template from which you can create new object instances in the scene. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Prefabs.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Prefab), synchronously:
```
GameObject gameObject = loadedAssetBundle.LoadAsset<GameObject>(assetName);

```

Use `LoadAllAssets` to load all assets as follows:
```
Unity.Object[] objectArray = loadedAssetBundle.LoadAllAssets();

```

This returns an array with all the root Object of each asset.
The methods in the previous snippets return either the type of object to be loaded or an array of objects. The asynchronous counterparts of these methods return an [`AssetBundleRequest`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundleRequest.html) instead. You must wait for this operation to complete before accessing the asset.
To load a single asset asynchronously:
```
AssetBundleRequest request = loadedAssetBundleObject.LoadAssetAsync<GameObject>(assetName);
yield return request; // or await request;
var loadedAsset = request.asset;

```

To load all assets asynchronously:
```
AssetBundleRequest request = loadedAssetBundle.LoadAllAssetsAsync();
yield return request; // or await request;
var loadedAssets = request.allAssets;

```

For more information and a full code example, refer to the [`AssetBundle`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundle.html) API reference.
### Loading AssetBundle manifests
You can load an AssetBundle manifest into an instance of the [`AssetBundleManifest`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundle.html) class to get information including dependency data, hash data, and variant data for built AssetBundles.
This is especially useful when managing dependencies between AssetBundles. The manifest object makes dynamically finding and loading dependencies possible, so you don’t have to hardcode all the AssetBundle names and their relationships explicitly in your code.
For more information and a code example, refer to [Handling dependencies between AssetBundles](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetBundles-Dependencies.html).
## Managing loaded AssetBundles
Unity recommends using the [Addressables](http://docs.unity3d.com/Packages/com.unity.addressables@latest/index.html) package for managing AssetBundles, dependencies, and assets, as it simplifies the process. For manual management, understanding proper AssetBundle loading and unloading is critical to avoid memory duplication or missing objects.
### Recommended unload strategies
The [`AssetBundle.Unload`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundle.Unload.html) function removes the AssetBundle header and associated structures from memory, with the boolean argument determining whether loaded objects are also unloaded.
Most projects should use `AssetBundle.Unload(true)` to prevent object duplication. Common strategies include:
  * **Defined unload points** : Unload transient AssetBundles at specific times, such as during level transitions or loading screens.
  * **Reference-counting** : Track object usage and unload AssetBundles only when all constituent objects are unused. For an example implementation, refer to [Example unload strategy: reference counting](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetBundles-Dependencies.html#reference-counting).


If you must use `Unload(false)`, unwanted objects can only be unloaded in one of the following ways:
  * References elimination: Remove all references to an object and call [`Resources.UnloadUnusedAssets`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Resources.UnloadUnusedAssets.html).
  * Non-additive **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) loading: Load a new scene non-additively to destroy current scene objects, automatically invoking `Resources.UnloadUnusedAssets`.


## Additional resources
  * [Managing Loaded AssetBundles](https://unity3d.com/fr/learn/tutorials/topics/best-practices/assetbundle-usage-patterns#Managing_Loaded_Assets).


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/assetbundles-file-format.html)
AssetBundle file format reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetBundles-Dependencies.html)
Handling dependencies between AssetBundles
