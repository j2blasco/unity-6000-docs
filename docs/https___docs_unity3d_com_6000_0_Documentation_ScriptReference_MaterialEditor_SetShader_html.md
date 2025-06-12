* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialEditor.SetShader.html

#  [MaterialEditor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialEditor.html).SetShader
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
public void SetShader([Shader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.html) shader); 
## Declaration
public void SetShader([Shader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.html) newShader, bool registerUndo); 
### Parameters
Parameter | Description  
---|---  
shader | Shader to set.  
registerUndo | Should undo be registered.  
### Description
Set the shader of the material.
Automatically handles internal inspector rebuilding.
* * *
