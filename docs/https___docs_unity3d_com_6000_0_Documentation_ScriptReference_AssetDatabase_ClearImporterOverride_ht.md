* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.ClearImporterOverride.html

#  [AssetDatabase](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.html).ClearImporterOverride
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
public static void ClearImporterOverride(string path); 
### Parameters
Parameter | Description  
---|---  
path | Asset path.  
### Description
Clears the importer override for the asset.
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEditor.AssetImporters;
using UnityEngine.Assertions;  
  
public class AssetDatabaseExamples : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("AssetDatabase[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.html)/Example Importer Actions")]
    static void AllImporterActions()
    {
        //This sets CubeImporter to be used for the asset
        AssetDatabase.SetImporterOverride[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.SetImporterOverride.html)<CubeImporter>("Assets/CompanionCube.cube");
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("New importer: " + AssetDatabase.GetImporterOverride[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GetImporterOverride.html)("Assets/CompanionCube.cube"));  
  
        //This clears importer override and sets it to null
        AssetDatabase.ClearImporterOverride[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.ClearImporterOverride.html)("Assets/CompanionCube.cube");
        Assert.IsNull[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Assertions.Assert.IsNull.html)(AssetDatabase.GetImporterOverride[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GetImporterOverride.html)("Assets/CompanionCube.cube"));
    }
}
```

* * *
