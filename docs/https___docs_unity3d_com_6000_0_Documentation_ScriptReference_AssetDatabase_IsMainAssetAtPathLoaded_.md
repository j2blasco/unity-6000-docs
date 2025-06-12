* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.IsMainAssetAtPathLoaded.html

#  [AssetDatabase](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.html).IsMainAssetAtPathLoaded
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
public static bool IsMainAssetAtPathLoaded(string assetPath); 
### Parameters
Parameter | Description  
---|---  
assetPath | Filesystem path of the asset to load.  
### Description
Returns true if the main asset object at `assetPath` is loaded in memory.
All paths are relative to the Project folder, for example: "Assets/MyTextures/hello.png".  
  
Additional resources: [AssetDatabase.LoadMainAssetAtPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.LoadMainAssetAtPath.html), [Resources.UnloadAsset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Resources.UnloadAsset.html), [EditorUtility.UnloadUnusedAssetsImmediate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.UnloadUnusedAssetsImmediate.html).
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;  
  
public class AssetDatabaseExamples : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("AssetDatabase[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.html)/Is Main Asset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Asset.html) At Path Loaded")]
    static void IsMainAssetAtPathLoadedExample()
    {
        //Create a material and unload it
        var materialPath = "Assets/Materials/NewMat0.mat";
        var material = new Material[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html)(Shader.Find[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.Find.html)("Standard"));
        AssetDatabase.CreateAsset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.CreateAsset.html)(material, materialPath);
        Resources.UnloadAsset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Resources.UnloadAsset.html)(material);  
  
        //This will be false
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(AssetDatabase.IsMainAssetAtPathLoaded[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.IsMainAssetAtPathLoaded.html)(materialPath));
        //Load material into memory
        AssetDatabase.LoadAssetAtPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.LoadAssetAtPath.html)(materialPath, typeof(Object));
        //This will be true
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(AssetDatabase.IsMainAssetAtPathLoaded[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.IsMainAssetAtPathLoaded.html)(materialPath));
    }
}
```

* * *
