* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GUIDFromAssetPath.html

#  [AssetDatabase](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.html).GUIDFromAssetPath
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
public static GUID GUIDFromAssetPath(string path); 
### Parameters
Parameter | Description  
---|---  
path | Filesystem path for the asset. All paths are relative to the project folder.  
### Returns
**GUID** The GUID of the asset. An all-zero GUID denotes an invalid asset path. 
### Description
Get the GUID for the asset at `path`.
All paths are relative to the project folder, for example: "Assets/MyTextures/hello.png".
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
public static class Example
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("AssetDatabase[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.html)/GUIDFromAssetPath")]
    static void Doit()
    {
        GUID t = AssetDatabase.GUIDFromAssetPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GUIDFromAssetPath.html)("Assets/texture.jpg");
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(t.ToString());
    }
}
```

* * *
