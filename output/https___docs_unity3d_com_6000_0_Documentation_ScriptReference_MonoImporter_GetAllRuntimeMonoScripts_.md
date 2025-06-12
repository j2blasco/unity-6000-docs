* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoImporter.GetAllRuntimeMonoScripts.html

#  [MonoImporter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoImporter.html).GetAllRuntimeMonoScripts
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
public static MonoScript[] GetAllRuntimeMonoScripts(); 
### Returns
**MonoScript[]** Returns an array of scripts. 
### Description
Gets an array of scripts that will be available at runtime.
Additional resources: [AssetDatabase.FindAssets](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.FindAssets.html).
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
class Example
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/Get Scripts Available at Runtime")]
    public static void GetScriptsAvailableAtRuntime()
    {
        foreach (var monoScript in MonoImporter.GetAllRuntimeMonoScripts[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoImporter.GetAllRuntimeMonoScripts.html)())
        {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)($"Class: {monoScript.GetClass()}, Name: {monoScript.name}");
        }
    }
}

```

* * *
