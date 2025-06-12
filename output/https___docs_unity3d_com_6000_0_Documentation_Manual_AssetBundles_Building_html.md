* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/AssetBundles-Building.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [Assets and media](https://docs.unity3d.com/6000.0/Documentation/Manual/assets-and-media.html)
  * [Combining assets into bundles](https://docs.unity3d.com/6000.0/Documentation/Manual/assetbundles-section.html)
  * [Creating AssetBundles](https://docs.unity3d.com/6000.0/Documentation/Manual/assetbundles-creating.html)
  * Build assets into an AssetBundle


[](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetBundles-Preparing.html)
Organizing assets into AssetBundles
[](https://docs.unity3d.com/6000.0/Documentation/Manual/Build-MultiProcess.html)
Build AssetBundles in parallel processes
# Build assets into an AssetBundle
To build assets into an AssetBundle, you must assign assets to an AssetBundle, either in the Unity Editor or through a script. You can then create and use a script to build the AssetBundles. For information on the best approaches for organizing assets into AssetBundles, refer to [Preparing assets for AssetBundles](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetBundles-Preparing.html).
**Note** : This workflow describes the creation of AssetBundles with the built-in [`BuildPipeline.BuildAssetBundles`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildPipeline.BuildAssetBundles.html) API. A more user-friendly alternative is to use the [Addressables](http://docs.unity3d.com/Packages/com.unity.addressables@latest/index.html) package.
## Assign assets to AssetBundles in the Editor
To assign a given asset to an AssetBundle in the Unity Editor, perform the following steps:
  1. Select the asset in the **Project window** A window that shows the contents of your `Assets` folder (Project tab) [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/ProjectView.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Projectwindow) and view it in the [Inspector](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector).
  2. Use the **AssetBundle** left-hand dropdown menu at the bottom of the Inspector window to assign or create an AssetBundle: 
     * To create a new AssetBundle, select the left-hand dropdown and select **New** , or choose an existing AssetBundle from the list. **Tip:** To organize AssetBundles with subfolders, use the `/` character. For example, use the AssetBundle name `environment/forest` to create an AssetBundle named `forest` under an `environment` subfolder.
  3. Optionally use the right-hand menu to assign or create an [AssetBundle variant](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetBundles-Preparing.html#assetbundle-variants): 
     * To create a new variant, select the right-hand dropdown and select **New** , or choose an existing variant from the list.


### Assigning multiple assets to an AssetBundle
You can assign an AssetBundle to a folder in your project. By default, all assets in that folder are assigned to the same AssetBundle as the folder. However, the AssetBundle assignments for individual assets takes precedence. To assign an AssetBundle to a folder:
  1. Select the folder in its containing parent folder the Project window.
  2. Use the **AssetBundle** dropdown to assign a new or existing AssetBundle to the folder.


You can also select multiple assets and assign them to an AssetBundle. However, assigning assets to an AssetBundle in this way overrides any existing AssetBundle assignments for those assets.
## Assign assets to AssetBundles with a script
To assign assets to AssetBundles in your code, use the [`BuildPipeline.BuildAssetBundles`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildPipeline.BuildAssetBundles.html) method with an array of [`AssetBundleBuild`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundleBuild.html) structures. This approach overrides any AssetBundle assignments made in the Inspector.
If you want your script to respect AssetBundle assignments made in the Inspector, use [`AssetDatabase.GetAllAssetBundleNames`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GetAllAssetBundleNames.html) and [`AssetDatabase.GetAssetPathsFromAssetBundle`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GetAssetPathsFromAssetBundle.html) to retrieve the necessary information and populate the `AssetBundleBuild` array.
## Build AssetBundles
To build AssetBundles, you must create a build script and place it a folder called `Editor` in the `Assets` folder. 
The following script is an example of an AssetBundle build script. It adds a menu item at the bottom of the Assets menu called **Build AssetBundles**. When you select **Build AssetBundles** the `BuildAllAssetBundles` method is called. A progress bar appears while the build takes all the assets you labeled with an AssetBundle name and uses them to populate AssetBundles at the path that `assetBundleDirectory` defines.
```
using UnityEditor;
using System.IO;

public class CreateAssetBundles
{
    [MenuItem("Assets/Build AssetBundles")]
    static void BuildAllAssetBundles()
    {
        string assetBundleDirectory = "Assets/AssetBundles";
        if(!Directory.Exists(assetBundleDirectory))
            Directory.CreateDirectory(assetBundleDirectory);

        BuildPipeline.BuildAssetBundles(assetBundleDirectory,
                                        BuildAssetBundleOptions.None,
                                        BuildTarget.StandaloneWindows);
    }
}

```

The script has the following arguments:
  * `assetBundleDirectory`: The directory to output the AssetBundles to within the current Unity project. The folder doesn’t need to be in the `Assets` folder. In the code example, it creates the folder on demand if it doesn’t exist.
  * `BuildAssetBundleOptions.None`: The default value for the build options argument. You can use this argument to specify one or more flags to enable a variety of optional behaviours. For example, this argument controls the choice of [compression algorithm](https://docs.unity3d.com/6000.0/Documentation/Manual/assetbundles-compression-format.html). For a full list of options available refer to [the `BuildAssetBundleOptions` API documentation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildAssetBundleOptions.html).
  * `BuildTarget.StandaloneWindows`: Defines the [target platform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildTarget.html) for the AssetBundles. Alternatively, you can call `EditorUserBuildSettings.activeBuildTarget`, which returns the platform profile currently set as active in the [Build Profiles](https://docs.unity3d.com/6000.0/Documentation/Manual/build-profiles.html)A set of customizable configuration settings to use when creating a build for your target platform. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/build-profiles.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Buildprofile) window.


### Performing a clean build
You should perform a [clean build](https://docs.unity3d.com/6000.0/Documentation/Manual/incremental-build-pipeline.html) when you do an official AssetBundle release. To perform a clean build, pass the [`BuildAssetBundleOptions.ForceRebuildAssetBundle`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildAssetBundleOptions.ForceRebuildAssetBundle.html) flag as an option to `BuildPipeline.BuildAssetBundles`.
In some projects, you can delete the `Library/ShaderCache` directory to decrease the time required for the next Player or AssetBundle build, especially for projects where **shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) compilation is a lengthy process. This cache isn’t cleared when you specify `BuildAssetBundleOptions.ForceRebuildAssetBundle`.
An alternative way to perform a clean build is to stop Unity, delete your project’s `Library` directory, then reopen Unity. This process is time consuming because all the project assets need to be reimported and other data is regenerated.
For more information, refer to [Incremental build pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/incremental-build-pipeline.html).
### Changing target platform
The [`BuildPipeline.BuildAssetBundles`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildPipeline.BuildAssetBundles.html) API allows you to specify the target and subtarget platform for deploying AssetBundles.
If the specified target platform differs from the one configured in [Build Profiles](https://docs.unity3d.com/6000.0/Documentation/Manual/build-profiles.html), Unity must recompile Editor **scripts** A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/creating-scripts.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scripts) and reimport assets such as textures that have platform-specific representations. After the build is complete, Unity restores the original target platform settings.
This process can significantly increase build times. Additionally, the script containing the `BuildPipeline.BuildAssetBundles` call continues to execute as compiled for the current target platform, not the specified build target. This can cause issues if the build script or callback scripts rely on platform-specific code or assemblies.
To avoid this issue, ensure that any code executed during a build dynamically checks the target platform (for example, using `if` statements) rather than relying on platform-specific conditional compilation (such as, `#ifdef` statements).
For command line builds, use the `--buildTarget` [command line argument](https://docs.unity3d.com/6000.0/Documentation/Manual/EditorCommandLineArguments.html) to align the target platform with your build requirements.
## Download and load AssetBundles and assets
You can distribute AssetBundles in the following ways:
  * Locate the files inside the [StreamingAssets](https://docs.unity3d.com/6000.0/Documentation/Manual/StreamingAssets.html) folder and include them with the player build.
  * Host the files with a web service such as [Unity’s Cloud Content Delivery](https://docs.unity.com/ugs/manual/ccd/manual/UnityCCD) and use [`UnityWebRequestAssetBundle`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityWebRequestAssetBundle.html) to download them.
  * Distribute a download or installation code. This approach takes more development work allows you to control aspects such as **compression** A method of storing data that reduces the amount of storage space it requires. See [Texture Compression](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextureImporterOverride), [Animation Compression](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AnimationClip.html#AssetProperties), [Audio Compression](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioClip.html), [Build Compression](https://docs.unity3d.com/6000.0/Documentation/Manual/ReducingFilesize.html).  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#compression), caching, [patching](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetBundles-Integrity.html) and validation before loading the file using Unity APIs.


To load AssetBundles and access the AssetBundle object in your runtime code, either use the load methods in [`AssetBundle`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundle.html) or [`UnityWebRequestAssetBundle`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityWebRequestAssetBundle.html).
To reclaim memory used by a loaded AssetBundle, call [`AssetBundle.Unload(bool)`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundle.Unload.html) or [`AssetBundle.UnloadAsync(bool)`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundle.Unload.html).
For more information on APIs that load and unload AssetBundles, refer to [Loading assets from AssetBundles](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetBundles-Native.html).
## Additional resources
  * [AssetBundle compression formats](https://docs.unity3d.com/6000.0/Documentation/Manual/assetbundles-compression-format.html)
  * [Preparing assets for AssetBundles](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetBundles-Preparing.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetBundles-Preparing.html)
Organizing assets into AssetBundles
[](https://docs.unity3d.com/6000.0/Documentation/Manual/Build-MultiProcess.html)
Build AssetBundles in parallel processes
