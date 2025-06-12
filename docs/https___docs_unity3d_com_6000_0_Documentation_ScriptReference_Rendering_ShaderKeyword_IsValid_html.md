* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ShaderKeyword.IsValid.html

#  [ShaderKeyword](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ShaderKeyword.html).IsValid
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
public bool IsValid(); 
### Returns
**bool** Returns true if the global shader keyword exists. Otherwise, returns false. 
### Description
Checks whether the global shader keyword exists.
* * *
## Declaration
public bool IsValid([ComputeShader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.html) shader); 
### Parameters
Parameter | Description  
---|---  
shader | The shader that declares the keyword.  
### Returns
**bool** Returns true if the shader keyword exists. Otherwise, returns false. 
### Description
Checks whether the shader keyword exists in the compute shader you pass in.
* * *
## Declaration
public bool IsValid([Shader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.html) shader); 
### Parameters
Parameter | Description  
---|---  
shader | The shader that declares the keyword.  
### Returns
**bool** Returns true if the shader keyword exists. Otherwise, returns false. 
### Description
Checks whether the shader keyword exists in the shader you pass in.
* * *
