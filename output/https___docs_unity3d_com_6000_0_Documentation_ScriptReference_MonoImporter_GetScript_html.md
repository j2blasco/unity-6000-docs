* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoImporter.GetScript.html

#  [MonoImporter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoImporter.html).GetScript
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
public [MonoScript](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoScript.html) GetScript(); 
### Returns
**MonoScript** Returns the imported script. 
### Description
Gets the imported [MonoScript](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoScript.html). If the imported C# file contains multiple classes, the first is returned.
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
class Example
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/Output the Name of an Imported MonoScript[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoScript.html)")]
    public static void OutputTheNameOfAnImportedMonoScript()
    {
        var assetPath = "Assets/MyMonoBehaviour.cs";
        var monoImporter = AssetImporter.GetAtPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporter.GetAtPath.html)(assetPath) as MonoImporter[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoImporter.html);  
  
        var monoScript = monoImporter.GetScript();
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)($"{assetPath} contains {monoScript.GetClass().FullName}");
    }
}

```

* * *
