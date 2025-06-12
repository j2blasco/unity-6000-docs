* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.FindSubshaderTagValue.html

#  [Shader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.html).FindSubshaderTagValue
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Shader.html "Go to Shader Component in the Manual")
## Declaration
public [Rendering.ShaderTagId](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ShaderTagId.html) FindSubshaderTagValue(int subshaderIndex, [Rendering.ShaderTagId](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ShaderTagId.html) tagName); 
### Parameters
Parameter | Description  
---|---  
subshaderIndex | The index of the SubShader.  
tagName | The name of the tag.  
### Description
Searches for the tag specified by `tagName` on the SubShader specified by `subshaderIndex` and returns the value of the tag.
* * *
