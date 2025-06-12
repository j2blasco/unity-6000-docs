* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Reporting.CommonRoles.html

# CommonRoles
class in UnityEditor.Build.Reporting
Leave feedback
Suggest a change
## Success!
Thank you for helping us improve the quality of Unity Documentation. Although we cannot accept all submissions, we do read each suggested change from our users and will make updates where applicable.
Close
## Submission failed
For some reason your suggested change could not be submitted. Please <a>try again</a> in a few minutes. And thank you for taking the time to help us improve the quality of Unity Documentation.
Close
Your name Your email Suggestion* Submit suggestion
Cancel
### Description
This class provides constant values for some of the common roles used by files in the build. The role of each file in the build is available in [BuildFile.role](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Reporting.BuildFile-role.html).
### Static Properties
Property | Description  
---|---  
[appInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Reporting.CommonRoles-appInfo.html) | The BuildFile.role value of the file that provides config information used in Low Integrity mode on Windows.  
[assetBundle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Reporting.CommonRoles-assetBundle.html) | The BuildFile.role value of built AssetBundle files.  
[assetBundleTextManifest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Reporting.CommonRoles-assetBundleTextManifest.html) | The BuildFile.role value of an AssetBundle manifest file, produced during the build process, that contains information about the bundle and its dependencies.  
[bootConfig](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Reporting.CommonRoles-bootConfig.html) | The BuildFile.role value of the file that contains configuration information for the very early stages of engine startup.  
[builtInResources](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Reporting.CommonRoles-builtInResources.html) | The BuildFile.role value of the file that contains built-in resources for the engine.  
[builtInShaders](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Reporting.CommonRoles-builtInShaders.html) | The BuildFile.role value of the file that contains Unity's built-in shaders, such as the Standard shader.  
[crashHandler](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Reporting.CommonRoles-crashHandler.html) | The BuildFile.role value of the executable that is used to capture crashes from the player.  
[debugInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Reporting.CommonRoles-debugInfo.html) | The BuildFile.role value of files that contain information for debuggers.  
[dependentManagedLibrary](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Reporting.CommonRoles-dependentManagedLibrary.html) | The BuildFile.role value of a managed library that is present in the build due to being a dependency of a CommonRoles.managedLibrary.  
[engineLibrary](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Reporting.CommonRoles-engineLibrary.html) | The BuildFile.role value of the main Unity runtime when it is built as a separate library.  
[executable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Reporting.CommonRoles-executable.html) | The BuildFile.role value of an executable - the file that will actually be launched on the target device.  
[globalGameManagers](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Reporting.CommonRoles-globalGameManagers.html) | The BuildFile.role value of the file that contains global Project Settings data for the player.  
[managedEngineApi](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Reporting.CommonRoles-managedEngineApi.html) | The BuildFile.role value of files that provide the managed API for Unity.  
[managedLibrary](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Reporting.CommonRoles-managedLibrary.html) | The BuildFile.role value of a managed assembly, containing compiled script code.  
[manifestAssetBundle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Reporting.CommonRoles-manifestAssetBundle.html) | The BuildFile.role value of a manifest AssetBundle, which is an AssetBundle that contains information about other AssetBundles and their dependencies.  
[monoConfig](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Reporting.CommonRoles-monoConfig.html) | The BuildFile.role value of files that are used as configuration data by the Mono runtime.  
[monoRuntime](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Reporting.CommonRoles-monoRuntime.html) | The BuildFile.role value of files that make up the Mono runtime itself.  
[resourcesFile](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Reporting.CommonRoles-resourcesFile.html) | The BuildFile.role value of the file that contains the contents of the project's "Resources" folder, packed into a single file.  
[scene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Reporting.CommonRoles-scene.html) | The BuildFile.role value of a file that contains the packed content of a Scene.  
[sharedAssets](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Reporting.CommonRoles-sharedAssets.html) | The BuildFile.role value of a file that contains asset objects which are shared between Scenes. Examples of asset objects are textures, models, and audio.  
[streamingAsset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Reporting.CommonRoles-streamingAsset.html) | The BuildFile.role value of files that have been copied into the build without modification from the StreamingAssets folder in the project.  
[streamingResourceFile](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Reporting.CommonRoles-streamingResourceFile.html) | The BuildFile.role value of a file that contains streaming resource data.  
* * *
