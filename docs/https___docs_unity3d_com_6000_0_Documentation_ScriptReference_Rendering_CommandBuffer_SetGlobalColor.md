* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.SetGlobalColor.html

#  [CommandBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.html).SetGlobalColor
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
public void SetGlobalColor(string name, [Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) value); 
## Declaration
public void SetGlobalColor(int nameID, [Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) value); 
### Description
Add a "set global shader color property" command.
When the command buffer will be executed, a global shader color property will be set at this point. The effect is as if [Shader.SetGlobalColor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.SetGlobalColor.html) was called.
* * *
