* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.LoadAssetAtPath.html

#  [AssetDatabase](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.html).LoadAssetAtPath
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
public static Object LoadAssetAtPath(string assetPath, Type type); 
### Parameters
Parameter | Description  
---|---  
assetPath | Path of the asset to load.  
type | Data type of the asset.  
### Returns
**Object** The asset matching the parameters. 
### Description
Returns the first asset object of type **type** at given path **assetPath**.
Some asset files may contain multiple objects. (such as a Maya file which may contain multiple Meshes and GameObjects). All paths are relative to the project folder, for example: "Assets/MyTextures/hello.png".  
  
**Note:**  
The **assetPath** parameter is not case sensitive.  
**ALL** asset names and paths in Unity use forward slashes, even on Windows.  
This returns only an asset object that is visible in the Project view. If the asset is not found `LoadAssetAtPath` returns Null.
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
public class MyPlayer : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("AssetDatabase[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.html)/LoadAssetExample")]
    static void ImportExample()
    {
        Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html) t = (Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html))AssetDatabase.LoadAssetAtPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.LoadAssetAtPath.html)("Assets/Textures/texture.jpg", typeof(Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html)));
    }
}

```

Additional resources: [AssetDatabase.LoadMainAssetAtPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.LoadMainAssetAtPath.html), [AssetDatabase.LoadAllAssetsAtPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.LoadAllAssetsAtPath.html).
* * *
