* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GUIDToAssetPath.html

#  [AssetDatabase](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.html).GUIDToAssetPath
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
public static string GUIDToAssetPath(string guid); 
## Declaration
public static string GUIDToAssetPath(GUID guid); 
### Parameters
Parameter | Description  
---|---  
guid | The GUID of an asset.  
### Returns
**string** Path of the asset relative to the project folder. 
### Description
Gets the corresponding asset path for the supplied GUID, or an empty string if the GUID can't be found.
Returned paths are relative to the project folder, for example: "Assets/MyTextures/hello.png".
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;  
  
public class GUIDToAssetPathExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("APIExamples/GUIDToAssetPath")]
    static void MaterialPathsInProject()
    {
        var allMaterials = AssetDatabase.FindAssets[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.FindAssets.html)("t: Material[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html)");  
  
        foreach (var guid in allMaterials)
        {
            var path = AssetDatabase.GUIDToAssetPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GUIDToAssetPath.html)(guid);
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(path);
        }
    }
}

```

See [AssetDatabase.AssetPathToGUID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.AssetPathToGUID.html) for a version that returns a string instead of a UnityEditor.GUID.
* * *
