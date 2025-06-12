* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.ValidateMoveAsset.html

#  [AssetDatabase](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.html).ValidateMoveAsset
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
public static string ValidateMoveAsset(string oldPath, string newPath); 
### Parameters
Parameter | Description  
---|---  
oldPath | The path where the asset currently resides.  
newPath | The path which the asset should be moved to.  
### Returns
**string** An empty string if the asset can be moved, otherwise an error message. 
### Description
Checks if an asset file can be moved from one folder to another. (Without actually moving the file).
All paths are relative to the project folder, for example: "Assets/MyTextures/hello.png".  
  
Additional resources: [AssetDatabase.MoveAsset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.MoveAsset.html).
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;  
  
public class AssetDatabaseExamples : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("AssetDatabase[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.html)/Move With Validate")]
    public static void MoveWithValidate()
    {
        for (var i = 0; i < 5; i++)
        {
            var oldPath = $"Assets/Textures/Building/BuildingTexture{i}.png";
            var newPath = $"Assets/Textures/Construction/BuildingTexture{i}.png";
            var moveResult = AssetDatabase.ValidateMoveAsset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.ValidateMoveAsset.html)(oldPath, newPath);  
  
            if (moveResult == "")
                AssetDatabase.MoveAsset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.MoveAsset.html)(oldPath, newPath);
            else
                Debug.LogError[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.LogError.html)($"Couldn't move {oldPath} because {moveResult}");
        }
    }
}
```

* * *
