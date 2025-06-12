* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ShaderKeyword-ctor.html

# ShaderKeyword Constructor
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
public ShaderKeyword(string keywordName); 
### Parameters
Parameter | Description  
---|---  
keywordName | The name of the keyword.  
### Description
Initializes a new instance of the ShaderKeyword class from a shader global keyword name.
If you call this function and a keyword with the name you pass in does not exist, Unity creates one with that name. To get all the global keywords that already exist, use [Shader.globalKeywords](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader-globalKeywords.html).  
  
Additional resources: [IPreprocessShaders.OnProcessShader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.IPreprocessShaders.OnProcessShader.html), [IPreprocessComputeShaders.OnProcessComputeShader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.IPreprocessComputeShaders.OnProcessComputeShader.html).
* * *
## Declaration
public ShaderKeyword([Shader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.html) shader, string keywordName); 
### Parameters
Parameter | Description  
---|---  
shader | The shader that declares the keyword.  
keywordName | The name of the keyword.  
### Description
Initializes a new instance of the ShaderKeyword class from a local shader keyword name.
If the shader defines a local keyword with the given name, Unity creates a valid ShaderKeyword instance that represents the local keyword. Otherwise, Unity creates an invalid ShaderKeyword instance.  
  
Additional resources: Build.IPreprocessComputeShaders.OnProcessShader, [ShaderKeyword.IsValid](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ShaderKeyword.IsValid.html).
* * *
## Declaration
public ShaderKeyword([ComputeShader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.html) shader, string keywordName); 
### Parameters
Parameter | Description  
---|---  
shader | The compute shader that declares the local keyword.  
keywordName | The name of the keyword.  
### Description
Initializes a new instance of the ShaderKeyword class from a local shader keyword name, and the compute shader that defines that local keyword.
If the compute shader defines a local keyword with the given name, Unity creates a valid ShaderKeyword instance that represents the local keyword. Otherwise, Unity creates an invalid ShaderKeyword instance.  
  
Additional resources: [IPreprocessComputeShaders.OnProcessComputeShader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.IPreprocessComputeShaders.OnProcessComputeShader.html), [ShaderKeyword.IsValid](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ShaderKeyword.IsValid.html).
* * *
