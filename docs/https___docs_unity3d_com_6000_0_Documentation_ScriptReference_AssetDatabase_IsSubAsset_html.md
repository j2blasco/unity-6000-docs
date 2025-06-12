* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.IsSubAsset.html

#  [AssetDatabase](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.html).IsSubAsset
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
public static bool IsSubAsset([Object](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.html) obj); 
## Declaration
public static bool IsSubAsset(int instanceID); 
### Parameters
Parameter | Description  
---|---  
obj | The asset Object to query.  
instanceID | Instance ID of the asset Object to query.  
### Description
Does the asset form part of another asset?
Some assets may form part of another asset (for example, a procedural material can be part of a material package). This function tells if an asset is subordinated in this way.
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;
public class Scriptable : ScriptableObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.html)
{
}  
  
public class AssetDatabaseExamples : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("AssetDatabase[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.html)/Is Sub Asset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Asset.html) Example")]
    static void IsSubAssetExample()
    {
        var materialAsset = new Material[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html)(Shader.Find[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.Find.html)("Standard"));
        //materialAsset is still in memory, therefore this will be False
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(AssetDatabase.IsSubAsset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.IsSubAsset.html)(materialAsset));  
  
        //Create a Scriptable object
        var scriptableAssetPath = "Assets/ScriptableObjects/NewObject.asset";
        var mainAsset = ScriptableObject.CreateInstance[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.CreateInstance.html)<Scriptable>();
        AssetDatabase.CreateAsset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.CreateAsset.html)(mainAsset, scriptableAssetPath);  
  
        //Add the Material[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html) Asset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Asset.html) to the Scriptable object, so that the Material[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html) becomes a Sub Asset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Asset.html) of the Scriptable object
        AssetDatabase.AddObjectToAsset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.AddObjectToAsset.html)(materialAsset, scriptableAssetPath);
        AssetDatabase.SaveAssets[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.SaveAssets.html)();  
  
        //This will be True because the Material[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html) asset has been added to the mainAsset and is now a Sub Asset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Asset.html)
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(AssetDatabase.IsSubAsset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.IsSubAsset.html)(materialAsset));
    }
}
```

* * *
