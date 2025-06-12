* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GetAssetPathsFromAssetBundleAndAssetName.html

#  [AssetDatabase](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.html).GetAssetPathsFromAssetBundleAndAssetName
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
## Declaration
public static string[] GetAssetPathsFromAssetBundleAndAssetName(string assetBundleName, string assetName); 
### Description
Get the Asset paths for all Assets tagged with assetBundleName and named assetName.
Get the Asset paths for all Assets tagged with assetBundleName and named assetName, regardless of extension or path e.g. "Assets/House.prefab", "Assets/Textures/House.png" and "Assets/Data/House.xml" when assetName is "House". 
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;  
  
public class ExampleScript
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("AssetDatabase[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.html)/Display[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Display.html) assets in an AssetBundle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundle.html)")]
    static void ExampleScriptCode1()
    {
        string[] assetPaths = AssetDatabase.GetAssetPathsFromAssetBundleAndAssetName[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GetAssetPathsFromAssetBundleAndAssetName.html)("assetname", "House");
        foreach (var assetPath in assetPaths)
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(assetPath);
    }  
  
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("AssetDatabase[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.html)/AssetBundle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundle.html) creation")]
    static void ExampleScriptCode2()
    {
        BuildPipeline.BuildAssetBundles[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildPipeline.BuildAssetBundles.html)("Assets/AssetBundles", BuildAssetBundleOptions.None[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildAssetBundleOptions.None.html), BuildTarget.StandaloneOSX[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildTarget.StandaloneOSX.html));
    }
}

```

* * *
