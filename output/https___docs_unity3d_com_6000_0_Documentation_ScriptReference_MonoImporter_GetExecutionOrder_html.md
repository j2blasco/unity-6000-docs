* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoImporter.GetExecutionOrder.html

#  [MonoImporter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoImporter.html).GetExecutionOrder
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
public static int GetExecutionOrder([MonoScript](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoScript.html) script); 
### Parameters
Parameter | Description  
---|---  
script | The script to retrieve the execution order for.  
### Returns
**int** Returns the execution order for the given [MonoScript](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoScript.html). 
### Description
Gets the execution order for a [MonoScript](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoScript.html).
This is the same execution order that the [Script Execution Order Settings](https://docs.unity3d.com/6000.0/Documentation/Manual/class-MonoManager.html) window displays.  
  
The default execution order for scripts is 0.  
  
Additional resources: [MonoImporter.SetExecutionOrder](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoImporter.SetExecutionOrder.html).
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
class Example
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/Get Execution Order for a Script")]
    public static void GetExecutionOrderForAScript()
    {
        var assetPath = "Assets/MyMonoBehaviour.cs";
        var monoImporter = AssetImporter.GetAtPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporter.GetAtPath.html)(assetPath) as MonoImporter[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoImporter.html);
        var executionOrder = MonoImporter.GetExecutionOrder[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoImporter.GetExecutionOrder.html)(monoImporter.GetScript());  
  
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)($"Execution order for {monoImporter.assetPath} is {executionOrder}");
    }
}

```

* * *
