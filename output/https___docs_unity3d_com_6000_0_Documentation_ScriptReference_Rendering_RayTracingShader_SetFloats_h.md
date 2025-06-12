* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RayTracingShader.SetFloats.html

#  [RayTracingShader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RayTracingShader.html).SetFloats
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
public void SetFloats(string name, params float[] values); 
## Declaration
public void SetFloats(int nameID, params float[] values); 
### Parameters
Parameter | Description  
---|---  
name | The name of the property being set.  
nameID | The ID of the property as given by Shader.PropertyToID.  
values | The float array to set.  
### Description
Sets the values for a float array uniform.
Only shaders defined in the .raytrace file can access the values you designate as the argument for this method. To make these values accessible to all ray tracing shader types (closest hit, any hit, miss, etc.), call the [Shader.SetGlobalFloatArray](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.SetGlobalFloatArray.html) method instead.
* * *
