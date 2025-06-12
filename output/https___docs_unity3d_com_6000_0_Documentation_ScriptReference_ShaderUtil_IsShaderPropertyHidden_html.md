* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderUtil.IsShaderPropertyHidden.html

#  [ShaderUtil](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderUtil.html).IsShaderPropertyHidden
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
public static bool IsShaderPropertyHidden([Shader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.html) s, int propertyIdx); 
### Parameters
Parameter | Description  
---|---  
s | The shader to check against.  
propertyIdx | The property index to use.  
### Description
Returns true if the shader propery at index `propertyIdx` is hidden with the `[HideInInspector]` attribute in the shader code.
* * *
