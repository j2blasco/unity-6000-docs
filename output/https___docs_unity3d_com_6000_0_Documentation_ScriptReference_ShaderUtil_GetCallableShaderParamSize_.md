* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderUtil.GetCallableShaderParamSize.html

#  [ShaderUtil](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderUtil.html).GetCallableShaderParamSize
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
public static int GetCallableShaderParamSize([Rendering.RayTracingShader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RayTracingShader.html) s, int shaderIndex); 
### Parameters
Parameter | Description  
---|---  
s | The [RayTracingShader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RayTracingShader.html) instance.  
shaderIndex | The callable Shader index for which to retrieve the parameter size.  
### Returns
**int** The parameter size in bytes. 
### Description
Returns the parameter size of a user-defined callable Shader from within a [RayTracingShader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RayTracingShader.html).
Additional resources: [ShaderUtil.GetCallableShaderCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderUtil.GetCallableShaderCount.html), [ShaderUtil.GetCallableShaderName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderUtil.GetCallableShaderName.html).
* * *
