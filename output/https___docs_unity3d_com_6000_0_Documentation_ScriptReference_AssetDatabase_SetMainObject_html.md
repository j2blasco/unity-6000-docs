* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.SetMainObject.html

#  [AssetDatabase](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.html).SetMainObject
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
public static void SetMainObject([Object](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.html) mainObject, string assetPath); 
### Parameters
Parameter | Description  
---|---  
mainObject | The object to become the main object.  
assetPath | Path to the asset file.  
### Description
Specifies which object in the asset file should become the main object after the next import.
All other objects in the asset become children of the main object. NOTE: This function modifies the importer object, not the asset itself. The next import reflects the change in the imported asset.
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;  
  
public class Scriptable : ScriptableObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.html)
{
}
public class AssetDatabaseExamples : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("AssetDatabase[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.html)/Set Main Object Example")]
    public static void SetMainObjectExample()
    {
        //Create a Scriptable Object and a Material[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html)
        var materialAsset = new Material[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html)(Shader.Find[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.Find.html)("Standard"));
        var scriptableAssetPath = "Assets/ScriptableObjects/NewObject.asset";
        var mainAsset = ScriptableObject.CreateInstance[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.CreateInstance.html)<Scriptable>();
        AssetDatabase.CreateAsset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.CreateAsset.html)(mainAsset, scriptableAssetPath);  
  
        //Add the Material[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html) to the Scriptable Object
        AssetDatabase.AddObjectToAsset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.AddObjectToAsset.html)(materialAsset, scriptableAssetPath);
        AssetDatabase.SaveAssets[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.SaveAssets.html)();  
  
        //Set the Material[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html) to be the main Object and import it
        AssetDatabase.SetMainObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.SetMainObject.html)(materialAsset, scriptableAssetPath);
        AssetDatabase.ImportAsset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.ImportAsset.html)(scriptableAssetPath);
    }
}
```

* * *
