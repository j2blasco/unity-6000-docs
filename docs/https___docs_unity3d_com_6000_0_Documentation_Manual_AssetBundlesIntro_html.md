* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/AssetBundlesIntro.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [Assets and media](https://docs.unity3d.com/6000.0/Documentation/Manual/assets-and-media.html)
  * [Combining assets into bundles](https://docs.unity3d.com/6000.0/Documentation/Manual/assetbundles-section.html)
  * Introduction to AssetBundles


[](https://docs.unity3d.com/6000.0/Documentation/Manual/assetbundles-section.html)
Combining assets into bundles
[](https://docs.unity3d.com/6000.0/Documentation/Manual/assetbundles-creating.html)
Creating AssetBundles
# Introduction to AssetBundles
An AssetBundle is an archive file that you can use to group together assets to create downloadable content (DLC), or reduce the initial installation size of your application. You can also use AssetBundles to load optimized platform-specific assets, or lower memory usage at runtime.
An AssetBundle can contain platform-specific non-code assets, such as models, textures, **prefabs** An asset type that allows you to store a GameObject complete with components and properties. The prefab acts as a template from which you can create new object instances in the scene. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Prefabs.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Prefab), **audio clips** A container for audio data in Unity. Unity supports mono, stereo and multichannel audio assets (up to eight channels). Unity can import .aif, .wav, .mp3, and .ogg audio file format, and .xm, .mod, .it, and .s3m tracker module formats. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioClip.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#AudioClip), or entire **scenes** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) that Unity then loads at runtime. AssetBundles are platform-specific because Unity builds asset data into formats based on the [`BuildTarget`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildTarget.html) you select in [Build Profiles](https://docs.unity3d.com/6000.0/Documentation/Manual/BuildSettings.html)A set of customizable configuration settings to use when creating a build for your target platform. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/build-profiles.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Buildprofile). For example, an AssetBundle built for iOS isn’t compatible for Android. 
You can also [compress AssetBundles](https://docs.unity3d.com/6000.0/Documentation/Manual/assetbundles-compression-format.html) using LZMA or LZ4 to efficiently distribute the archives.
To build and define AssetBundles, you can use the high-level [Addressables](http://docs.unity3d.com/Packages/com.unity.addressables@latest) package, which provides a way of defining and building AssetBundles from the Unity Editor. If you prefer low-level API control, you can use the [`BuildPipeline.BuildAssetBundles`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildPipeline.BuildAssetBundles.html), [`AssetBundle`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundle.html), and [`UnityWebRequestAssetBundle`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequestAssetBundle.html) native APIs.
## Reasons to use AssetBundles
Using AssetBundles can help with content distribution and optimizing your application’s performance. The following are benefits of using the AssetBundle system:
  * **Dynamic content delivery** : You can use AssetBundles to load assets on demand, which is especially useful for games with downloadable content (DLC), episodic updates, or live service models. It also helps efficiently manage memory, ensuring only the assets that your application needs are loaded into memory.
  * **Reduced build size** : Moving assets to AssetBundles can reduce the initial application build size, which is important for mobile games or platforms with strict size limitations.
  * **Platform compatibility** : You can create AssetBundles for different platforms, reducing the need to include platform-specific assets in your application’s build.


AssetBundles are useful if you want to optimize asset loading, such as only streaming content near a character’s location, only loading relevant localized content, or loading assets in the background. However, the AssetBundle system provides low-level asset management, so you might want to consider using the [Addressables](http://docs.unity3d.com/Packages/com.unity.addressables@latest) package, which provides a higher level way of managing AssetBundles in your project.
If you’re prototyping, or have a particularly small project, you might want to consider using the [resources system](https://docs.unity3d.com/6000.0/Documentation/Manual/LoadingResourcesatRuntime.html).
## Structure of an AssetBundle
The AssetBundle is a container file format, similar to a zip file. It contains the following file types in a binary-format header:
  * **Serialized files** : Contains serialized Unity objects. This is the same binary file format used in Player builds. The output depends on what the AssetBundle contains: 
    * Only assets: Unity creates a single serialized file.
    * Only scenes: Unity creates two serialized files per scene. One file contains the objects from the scene hierarchy, and the second contains any referenced objects.
  * **Resource files:** Contains chunks of binary data stored separately for certain assets such as textures and audio. This separation allows Unity to use multithreaded code to efficiently load the assets from disk.


The AssetBundle file always includes a serialized [`AssetBundle`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundle.html) object which acts like a directory for the contents of the AssetBundle. You can use the `AssetBundle` instance to load assets from a specific AssetBundle archive in your code. 
## AssetBundle support between Unity versions
Any AssetBundles you create with older versions of Unity are usually compatible with newer versions of Unity. However, if there are large changes between versions, Unity might not be able to load the data, and you must rebuild the AssetBundle with a newer version of Unity. 
Unity doesn’t support forward-compatibility of AssetBundles, so you can’t load an AssetBundle built with a newer version of Unity into an older version of Unity.
Unity serializes AssetBundles based on the Unity version and the C# types present during their creation. Unity stores the information in a type tree structure and uses this information when it loads the objects from different versions of the Unity Editor.
**Tip** : By default, Unity includes the version of the Unity Editor used to build the AssetBundle inside the AssetBundle header. This information can result in AssetBundles unnecessarily being rebuilt. To avoid this, you can exclude the Editor version from the header. For more information, refer to [`BuildAssetBundleOptions.AssetBundleStripUnityVersion`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildAssetBundleOptions.AssetBundleStripUnityVersion.html).
## Script support
AssetBundles can’t contain assemblies, so you can’t use them to distribute new C# classes or changes to existing classes. However, you can use an AssetBundle to distribute precompiled object instances, such `ScriptableObject` assets. 
Unity matches objects based on their assembly, namespace, and class names. It then creates an object that’s an instance of that class, using the serialized values to set the fields of the object. It uses the information stored in the type tree to adjust field mappings for different versions of Unity.
Unity uses the [conditional compilation](https://docs.unity3d.com/6000.0/Documentation/Manual/platform-dependent-compilation.html) information in your code to determine the fields to include in an AssetBundle. If a field doesn’t contain a conditional scripting symbol, then Unity doesn’t include that information in the AssetBundle’s type tree.
## Building AssetBundles
You can use the following method to build AssetBundles:
  * **Addressables** : The [Addressables](http://docs.unity3d.com/Packages/com.unity.addressables@latest) package is a user-friendly way of defining and building AssetBundles from the Unity Editor. It simplifies AssetBundle creation and management with a high-level API.
  * **Native APIs** : `BuildPipeline.BuildAssetBundles`, `AssetBundle`, and `UnityWebRequestAssetBundle` are native APIs you can use to build AssetBundles, but they require manual dependency management, and you must write your own build script to use them.


For more information, refer to [Build assets into an AssetBundle](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetBundles-Building.html).
### Building multiple AssetBundles
When you build or rebuild AssetBundles, it’s best practice to use a single [`AssetBundle`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundle.html) API call to build all the project’s AssetBundles together. AssetBundles can reference and have dependencies on other AssetBundles. For example, a material in one AssetBundle can reference a texture in another AssetBundle. When you build AssetBundles together, Unity automatically manages the references and dependencies between them.
## Additional resources
  * [Addressables package](http://docs.unity3d.com/Packages/com.unity.addressables@latest)
  * [`BuildPipeline.BuildAssetBundles` API documentation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildPipeline.BuildAssetBundles.html)
  * [Organizing assets into AssetBundles](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetBundles-Preparing.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/assetbundles-section.html)
Combining assets into bundles
[](https://docs.unity3d.com/6000.0/Documentation/Manual/assetbundles-creating.html)
Creating AssetBundles
