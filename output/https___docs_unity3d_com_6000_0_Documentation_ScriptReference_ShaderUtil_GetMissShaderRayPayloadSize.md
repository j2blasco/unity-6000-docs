* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderUtil.GetMissShaderRayPayloadSize.html

#  [ShaderUtil](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderUtil.html).GetMissShaderRayPayloadSize
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
public static int GetMissShaderRayPayloadSize([Rendering.RayTracingShader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RayTracingShader.html) s, int shaderIndex); 
### Parameters
Parameter | Description  
---|---  
s | The [RayTracingShader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RayTracingShader.html) instance.  
shaderIndex | The miss Shader index for which to retrieve the ray payload size.  
### Returns
**int** The ray payload size in bytes. 
### Description
Returns the ray payload size of a user-defined miss Shader from within a [RayTracingShader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RayTracingShader.html).
Additional resources: [ShaderUtil.GetMissShaderCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderUtil.GetMissShaderCount.html), [ShaderUtil.GetMissShaderName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderUtil.GetMissShaderName.html).
* * *
