* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/LoadingResourcesatRuntime.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [Assets and media](https://docs.unity3d.com/6000.0/Documentation/Manual/assets-and-media.html)
  * [Scripting with assets](https://docs.unity3d.com/6000.0/Documentation/Manual/ScriptingAssets.html)
  * Load assets at runtime


[](https://docs.unity3d.com/6000.0/Documentation/Manual/ScriptingAssets.html)
Scripting with assets
[](https://docs.unity3d.com/6000.0/Documentation/Manual/StreamingAssets.html)
Stream assets directly into a build
# Load assets at runtime
The [`Resources`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Resources.html) class allows you to find and access objects that are in a `Resources` folder in your project.
**Important** : The Resources system is a performance-intensive way to organize assets in your project and isn’t recommended. Use [AssetBundles](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetBundlesIntro.html) and the [Addressables](https://docs.unity3d.com/Packages/com.unity.addressables@latest) package instead.
You can use the Resources system to make an asset available to a project without loading it in as part of a **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene). When you add content to a folder named `Resources` in your project, Unity makes it available to load when needed, independent of the scenes that you build. However, having the content constantly available at runtime has significant performance impact on your project.
## Avoid using the Resources system
It’s best practice not to use the `Resources` system for the following reasons:
  * It makes memory management more difficult.
  * Placing a lot of content in the `Resources` folder slows down application startup and the length of builds.
  * The `Resources` system makes it harder to deliver custom content to specific platforms and prevents incremental content upgrades.
  * Making changes to assets in the `Resources` folder requires a player rebuild and redeployment, whereas AssetBundles are better suited for incremental content updates.


[AssetBundles](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetBundlesIntro.html) and the Addressables package are the recommended alternative.
Unity combines all assets and objects in the `Resources` folder into a single serialized file when you build a project. This file contains metadata and indexing information, which includes a serialized lookup tree that Unity uses to resolve a given object’s name into its appropriate File GUID and Local ID. It’s also used to locate the object at a specific byte offset in the serialized file’s body.
On most platforms, the lookup data structure is a balanced search tree, which has a construction time that causes the index’s loading time to grow more-than-linearly as the number of objects in `Resources` folders increases.
This operation is unskippable and happens at application startup time while the initial non-interactive splash screen is displayed. For example, initializing a `Resources` system containing 10,000 assets takes several seconds on low-end mobile devices, even though most of the objects contained in `Resources` folders are rarely needed to load into an application’s first scene.
## When to use the Resources system
The `Resources` system can be helpful in the following situations:
  * For rapid prototyping. Remove the `Resources` folder when a project moves into full production.
  * In smaller projects if the content meets the following criteria: 
    * It’s needed throughout the project’s lifetime.
    * It’s not memory-intensive.
    * It doesn’t need patching, or doesn’t vary across platforms and devices.
    * It’s used for minimal bootstrapping.


Examples of the latter include MonoBehaviour singletons used to host **prefabs** An asset type that allows you to store a GameObject complete with components and properties. The prefab acts as a template from which you can create new object instances in the scene. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Prefabs.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Prefab), or ScriptableObject instances containing third-party configuration data, such as a Facebook App ID.
## Using the Resources system
To use the Resources system:
  1. Create a new folder called `Resources` in your project, and add assets to it. Unity then makes these assets available even if they’re not directly referenced in a scene. **Note:** You can have multiple `Resources` folders located at different subfolders within your `Assets` folder, and packages can also contain `Resources` folders
  2. Whenever you want to load an asset from one of these folders, call [`Resources.Load`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Resources.Load.html) in your code. Only assets in the `Resources` folder can be accessed in this way.


Unity stores all assets in the `Resources` folders and their dependencies in a file in the build output called `resources.assets`. If a scene in the build references an asset Unity serializes that asset into a `sharedAssets*.assets` file instead.
Additional assets might end up in the `resources.assets` file if they’re dependencies. For example, a material in the `Resources` folder might reference a texture outside of the `Resources` folder. In that case the texture is also included in the `resources.assets` file, but isn’t available to load directly.
### Resource unloading
If you want to destroy scene objects that were loaded using [`Resources.Load`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Resources.Load.html) before loading another scene, call [`Object.Destroy`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.Destroy.html) on them. To release assets and reclaim memory, use [`Resources.UnloadUnusedAssets`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Resources.UnloadUnusedAssets.html).
## Additional resources
  * [Addressables](https://docs.unity3d.com/Packages/com.unity.addressables@latest)
  * [Optimizing Assets](https://docs.unity3d.com/6000.0/Documentation/Manual/assets-optimizing.html)
  * [AssetBundles](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetBundlesIntro.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/ScriptingAssets.html)
Scripting with assets
[](https://docs.unity3d.com/6000.0/Documentation/Manual/StreamingAssets.html)
Stream assets directly into a build
