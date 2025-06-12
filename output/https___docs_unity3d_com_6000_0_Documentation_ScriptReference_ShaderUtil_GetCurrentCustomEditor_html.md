* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderUtil.GetCurrentCustomEditor.html

#  [ShaderUtil](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderUtil.html).GetCurrentCustomEditor
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
public static string GetCurrentCustomEditor([Shader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.html) shader); 
### Parameters
Parameter | Description  
---|---  
shader | The shader to obtain the custom editor.  
### Returns
**string** The current custom editor full class name. 
### Description
Gets the current custom editor for the shader you pass in.  
  
Depending on the render pipeline asset assigned in your Graphics Settings, the custom editor can change if the shader has a different custom editor for one or multiple render pipeline assets.
* * *
