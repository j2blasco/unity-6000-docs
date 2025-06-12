* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderUtil.RegisterShader.html

#  [ShaderUtil](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderUtil.html).RegisterShader
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
public static void RegisterShader([Shader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.html) shader); 
### Description
Register a user created shader.
Register a [Shader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.html) created with ShaderUtil.CreateShaderAsset with Unity. This is required if you wish your shader to exist when calling [Shader.Find](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.Find.html) and the material inspector shader menu.
* * *
