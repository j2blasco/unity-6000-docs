* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.LoadAllAssetRepresentationsAtPath.html

#  [AssetDatabase](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.html).LoadAllAssetRepresentationsAtPath
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
public static Object[] LoadAllAssetRepresentationsAtPath(string assetPath); 
### Description
Returns all sub Assets at `assetPath`.
This function only returns sub Assets that are visible in the Project view.  
All paths are relative to the project folder, for example: "Assets/MyTextures/hello.png"  
  
**Note** : Sub Assets can be added explicitly via [AssetDatabase.AddObjectToAsset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.AddObjectToAsset.html)  
Additional resources: [AssetDatabase.LoadMainAssetAtPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.LoadMainAssetAtPath.html), [AssetDatabase.LoadAllAssetsAtPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.LoadAllAssetsAtPath.html), [HideFlags.HideInHierarchy](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HideFlags.HideInHierarchy.html).
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("AssetDatabase[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.html)/LoadAllAssetRepresentationsAtPath")]
    private static void PrintSubAssets()
    {
        Object[] data = AssetDatabase.LoadAllAssetRepresentationsAtPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.LoadAllAssetRepresentationsAtPath.html)("Assets/MySpriteTexture.png");  
  
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(data.Length + " Sub Assets");  
  
        foreach (Object o in data)
        {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(o);
        }  
  
        // outputs:
        //  4 Sub Assets
        //  MyTexture_0 (UnityEngine.Sprite)
        //  MyTexture_1 (UnityEngine.Sprite)
        //  MyTexture_2 (UnityEngine.Sprite)
        //  MyTexture_3 (UnityEngine.Sprite)
    }
}

```

* * *
