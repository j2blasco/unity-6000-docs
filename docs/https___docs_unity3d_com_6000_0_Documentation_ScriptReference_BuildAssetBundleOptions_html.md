* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildAssetBundleOptions.html

# BuildAssetBundleOptions
enumeration
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
Asset Bundle building options.
These flags allows you to configure options when calling [BuildPipeline.BuildAssetBundles](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildPipeline.BuildAssetBundles.html).  
  
Additional resources: [AssetBundle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundle.html), [BuildPipeline.BuildAssetBundles](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildPipeline.BuildAssetBundles.html)
```
//Create a folder (right click in the Assets folder and go to **Create**>**Folder**), and name it “Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html)” if it doesn’t already exist
//Place this script in the Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html) folder  
  
//This script creates a new Menu[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Menu.html) named “Build Asset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Asset.html)” and new options within the menu named “Normal” and “Strict Mode[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.PrefabStage.Mode.html)”. Click these menu items to build an AssetBundle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundle.html) into a folder with either no extra build options, or a strict build.  
  
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
public class Example
{
    //Creates a new menu (Build Asset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Asset.html) Bundles) and item (Normal) in the Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html)
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Build Asset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Asset.html) Bundles/Normal")]
    static void BuildABsNone()
    {
        //Build AssetBundles with no special options
        //They will be written in the custom folder ("MyAssetBuilds") which needs to exist prior to this call.
        BuildPipeline.BuildAssetBundles[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildPipeline.BuildAssetBundles.html)("Assets/MyAssetBuilds", BuildAssetBundleOptions.None[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildAssetBundleOptions.None.html), BuildTarget.StandaloneOSX[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildTarget.StandaloneOSX.html));
    }  
  
    //Creates a new item (Strict Mode[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.PrefabStage.Mode.html)) in the new Build Asset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Asset.html) Bundles menu
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Build Asset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Asset.html) Bundles/Strict Mode[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.PrefabStage.Mode.html)")]
    static void BuildABsStrict()
    {
        //Build the AssetBundles in strict mode (build fails if any errors are detected)
        BuildPipeline.BuildAssetBundles[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildPipeline.BuildAssetBundles.html)("Assets/MyAssetBuilds", BuildAssetBundleOptions.StrictMode[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildAssetBundleOptions.StrictMode.html), BuildTarget.StandaloneOSX[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildTarget.StandaloneOSX.html));
    }
}

```

### Properties
Property | Description  
---|---  
[None](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildAssetBundleOptions.None.html) | Build assetBundle without any special option.  
[UncompressedAssetBundle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildAssetBundleOptions.UncompressedAssetBundle.html) | Don't compress the data when creating the AssetBundle.  
[DisableWriteTypeTree](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildAssetBundleOptions.DisableWriteTypeTree.html) | Do not include type information within the AssetBundle.  
[ForceRebuildAssetBundle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildAssetBundleOptions.ForceRebuildAssetBundle.html) | Force rebuild the assetBundles.  
[IgnoreTypeTreeChanges](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildAssetBundleOptions.IgnoreTypeTreeChanges.html) | Ignore the type tree changes when doing the incremental build check.  
[AppendHashToAssetBundleName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildAssetBundleOptions.AppendHashToAssetBundleName.html) | Append the hash to the assetBundle name.  
[ChunkBasedCompression](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildAssetBundleOptions.ChunkBasedCompression.html) | Use chunk-based LZ4 compression when creating the AssetBundle.  
[StrictMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildAssetBundleOptions.StrictMode.html) | Do not allow the build to succeed if any errors are reporting during it.  
[DryRunBuild](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildAssetBundleOptions.DryRunBuild.html) | Do a dry run build.  
[DisableLoadAssetByFileName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildAssetBundleOptions.DisableLoadAssetByFileName.html) | Disables Asset Bundle LoadAsset by file name.  
[DisableLoadAssetByFileNameWithExtension](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildAssetBundleOptions.DisableLoadAssetByFileNameWithExtension.html) | Disables Asset Bundle LoadAsset by file name with extension.  
[AssetBundleStripUnityVersion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildAssetBundleOptions.AssetBundleStripUnityVersion.html) | Removes the Unity Version number in the Archive File and Serialized File headers during the build.  
[UseContentHash](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildAssetBundleOptions.UseContentHash.html) | Use the content of the asset bundle to calculate the hash. This feature is always enabled.  
[RecurseDependencies](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildAssetBundleOptions.RecurseDependencies.html) | Use when AssetBundle dependencies need to be calculated recursively, such as when you have a dependency chain of matching typed Scriptable Objects.  
[StripUnatlasedSpriteCopies](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildAssetBundleOptions.StripUnatlasedSpriteCopies.html) | Use to prevent duplicating a texture when it is referenced in multiple bundles. This would primarily happen with particle systems. The new behavior does not duplicate the texture if the sprite does not belong to an atlas. Using this flag is the desired behavior, but is not set by default for backwards compatability reasons.  
* * *
