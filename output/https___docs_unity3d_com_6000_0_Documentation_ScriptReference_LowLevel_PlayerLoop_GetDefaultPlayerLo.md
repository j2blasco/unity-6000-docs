* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LowLevel.PlayerLoop.GetDefaultPlayerLoop.html

#  [PlayerLoop](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LowLevel.PlayerLoop.html).GetDefaultPlayerLoop
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
public static [LowLevel.PlayerLoopSystem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LowLevel.PlayerLoopSystem.html) GetDefaultPlayerLoop(); 
### Description
Returns the default update order of all engine systems in Unity.
The default update order of Unity is the order in which systems will update unless you change it with [SetPlayerLoop](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LowLevel.PlayerLoop.SetPlayerLoop.html). Use [GetCurrentPlayerLoop](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LowLevel.PlayerLoop.GetCurrentPlayerLoop.html) to append to the current update order. The player loop returned by this method can be modified to create a custom update order which you can set using [SetPlayerLoop](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LowLevel.PlayerLoop.SetPlayerLoop.html).
* * *
