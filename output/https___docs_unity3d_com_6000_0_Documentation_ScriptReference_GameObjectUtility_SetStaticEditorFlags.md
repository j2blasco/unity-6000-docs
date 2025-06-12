* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObjectUtility.SetStaticEditorFlags.html

#  [GameObjectUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObjectUtility.html).SetStaticEditorFlags
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
public static void SetStaticEditorFlags([GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) go, [StaticEditorFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/StaticEditorFlags.html) flags); 
### Parameters
Parameter | Description  
---|---  
go | The GameObject whose Static Editor Flags you want to set.  
flags | The StaticEditorFlags to set on the GameObject.  
### Description
Sets the StaticEditorFlags of the specified GameObject.
[StaticEditorFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/StaticEditorFlags.html) determine which Unity systems consider a GameObject as static, and include the GameObject in their precomputations in the Unity Editor. Setting StaticEditorFlags at runtime has no effect on these systems.  
  
For more information, see the [ Unity Manual documentation on Static Editor Flags](https://docs.unity3d.com/6000.0/Documentation/Manual/StaticObjects.html).  
  
The code in this example enables the **Occludee Static** and **Occluder Static** StaticEditorFlags for a GameObject:
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
public class StaticEditorFlagsExample
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/Create GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) and set Static Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html) Flags[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.IO.LowLevel.Unsafe.AsyncReadManagerMetrics.Flags.html)")]
    static void CreateGameObjectAndSetStaticEditorFlags()
    {
        // Create a GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)
        var go = new GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)("Example");
        // Set the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)'s StaticEditorFlags[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/StaticEditorFlags.html)
        var flags = StaticEditorFlags.OccluderStatic[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/StaticEditorFlags.OccluderStatic.html) | StaticEditorFlags.OccludeeStatic[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/StaticEditorFlags.OccludeeStatic.html);
        GameObjectUtility.SetStaticEditorFlags[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObjectUtility.SetStaticEditorFlags.html)(go, flags);
    }
}

```

Additional resources: [StaticEditorFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/StaticEditorFlags.html), [GameObject.isStatic](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject-isStatic.html)
* * *
