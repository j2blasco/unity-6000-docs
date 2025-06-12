* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LowLevel.PlayerLoopSystem.html

# PlayerLoopSystem
struct in UnityEngine.LowLevel
/
Implemented in:[UnityEngine.CoreModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.CoreModule.html)
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
### Description
The representation of a single system being updated by the player loop in Unity.
This struct represents a single system in the player loop. A system can be one of Unity's built-in native systems, or you can add new custom systems to the player loop using C#. Native systems can only be retrieved by calling [PlayerLoop.GetDefaultPlayerLoop](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LowLevel.PlayerLoop.GetDefaultPlayerLoop.html), and the parameters of them should not be modified.
### Properties
Property | Description  
---|---  
[loopConditionFunction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LowLevel.PlayerLoopSystem-loopConditionFunction.html) | The loop condition for a native engine system. To get a valid value for this, you must copy it from one of the PlayerLoopSystems returned by PlayerLoop.GetDefaultPlayerLoop.  
[subSystemList](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LowLevel.PlayerLoopSystem-subSystemList.html) | A list of sub systems which run as part of this item in the player loop.  
[type](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LowLevel.PlayerLoopSystem-type.html) | This property is used to identify which native system this belongs to, or to get the name of the managed system to show in the profiler.  
[updateDelegate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LowLevel.PlayerLoopSystem-updateDelegate.html) | A managed delegate. You can set this to create a new C# entrypoint in the player loop.  
[updateFunction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LowLevel.PlayerLoopSystem-updateFunction.html) | A native engine system. To get a valid value for this, you must copy it from one of the PlayerLoopSystems returned by PlayerLoop.GetDefaultPlayerLoop.  
* * *
