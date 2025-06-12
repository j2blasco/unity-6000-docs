* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RayTracingShader.SetTexture.html

#  [RayTracingShader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RayTracingShader.html).SetTexture
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
public void SetTexture(string name, [Texture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) texture); 
## Declaration
public void SetTexture(int nameID, [Texture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) texture); 
### Parameters
Parameter | Description  
---|---  
nameID | The ID of the resource as given by Shader.PropertyToID.  
name | The name of the texture being set.  
texture | The texture to bind.  
### Description
Binds a texture resource. This can be a input or an output texture (UAV).
Only shaders defined in the .raytrace file can access the texture you designate as the argument for this method. To make this texture accessible to all ray tracing shader types (closest hit, any hit, miss, etc.), call the [Shader.SetGlobalTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.SetGlobalTexture.html) method instead.
* * *
