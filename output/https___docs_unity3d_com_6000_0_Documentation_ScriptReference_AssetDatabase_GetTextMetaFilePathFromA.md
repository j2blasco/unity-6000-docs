* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GetTextMetaFilePathFromAssetPath.html

#  [AssetDatabase](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.html).GetTextMetaFilePathFromAssetPath
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
public static string GetTextMetaFilePathFromAssetPath(string path); 
### Parameters
Parameter | Description  
---|---  
path | The path to the asset.  
### Returns
**string** The path to the .meta text file or an empty string if the file does not exist. 
### Description
Gets the path to the text .meta file associated with an asset.
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
public class AssetDatabaseExamples
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("AssetDatabase[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.html)/Get Meta file path of Animations")]
    static void GetMetaFilePathOfAllAnimations()  
  
    {
        //This will create a list of file paths of all Animation[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animation.html) assets.
        string[] animAssetsGuids = AssetDatabase.FindAssets[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.FindAssets.html)("t:Animation[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animation.html)");  
  
        foreach (var animAssetGuid in animAssetsGuids)
        {
            //This will output the path of an asset and a .meta file associated with an asset
            string animAsset = AssetDatabase.GUIDToAssetPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GUIDToAssetPath.html)(animAssetGuid);
            string metaPath = AssetDatabase.GetTextMetaFilePathFromAssetPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GetTextMetaFilePathFromAssetPath.html)(animAsset);
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Asset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Asset.html) file path: " + animAsset);
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Meta file path: " + metaPath);
        }
    }
}
```

* * *
