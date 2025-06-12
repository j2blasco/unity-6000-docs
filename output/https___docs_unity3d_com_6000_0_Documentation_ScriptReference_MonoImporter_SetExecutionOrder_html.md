* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoImporter.SetExecutionOrder.html

#  [MonoImporter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoImporter.html).SetExecutionOrder
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
public static void SetExecutionOrder([MonoScript](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoScript.html) script, int order); 
### Parameters
Parameter | Description  
---|---  
script | The script to set the execution order for.  
order | The execution order for the given [MonoScript](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoScript.html).  
### Description
Sets the execution order for a [MonoScript](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoScript.html). This method forces Unity to reimport the [MonoImporter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoImporter.html) for the target script.
This is the same execution order that the [Script Execution Order Settings](https://docs.unity3d.com/6000.0/Documentation/Manual/class-MonoManager.html) window displays.  
  
The default execution order for scripts is 0.  
  
Additional resources: [MonoImporter.GetExecutionOrder](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoImporter.GetExecutionOrder.html).
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
class Example
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/Set Execution Order for a Script")]
    public static void SetExecutionOrderForAScript()
    {
        var assetPath = "Assets/MyMonoBehaviour.cs";
        var monoImporter = AssetImporter.GetAtPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporter.GetAtPath.html)(assetPath) as MonoImporter[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoImporter.html);  
  
        MonoImporter.SetExecutionOrder[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoImporter.SetExecutionOrder.html)(monoImporter.GetScript(), 100);
    }
}

```

* * *
