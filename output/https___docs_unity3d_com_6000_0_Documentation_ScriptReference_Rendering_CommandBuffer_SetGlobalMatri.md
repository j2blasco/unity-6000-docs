* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.SetGlobalMatrixArray.html

#  [CommandBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.html).SetGlobalMatrixArray
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
public void SetGlobalMatrixArray(string propertyName, Matrix4x4[] values); 
## Declaration
public void SetGlobalMatrixArray(int nameID, Matrix4x4[] values); 
## Declaration
public void SetGlobalMatrixArray(string propertyName, List<Matrix4x4> values); 
## Declaration
public void SetGlobalMatrixArray(int nameID, List<Matrix4x4> values); 
### Description
Add a "set global shader matrix array property" command.
When the command buffer will be executed, a global shader matrix array property will be set at this point. The effect is as if [Shader.SetGlobalMatrixArray](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.SetGlobalMatrixArray.html) was called.
* * *
