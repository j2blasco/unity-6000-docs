* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.DeleteAsset.html

#  [AssetDatabase](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.html).DeleteAsset
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
public static bool DeleteAsset(string path); 
### Parameters
Parameter | Description  
---|---  
path | Project relative path of the asset or folder to be deleted.  
### Returns
**bool** Returns true if the asset has been successfully removed, false if it doesn't exist or couldn't be removed. 
### Description
Deletes the specified asset or folder.
Paths should be relative to the project folder, for example: "Assets/MyTextures/hello.png"  
  
Additional resources: [AssetDatabase.DeleteAssets](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.DeleteAssets.html), [AssetDatabase.MoveAssetToTrash](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.MoveAssetToTrash.html), [AssetDatabase.MoveAssetsToTrash](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.MoveAssetsToTrash.html).
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
public class AssetDatabaseExamples : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("AssetDatabase[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.html)/Delete Files In 'Unused' Folder[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WSA.Folder.html)")]
    static void DeleteAllFilesInFolder()
    {
        //"Assets/Unused" folder should exist before running this Method
        string[] unusedFolder = { "Assets/Unused" };
        foreach (var asset in AssetDatabase.FindAssets[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.FindAssets.html)("", unusedFolder))
        {
            var path = AssetDatabase.GUIDToAssetPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GUIDToAssetPath.html)(asset);
            AssetDatabase.DeleteAsset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.DeleteAsset.html)(path);
        }
    }
}
```

* * *
