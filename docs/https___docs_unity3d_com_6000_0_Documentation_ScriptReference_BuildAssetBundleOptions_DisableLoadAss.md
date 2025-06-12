* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildAssetBundleOptions.DisableLoadAssetByFileNameWithExtension.html

#  [BuildAssetBundleOptions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildAssetBundleOptions.html).DisableLoadAssetByFileNameWithExtension
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
Disables Asset Bundle LoadAsset by file name with extension.
Asset Bundles by default have three ways to look up the same asset: full asset path, asset file name, and asset file name with extension. The full path is serialized into Asset Bundles, while file name and file name with extension are generated when an Asset Bundle is loaded from file.  
  
Example: "Assets/Prefabs/Player.prefab", "Player", and "Player.prefab"  
  
This option will set a flag on Asset Bundles to prevent creating the asset file name with extension lookup. This option saves runtime memory and loading performance for asset bundles.  
  
Additional resources: BuildAssetBundleOptions.DisableFileNameLoading.
```
//Create a folder (right click in the Assets folder and go to **Create**>**Folder**), and name it “Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html)” if it doesn’t already exist
//Place this script in the Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html) folder  
  
//This script creates a new Menu[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Menu.html) named “Build Asset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Asset.html)” and new options within the menu named “Normal” and “Disable Load Asset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Asset.html) By filename with Extension”. Click these menu items to build an AssetBundle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundle.html) into a folder.  
  
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
  
    //Creates a new item (Disable Load Asset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Asset.html) By Name with Extension) in the new Build Asset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Asset.html) Bundles menu
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Build Asset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Asset.html) Bundles/Disable Load Asset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Asset.html) By Name with Extension ")]
    static void BuildABsDisable()
    {
        //Build the AssetBundles in this mode
        BuildPipeline.BuildAssetBundles[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildPipeline.BuildAssetBundles.html)("Assets/MyAssetBuilds", BuildAssetBundleOptions.DisableLoadAssetByFileNameWithExtension[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildAssetBundleOptions.DisableLoadAssetByFileNameWithExtension.html), BuildTarget.StandaloneOSX[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildTarget.StandaloneOSX.html));
    }
}

```

* * *
