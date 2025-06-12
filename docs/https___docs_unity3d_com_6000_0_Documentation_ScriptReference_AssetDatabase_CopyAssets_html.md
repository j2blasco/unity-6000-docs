* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.CopyAssets.html

#  [AssetDatabase](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.html).CopyAssets
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
public static bool CopyAssets(string[] paths, string[] newPaths); 
### Parameters
Parameter | Description  
---|---  
paths | Filesystem paths of the source assets.  
newPaths | Filesystem paths of the new assets to create.  
### Returns
**bool** Returns true if the copy operation is successful or false if part of the process fails. 
### Description
Duplicates assets in `paths` and stores them in `newPaths`.
All paths are relative to the project folder, for example: "Assets`paths`hello.png". `paths` and `newPaths` must contain the same number of items.
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
public class AssetDatabaseExamples : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("AssetDatabase[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.html)/Duplicate Materials")]
    static void DuplicateMaterials()
    {
        string[] sourcePaths = new []
        {
            "Assets/Materials/CarMaterial.mat",
            "Assets/Materials/TruckMaterial",
            "Assets/Materials/BoatMaterial"
        };
        string[] targetPaths = new []
        {
            "Assets/Duplicates/Materials/CarMaterial_Dup.mat",
            "Assets/Duplicates/Materials/TruckMaterial_Dup",
            "Assets/Duplicates/Materials/BoatMaterial_Dup"
        };
        if(!AssetDatabase.CopyAssets[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.CopyAssets.html)(sourcePaths, targetPaths))
            Debug.LogWarning[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.LogWarning.html)($"Failed to copy assets");
    }
}
```

You cannot use this function during an import (either in process or from an asset worker), as it would result in new assets created in the middle of an import. Any errors and warnings from the copy operation are reported in the log and the console.
* * *
