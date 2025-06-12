* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/Build-MultiProcess.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [Assets and media](https://docs.unity3d.com/6000.0/Documentation/Manual/assets-and-media.html)
  * [Combining assets into bundles](https://docs.unity3d.com/6000.0/Documentation/Manual/assetbundles-section.html)
  * [Creating AssetBundles](https://docs.unity3d.com/6000.0/Documentation/Manual/assetbundles-creating.html)
  * Build AssetBundles in parallel processes


[](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetBundles-Building.html)
Build assets into an AssetBundle
[](https://docs.unity3d.com/6000.0/Documentation/Manual/assetbundles-compression-format.html)
AssetBundle compression formats
# Build AssetBundles in parallel processes
To speed up AssetBundle building, you can use the Asset Database to parallel import assets and cache intermediate files with the **Multi-Process AssetBundle Building** setting. You can use this setting with AssetBundles built with `BuildPipeline.BuildAssetBundles`, but not Addressables.
When you enable parallel processsing of AssetBundles, Unity compiles **shaders** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) in its own dedicated build step. This can make it clearer to identify how much time your project spent on compiling shaders when you [analyze asset build times](https://docs.unity3d.com/6000.0/Documentation/Manual/import-analyze.html). You can also use the setting together with [Unity Accelerator](https://docs.unity3d.com/6000.0/Documentation/Manual/UnityAccelerator.html) to share artifacts between machines, and use the [Asset Pipeline Project settings](https://docs.unity3d.com/6000.0/Documentation/Manual/class-EditorManager.html#asset-pipeline) to speed up import times. For more information, refer to [Controlling the import worker processes](https://docs.unity3d.com/6000.0/Documentation/Manual/ParallelImport.html#controlling-the-import-worker-processes).
The **Multi-Process AssetBundle Building** setting evaluates how objects interact across all AssetBundles, rather than within the scope of individual AssetBundles. For example, if a material requires a specific shader feature, that feature is enabled even if the shader is in a different AssetBundle. This approach might increase shader compilation times, particularly when the same shader is used in multiple AssetBundles. For more information, refer to [Shader keywords](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-keywords.html).
When you use multi-process building, the disk space used by your Project’s `Library` folder might grow larger because Unity uses the Asset Database to cache intermediate build artifacts. These artifacts are fully flushed at the beginning of a build when the [`BuildAssetBundleOptions.ForceRebuildAssetBundle`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildAssetBundleOptions.ForceRebuildAssetBundle.html) flag is specified.
## Enable building AssetBundles in parallel processes
To enable **Multi-Process AssetBundle Building** , perform the following steps:
  1. Go to **Edit > Project Settings** to open the Project Settings window.
  2. Select the **Editor** category.
  3. Under **Build Pipeline** , enable **Multi-Process AssetBundle Building**.


You can use [`EditorBuildSettings.UseParallelAssetBundleBuilding`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorBuildSettings.UseParallelAssetBundleBuilding.html) to control this setting in your **scripts** A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/creating-scripts.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scripts).
## Unsupported settings
The following settings aren’t compatible with the **Multi-Process AssetBundle Building** setting: 
  * The [Optimize Mesh](https://docs.unity3d.com/6000.0/Documentation/Manual/FBXImporter-Model.html#meshprops) setting is silently disabled during the build.
  * [Sprite Atlas V1](https://docs.unity3d.com/6000.0/Documentation/Manual/class-EditorManager.html) isn’t supported and an error is printed to the Console if you attempt to build with these settings enabled. Update to [Sprite Atlas V2](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/atlas/v2/v2-landing.html) to build successfully.


## Build output
The output from a multi-process build isn’t binary-identical to a non-multi-process build. This is due to differences in object naming or ordering. However, the output is functionally identical. If you change to multi-process building after shipping AssetBundle files, all AssetBundle files might change. This can trigger downloads for all live users.
The AssetBundle hash is a hash value of the uncompressed contents of the AssetBundle. This serves as a file version identifier that’s independent of the **compression** A method of storing data that reduces the amount of storage space it requires. See [Texture Compression](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextureImporterOverride), [Animation Compression](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AnimationClip.html#AssetProperties), [Audio Compression](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioClip.html), [Build Compression](https://docs.unity3d.com/6000.0/Documentation/Manual/ReducingFilesize.html).  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#compression) and doesn’t incorporate the content of the AssetBundle header. You can use the [`BuildAssetBundleOptions.AssetBundleStripUnityVersion`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildAssetBundleOptions.AssetBundleStripUnityVersion.html) flag to exclude the Unity version from the AssetBundle content and from the hash.
You can only determine the hash of an AssetBundle by performing a full build. Therefore [`AssetBundleManifest.GetAssetBundleHash`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundleManifest.GetAssetBundleHash.html) returns 0 when `BuildPipeline.BuildAssetBundles` is called with [`BuildAssetBundleOptions.DryRunBuild`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildAssetBundleOptions.DryRunBuild.html).
## Build callback compatibility
If your project uses [build callbacks](https://docs.unity3d.com/6000.0/Documentation/Manual/incremental-build-pipeline.html), you might need to update your code to make it compatibile with multi-process building.
During a build, Unity loads and resaves **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) files into the output format. Script code can run during this process, such as through the [`IProcessSceneWithReport.OnProcessScene`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.IProcessSceneWithReport.OnProcessScene.html) callback. In multi-process building, this code runs within an `Import` job inside an `AssetDatabase` worker process, similar to how a [scripted importer](https://docs.unity3d.com/6000.0/Documentation/Manual/ScriptedImporters.html) can run.
Scene callbacks that only work with the loaded scene’s state function correctly in this context. However, the following scenarios might cause issues:
  * **Modifying assets** : Avoid creating, deleting, or modifying external assets in a build callback. Unity enforces this with protections that throw scripting exceptions if such calls are made.
  * **Dependency tracking** : If a build callback needs to read other assets not explicitly referenced by the scene, use [`BuildPipelineContext.DependOnAsset`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.BuildPipelineContext.DependOnAsset.html) to track the dependency. Without this, incremental builds might reuse outdated cached artifacts, and the callback won’t be invoked.
  * **Singletons and global state** : Multi-process building loads scenes and assets in separate worker processes, not sequentially in the main Unity process. Code relying on shared global data, such as singletons, might fail. Refactor such code to store data in the scene, an asset, or a temporary file.


### Callback versioning
Incremental builds only invoke a build callback if the scene or its dependencies have changed after the last build. To force a callback to run after modifying its script, increment the [`BuildCallbackVersion`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.BuildCallbackVersionAttribute.html) attribute. If this attribute isn’t specified, the default version is 1.
Other scripting code may also run during a build, such as the [`Awake`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.Awake.html) method on MonoBehaviour-derived classes with the [`ExecuteInEditMode`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ExecuteInEditMode.html) attribute. If your code performs actions that aren’t allowed during an AssetDatabase import, you might need to modify it. **Tip:** The [`BuildPipeline.isBuildingPlayer`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildPipeline.isBuildingPlayer.html) API returns `true` during AssetBundle builds, so you can use it to add conditional logic. Fot rcample, you can bypass problematic code during a build while keeping it functional in Play mode.
## Using diagnostics flags for troubleshooting
You can use [diagnostic flags](https://docs.unity3d.com/6000.0/Documentation/Manual/Preferences.html#diagnostics) in the Preferences window to collect detailed information about an AssetBundle build. To enable these flags go to **Settings** > **Diagnostics** > **Build Pipeline**.
**Flag** | **Description**  
---|---  
`BuildPipelineBinaryBackwardCompatibilityMode` | For multi-process AssetBundle builds only. Enable to change the build to match the behavior of the existing AssetBundle build logic.  
`BuildPipelineTEPCapture` | Calls to `BuildPipeline.BuildAssetBundles` generate a trace event format profiler file at `Logs/BuildAssetBundlesTEP.json`. You can use this file to get a detailed view of what steps the build performed, including steps performed in each AssetDatabase worker process. This file is overwritten for each build.  
  
You can view the Trace Event Format file with the `chrome://tracing` tool in Google Chrome or another Chromium-based browser.  
`BuildPipelineWriteDebugFiles` | For multi-process AssetBundle builds only. Enable to write extra JSON format files into the `Temp/BuildInstructions` folder. These files are useful for testing and debugging purposes, but aren’t required or consumed by the build itself. When sending bug reports to Unity, it might be useful to provide these files, especially if it’s impossible to submit the full project.  
## Additional resources
  * [Importing assets simultaneously](https://docs.unity3d.com/6000.0/Documentation/Manual/ParallelImport.html)
  * [Build assets into an AssetBundle](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetBundles-Building.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetBundles-Building.html)
Build assets into an AssetBundle
[](https://docs.unity3d.com/6000.0/Documentation/Manual/assetbundles-compression-format.html)
AssetBundle compression formats
