* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderUtil.PassHasKeyword.html

#  [ShaderUtil](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderUtil.html).PassHasKeyword(Shader,Rendering.PassIdentifier,Rendering.LocalKeyword)
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
keyword | The local shader keyword to check.  
### Returns
**void** Returns true if the keyword is valid for the given Pass. Otherwise, returns false. If the [PassIdentifier](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.PassIdentifier.html) you use is invalid, this function returns false and Unity displays an error in the Console window. 
### Description
Checks whether a local shader keyword is valid for a Pass within a particular shader.
Additional resources: [Pass](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-Pass.html).
* * *
### Parameters
Parameter | Description  
---|---  
s | The shader the Pass belongs to.  
passIdentifier | The identifier of a Pass within the given shader.  
keyword | The local shader keyword to check.  
shaderType | The shader stage of the given pass.  
### Returns
**void** Returns true if the keyword is valid for the given shader stage of the Pass. Otherwise, returns false. If the [PassIdentifier](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.PassIdentifier.html) you use is invalid, this function returns false and Unity displays an error in the Console window. 
### Description
Checks whether a local shader keyword is valid for a particular shader stage of a Pass within a particular shader.
Additional resources: [Pass](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-Pass.html).
* * *
### Parameters
Parameter | Description  
---|---  
s | The shader the Pass belongs to.  
passIdentifier | The identifier of a Pass within the given shader.  
keyword | The local shader keyword to check.  
shaderType | The shader stage of the given pass.  
shaderCompilerPlatform | The shader compiler platform to check against.  
### Returns
**void** Returns true if the keyword is valid for the given shader stage of the Pass for the given ShaderCompilerPlatform. Otherwise, returns false. If the [PassIdentifier](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.PassIdentifier.html) you use is invalid, this function returns false and Unity displays an error in the Console window. 
### Description
Checks whether a local shader keyword is valid for a particular shader stage of a Pass within a particular shader for the given shader compiler platform.
Some shader compiler platforms combine several shader stages in one. This method overload ensures that correct data is returned for all shader compiler platforms.  
  
Additional resources: [Pass](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-Pass.html).
* * *
