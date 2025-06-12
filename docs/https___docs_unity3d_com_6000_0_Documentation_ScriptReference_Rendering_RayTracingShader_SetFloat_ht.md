* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RayTracingShader.SetFloat.html

#  [RayTracingShader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RayTracingShader.html).SetFloat
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
public void SetFloat(string name, float val); 
## Declaration
public void SetFloat(int nameID, float val); 
### Parameters
Parameter | Description  
---|---  
name | The name of the property being set.  
nameID | The ID of the property as given by Shader.PropertyToID.  
val | The float value to set.  
### Description
Sets the value of a float uniform.
Only shaders defined in the .raytrace file can access the value you designate as the argument for this method. To make this value accessible to all ray tracing shader types (closest hit, any hit, miss, etc.), call the [Shader.SetGlobalFloat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.SetGlobalFloat.html) method instead.
* * *
