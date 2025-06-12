* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.RemoveObjectFromAsset.html

#  [AssetDatabase](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.html).RemoveObjectFromAsset
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
public static void RemoveObjectFromAsset([Object](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.html) objectToRemove); 
### Description
Removes object from its asset (Additional resources: [AssetDatabase.AddObjectToAsset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.AddObjectToAsset.html)).
```
using System.Collections.Generic;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;  
  
public class Scriptable : ScriptableObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.html)
{
}
public class AssetDatabaseExamples : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("AssetDatabase[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.html)/Remove Object From Asset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Asset.html) Example")]
    public static void RemoveObjectFromAssetExample()
    {
        var scriptableObjectList = new List<Scriptable>();  
  
        //Create Scriptable Objects and store them in a List
        for (var i = 0; i < 10; i++)
        {
            scriptableObjectList.Add(ScriptableObject.CreateInstance[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.CreateInstance.html)<Scriptable>());
            AssetDatabase.CreateAsset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.CreateAsset.html)(scriptableObjectList[i], $"Assets/ScriptableObjects/SO{i}.asset");
        }  
  
        //Add Materials as Sub Assets to the Scriptable Objects
        foreach (var so in scriptableObjectList)
        {
            AssetDatabase.AddObjectToAsset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.AddObjectToAsset.html)(new Material[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html)(Shader.Find[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.Find.html)("Standard")), so);
        }
        AssetDatabase.SaveAssets[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.SaveAssets.html)();  
  
        //Remove Materials from their Scriptable Objects
        foreach (var so in scriptableObjectList)
        {
            var material =
                AssetDatabase.LoadAssetAtPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.LoadAssetAtPath.html)(AssetDatabase.GetAssetPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GetAssetPath.html)(so), typeof(Material[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html)));
            AssetDatabase.RemoveObjectFromAsset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.RemoveObjectFromAsset.html)(material);
        }
        AssetDatabase.SaveAssets[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.SaveAssets.html)();
    }
}

```

* * *
