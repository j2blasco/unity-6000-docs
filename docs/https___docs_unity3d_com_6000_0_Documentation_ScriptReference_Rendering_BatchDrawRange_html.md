* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchDrawRange.html

# BatchDrawRange
struct in UnityEngine.Rendering
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
Specifies a draw range of [draw commands](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchFilterSettings.html).
For more information, see [BatchRendererGroup](https://docs.unity3d.com/6000.0/Documentation/Manual/batch-renderer-group.html).
### Properties
Property | Description  
---|---  
[drawCommandsBegin](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchDrawRange-drawCommandsBegin.html) | The index of the first draw command inside the BatchCullingOutput.drawCommands array that this draw range applies to.  
[drawCommandsCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchDrawRange-drawCommandsCount.html) | The number of draw commands, starting from BatchDrawRange.drawCommandsBegin, this draw range applies to.  
[drawCommandsType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchDrawRange-drawCommandsType.html) | The BatchDrawCommandType that apply to draw commands in this draw range.  
[filterSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchDrawRange-filterSettings.html) | The BatchFilterSettings that apply to draw commands in this draw range.  
* * *
