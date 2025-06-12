* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoImporter.SetDefaultReferences.html

#  [MonoImporter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoImporter.html).SetDefaultReferences
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
public void SetDefaultReferences(string[] name, Object[] target); 
### Parameters
Parameter | Description  
---|---  
name | An array of names of public fields in the imported [MonoScript](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoScript.html). The type of each field must be derived from UnityEngine.Object.  
target | An array of objects to use as default values. The size of the array must match the size of the names array. The array can include null values.  
### Description
Sets default references for this [MonoScript](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoScript.html).
When the Unity Editor instantiates this [MonoScript](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoScript.html), it uses the default values to populate the named fields. Additional resources: [MonoImporter.GetDefaultReference](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoImporter.GetDefaultReference.html).
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
class Example
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/Set Default References")]
    public static void SetDefaultReferences()
    {
        var assetPath = "Assets/MyMonoBehaviour.cs";
        var monoImporter = AssetImporter.GetAtPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporter.GetAtPath.html)(assetPath) as MonoImporter[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoImporter.html);  
  
        var gameObject = AssetDatabase.LoadAssetAtPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.LoadAssetAtPath.html)<GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)>(AssetDatabase.GUIDToAssetPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GUIDToAssetPath.html)(AssetDatabase.FindAssets[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.FindAssets.html)("Cube")[0]));
        var material = AssetDatabase.LoadAssetAtPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.LoadAssetAtPath.html)<Material[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html)>(AssetDatabase.GUIDToAssetPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GUIDToAssetPath.html)(AssetDatabase.FindAssets[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.FindAssets.html)("defaultMat")[0]));  
  
        var names = new string[] {"MyGameObject", "MyMaterial"};
        var values = new Object[] {gameObject, material};
        monoImporter.SetDefaultReferences(names, values);
        monoImporter.SaveAndReimport();
    }
}

```

* * *
