* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LowLevel.PlayerLoop.SetPlayerLoop.html

#  [PlayerLoop](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LowLevel.PlayerLoop.html).SetPlayerLoop
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
public static void SetPlayerLoop([LowLevel.PlayerLoopSystem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LowLevel.PlayerLoopSystem.html) loop); 
### Description
Set a new custom update order of all engine systems in Unity.
This method changes the update order of Unity to the one specified. Only the systems you include in the new player loop will run. If you omit any systems, they will not run at all. You can insert custom script entry points in the update order before setting it. For example, this allows you to add a script which runs right before physics or in other places where scripts are not run by default. The new update order will not take effect until the next full player loop iteration, but the changes will be immediately visible in subsequent calls to [GetCurrentPlayerLoop](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LowLevel.PlayerLoop.GetCurrentPlayerLoop.html).
* * *
