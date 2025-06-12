* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RayTracingShader.SetMatrixArray.html

#  [RayTracingShader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RayTracingShader.html).SetMatrixArray
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
public void SetMatrixArray(string name, Matrix4x4[] values); 
## Declaration
public void SetMatrixArray(int nameID, Matrix4x4[] values); 
### Parameters
Parameter | Description  
---|---  
name | The name of the property being set.  
nameID | The ID of the property as given by Shader.PropertyToID.  
values | The matrix array to set.  
### Description
Sets a matrix array uniform.
Only shaders defined in the .raytrace file can access the matrix array you designate as the argument for this method. To make this matrix array accessible to all ray tracing shader types (closest hit, any hit, miss, etc.), call the [Shader.SetGlobalMatrixArray](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.SetGlobalMatrixArray.html) method instead.
* * *
