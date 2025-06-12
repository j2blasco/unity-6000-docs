* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/assetbundles-file-format.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [Assets and media](https://docs.unity3d.com/6000.0/Documentation/Manual/assets-and-media.html)
  * [Combining assets into bundles](https://docs.unity3d.com/6000.0/Documentation/Manual/assetbundles-section.html)
  * [Creating AssetBundles](https://docs.unity3d.com/6000.0/Documentation/Manual/assetbundles-creating.html)
  * AssetBundle file format reference


[](https://docs.unity3d.com/6000.0/Documentation/Manual/assetbundles-compression-format.html)
AssetBundle compression formats
[](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetBundles-Native.html)
Loading assets from AssetBundles
# AssetBundle file format reference
When you use `BuildPipeline.BuildAssetBundles` to [build AssetBundles](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetBundles-Building.html), Unity writes the following files to a specified output directory:
  * [The AssetBundle files](https://docs.unity3d.com/6000.0/Documentation/Manual/assetbundles-file-format.html#assetbundle-files).
  * [A `.manifest` file for each AssetBundle file](https://docs.unity3d.com/6000.0/Documentation/Manual/assetbundles-file-format.html#manifest-files).
  * [A manifest bundle](https://docs.unity3d.com/6000.0/Documentation/Manual/assetbundles-file-format.html#manifest-bundles).


**Note:** If you use the [Addressables package](http://docs.unity3d.com/Packages/com.unity.addressables@latest) to build AssetBundles, it produces an AssetBundle file but no manifest files or manifest bundles.
## Archive file format
The Unity archive file format is a generic packaging format which can store any type of file, similar to a .zip file. Archive files are [mounted](https://en.wikipedia.org/wiki/Mount_\(computing\)) into Unity’s [virtual file system](https://en.wikipedia.org/wiki/Virtual_file_system), which allows them to be accessed in a uniform way across different platforms.
The archive format is used for AssetBundles, where archive files are created as a final stage of the [AssetBundle build process](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetBundles-Building.html). They are mounted into the Unity virtual file system when the AssetBundle is [loaded](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetBundles-Native.html).
The archive format is also used for Players built with LZ4 **compression** A method of storing data that reduces the amount of storage space it requires. See [Texture Compression](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextureImporterOverride), [Animation Compression](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AnimationClip.html#AssetProperties), [Audio Compression](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioClip.html), [Build Compression](https://docs.unity3d.com/6000.0/Documentation/Manual/ReducingFilesize.html).  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#compression), in which case the archive is mounted automatically when the Player runs. For more information, refer to the [`BuildOptions.CompressWithLz4` API documentation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildOptions.CompressWithLz4.html)
In most cases you don’t need to interact with archives at a low level and should use the [`AssetBundle`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundle.html) API or the Addressables package instead. However, for more information on how you can manage archive files directly with low-level APIs, refer to the [`ArchiveFileInterface`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.IO.Archive.ArchiveFileInterface.html) API documentation.
## AssetBundle files
The AssetBundle file is an [archive file](https://docs.unity3d.com/6000.0/Documentation/Manual/assetbundles-file-format.html#archive-format) that contains multiple files which loads in assets at runtime. The following diagram contains an example of an AssetBundle file layout:
  * It contains a series of containers, where the outermost is an instance of the archive file system with the same name as the AssetBundle.
  * `ArchiveFileSystem` has two containers: 
    * Main `SerializedFile`, which represents the main AssetBundle file in Unity’s serialized file format. It contains the AssetBundle object and the objects from all the assets included (explicitly or implicitly) in the AssetBundle.
    * An audio resource in the `.resource` format. All audio or video is stored in a `.resource` format, and textures are stored in `.resS` format.

![Internal structure of a typical AssetBundle file depicted as a series of containers. ](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/AssetBundles-Building-0.png) Internal structure of a typical AssetBundle file depicted as a series of containers. 
The content inside a **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) AssetBundle is similar, but it’s optimized for stream loading of individual scenes. It contains two `SerializedFile` instances per scene.
## Examining AssetBundle file contents
In some cases you might want to look directly inside an AssetBundle file, or compare the contents of two AssetBundles. 
The Unity Editor installation includes the `WebExtract` and `Binary2Text` executables. You can use`WebExtract` to extract the files nested inside the AssetBundle, similar to extracting a zip file. You can use `Binary2Text` to produce a text format dump of the contents of a binary `SerializedFile`. Its output is similar to the YAML format used by Unity.
You can also use `UnityDataTools` with the `dump` argument to view the contents of an AssetBundle’s SerializedFile.
The raw content of serialized files is often highly technical and large, especially when it includes **shaders** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader), meshes, or binary data. However, these dumps can be useful to pinpoint a problem with specific objects in a file. Using a diff tool to compare the extracted content of two similar AssetBundles can help identify the differences.
## Manifest files
For every AssetBundle generated, Unity generates an associated manifest file. The manifest file has the extension `.manifest` and you can open it with any text editor. 
It include the following content:
  * The hashes required for incremental build calculations and content verification. For more information, refer to [`BuildPipeline.GetHashForAssetBundle`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildPipeline.GetHashForAssetBundle.html).
  * The cyclic redundancy check (CRC). You can get this information with [`BuildPipeline.GetCRCForAssetBundle`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildPipeline.GetCRCForAssetBundle.html).
  * The list of scenes or assets in the AssetBundle.
  * The list of any AssetBundles that this AssetBundle depends on, as absolute paths.
  * Type usage information which is used for type stripping. This includes usage of Unity objects, MonoBehaviour and ScriptableObject-derived classes, and [`SerializeReference`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializeReference.html) types. For more information, refer to [`BuildPlayerOptions.assetBundleManifestPath`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildPlayerOptions-assetBundleManifestPath.html).


The following is an example of the contents of an AssetBundle manifest file:
```
ManifestFileVersion: 0
UnityVersion: 6000.2.0a6
CRC: 4208470199
Compression: None
Hashes:
  AssetFileHash:
    serializedVersion: 2
    Hash: 81197c4674c1f389b3568a0aa1b41119
  TypeTreeHash:
    serializedVersion: 2
    Hash: 3c2131fb3360d17991621f547033218e
  IncrementalBuildHash:
    serializedVersion: 2
    Hash: 489e266cfc1b361a94c3efc39afecb54
HashAppended: 0
ClassTypes:
- Class: 1
  Script: {instanceID: 0}
- Class: 4
  Script: {instanceID: 0}
SerializeReferenceClassIdentifiers: []
Assets:
- Assets/Scenes/Scene2.unity
- Assets/Scenes/SampleScene.unity
Dependencies:
- C:/MyBuild/audio.bundle
- C:/MyBuild/sprites.bundle

```

Unity uses the `.manifest` files for its [incremental build pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/incremental-build-pipeline.html). When performing a build, Unity checks the existing AssetBundles and `.manifest` files to determine if the AssetBundle needs to be rebuilt or can be reused. If you delete the `.manifest` files then Unity always rebuilds the AssetBundles from scratch.
Manifest files aren’t required to load the AssetBundles, so you don’t need to distribute them.
## Manifest bundles
Unity additionally generates a manifest bundle, which is an AssetBundle file named after the directory it’s located in. It contains the [`AssetBundleManifest`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundleManifest.html) object which Unity uses to determine which bundle dependencies to load at runtime. 
There are two additional files generated by the build.
The first is a small AssetBundle that is named after the directory that it’s located in (where the AssetBundles were built to). This file is called the `Manifest Bundle` and it contains the [AssetBundleManifest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundleManifest.html) object which will be useful for figuring out which bundle dependencies to load at runtime. For information on how to use this bundle, refer to [Loading assets from bundles](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetBundles-Native.html).
The manifest bundle also includes its own `.manifest` file. The following is an example of a manifest bundle’s manifest file:
```
ManifestFileVersion: 0
AssetBundleManifest:
  AssetBundleInfos:
    Info_0:
      Name: scene1assetbundle
      Dependencies: {}

```

The `.manifest` file for the manifest bundle records how AssetBundles relate, and what their dependencies are. This information is similar to the information recorded by the `AssetBundleManifest` object inside the manifest bundle. 
The manifest file is important to prevent code stripping for unused types that you use in your AssetBundle. If you have enabled [code stripping](https://docs.unity3d.com/6000.0/Documentation/Manual/managed-code-stripping.html) in your project, set [`BuildPlayerOptions.assetBundleManifestPath`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildPlayerOptions-assetBundleManifestPath.html) to pass the path to this manifest when performing player builds.
## Build Report
AssetBundle builds additionally generate a `BuildReport` file which is a Unity `SerializedFile` written to `Library/LastBuild.buildreport` inside the project directory. This file is useful to view a summary of the timings for build steps and a detailed view of the contents of the AssetBundle. You can use the [`BuildReport`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Reporting.BuildReport.html) API to read information from the `BuildReport` file.
You can also use the following tools to view the content of the `BuildReport` file:
  * [Project Auditor](https://docs.unity3d.com/Packages/com.unity.project-auditor@latest)
  * [Build Report Inspector](https://docs.unity3d.com/Packages/com.unity.build-report-inspector@latest)


## Additional resources
  * [Loading assets from bundles](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetBundles-Native.html)
  * [`AssetBundleManifest` API documentation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundleManifest.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/assetbundles-compression-format.html)
AssetBundle compression formats
[](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetBundles-Native.html)
Loading assets from AssetBundles
