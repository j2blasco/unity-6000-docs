* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GetAssetPath.html

#  [AssetDatabase](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.html).GetAssetPath
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
public static string GetAssetPath(int instanceID); 
## Declaration
public static string GetAssetPath([Object](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.html) assetObject); 
### Parameters
Parameter | Description  
---|---  
instanceID | The instance ID of the asset.  
assetObject | A reference to the asset.  
### Returns
**string** The asset path name, or null, or an empty string if the asset does not exist. 
### Description
Returns the path name relative to the project folder where the asset is stored.
All paths are relative to the project folder, for example: "Assets/MyTextures/hello.png".
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
public class CreateMaterialExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)/Create Material[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html)")]
    static void CreateMaterial()
    {
        // Create a simple material asset  
  
        Material[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html) material = new Material[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html)(Shader.Find[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.Find.html)("Specular"));
        AssetDatabase.CreateAsset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.CreateAsset.html)(material, "Assets/MyMaterial.mat");  
  
        // Print the path of the created asset
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(AssetDatabase.GetAssetPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GetAssetPath.html)(material));
    }
}

```

* * *
