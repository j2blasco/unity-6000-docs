* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.CopyAsset.html

#  [AssetDatabase](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.html).CopyAsset
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
public static bool CopyAsset(string path, string newPath); 
### Parameters
Parameter | Description  
---|---  
path | Filesystem path of the source asset.  
newPath | Filesystem path of the new asset to create.  
### Returns
**bool** Returns true if the copy operation is successful or false if part of the process fails. 
### Description
Duplicates the asset at `path` and stores it at `newPath`.
All paths are relative to the project folder, for example: "Assets/MyTextures/hello.png".
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
public class AssetDatabaseExamples : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("AssetDatabase[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.html)/Duplicate Material[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html)")]
    static void DuplicateMaterial()
    {
        const string assetPath = "Assets/Materials/CarMaterial.mat";
        for (var i = 0; i < 20; i++)
        {
            if(!AssetDatabase.CopyAsset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.CopyAsset.html)(assetPath, $"Assets/Duplicates/Materials/CarMaterial{i}.mat"))
                Debug.LogWarning[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.LogWarning.html)($"Failed to copy {assetPath}");
        }
    }
}
```

Any errors and warnings from the copy operation are reported in the log and the console.
* * *
