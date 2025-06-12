* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RayTracingShader.SetVectorArray.html

#  [RayTracingShader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RayTracingShader.html).SetVectorArray
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
public void SetVectorArray(int nameID, Vector4[] values); 
## Declaration
public void SetVectorArray(string name, Vector4[] values); 
### Parameters
Parameter | Description  
---|---  
name | The name of the property being set.  
nameID | The ID of the property as given by Shader.PropertyToID.  
values | The array of vectors to set.  
### Description
Sets a vector array uniform.
Only shaders defined in the .raytrace file can access the vector array you designate as the argument for this method. To make this vector array accessible to all ray tracing shader types (closest hit, any hit, miss, etc.) call the [Shader.SetGlobalVectorArray](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.SetGlobalVectorArray.html) instead.
* * *
