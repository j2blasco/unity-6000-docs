* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderUtil.GetPassKeywords.html

#  [ShaderUtil](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderUtil.html).GetPassKeywords(Shader,Rendering.PassIdentifier)
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
### Parameters
Parameter | Description  
---|---  
s | The shader the Pass belongs to.  
passIdentifier | The identifier of a Pass within the given shader.  
### Returns
**void** Returns an array of LocalKeywords that are valid for the Pass you identify. If the [PassIdentifier](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.PassIdentifier.html) you use is invalid, this function returns an empty array and Unity displays an error in the Console window. 
### Description
Gets the local shader keywords that are valid for a Pass within a particular shader.
Additional resources: [Pass](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-Pass.html).
* * *
### Parameters
Parameter | Description  
---|---  
s | The shader the Pass belongs to.  
passIdentifier | The identifier of a Pass within the given shader.  
shaderType | The shader stage of the given Pass.  
### Returns
**void** Returns an array of LocalKeywords that are valid for the given [shader stage](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ShaderType.html) of the Pass you identify. If the [PassIdentifier](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.PassIdentifier.html) you use is invalid, this function returns an empty array and Unity displays an error in the Console window. If the shader stage doesn't exist in the pass, this function returns an empty array. 
### Description
Gets the local shader keywords that are valid for a specified shader stage of a Pass within a particular shader.
Additional resources: [Pass](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-Pass.html), [ShaderType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ShaderType.html).
* * *
