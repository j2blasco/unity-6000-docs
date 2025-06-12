* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RayTracingShader.SetMatrix.html

#  [RayTracingShader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RayTracingShader.html).SetMatrix
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
public void SetMatrix(string name, [Matrix4x4](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.html) val); 
## Declaration
public void SetMatrix(int nameID, [Matrix4x4](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.html) val); 
### Parameters
Parameter | Description  
---|---  
name | The name of the property being set.  
nameID | The ID of the property as given by Shader.PropertyToID.  
val | The matrix to set.  
### Description
Sets the value of a matrix uniform.
Only shaders defined in the .raytrace file can access the matrix you designate as the argument for this method. To make this matrix accessible to all ray tracing shader types (closest hit, any hit, miss, etc.), call the [Shader.SetGlobalMatrix](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.SetGlobalMatrix.html) method instead.
* * *
