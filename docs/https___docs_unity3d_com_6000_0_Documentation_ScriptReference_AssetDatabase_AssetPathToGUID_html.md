* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.AssetPathToGUID.html

#  [AssetDatabase](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.html).AssetPathToGUID
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
public static string AssetPathToGUID(string path); 
## Declaration
public static string AssetPathToGUID(string path, [AssetPathToGUIDOptions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetPathToGUIDOptions.html) options = AssetPathToGUIDOptions.IncludeRecentlyDeletedAssets); 
### Parameters
Parameter | Description  
---|---  
path | Filesystem path for the asset.  
options | Specifies whether this method should return a GUID for recently deleted assets. The default value is [AssetPathToGUIDOptions.IncludeRecentlyDeletedAssets](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetPathToGUIDOptions.IncludeRecentlyDeletedAssets.html).  
### Returns
**string** GUID. 
### Description
Get the GUID for the asset at `path`.
All paths are relative to the project folder, for example: "Assets/MyTextures/hello.png".  
  
When you delete an asset, the GUID for that asset remains in Unity's asset database until you close the Editor. As a result, by default this method will still return GUIDs for assets that were deleted in the current session of the Unity Editor.  
  
For assets that do not exist, and were not deleted in the current Editor session, this method returns an empty string.  
  
If you need it to return an empty string for assets that were deleted in the current Editor session, pass the value [AssetPathToGUIDOptions.OnlyExistingAssets](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetPathToGUIDOptions.OnlyExistingAssets.html) as the "options" parameter.
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("AssetDatabase[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.html)/AssetPathToGUID")]
    static void Doit()
    {
        // texture.jpg exists or was recently deleted
        string t = AssetDatabase.AssetPathToGUID[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.AssetPathToGUID.html)("Assets/texture.jpg");
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(t); // t will be not null
    }  
  
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("AssetDatabase[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.html)/AssetPathToGUID Existing Assets Only")]
    static void DoitExistingAssetsOnly()
    {
        // texture.jpg does not exist on disk
        string t = AssetDatabase.AssetPathToGUID[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.AssetPathToGUID.html)("Assets/texture.jpg", AssetPathToGUIDOptions.OnlyExistingAssets[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetPathToGUIDOptions.OnlyExistingAssets.html));
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(t); // t will be null
    }
}

```

See [AssetDatabase.GUIDFromAssetPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GUIDFromAssetPath.html) for a version that returns a UnityEditor.GUID instead of a string.
* * *
