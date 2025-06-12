* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RayTracingShader.SetAccelerationStructure.html

#  [RayTracingShader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RayTracingShader.html).SetAccelerationStructure
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
public void SetAccelerationStructure(int nameID, [Rendering.RayTracingAccelerationStructure](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RayTracingAccelerationStructure.html) accelerationStructure); 
## Declaration
public void SetAccelerationStructure(string name, [Rendering.RayTracingAccelerationStructure](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RayTracingAccelerationStructure.html) accelerationStructure); 
### Parameters
Parameter | Description  
---|---  
name | The name of the [RayTracingAccelerationStructure](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RayTracingAccelerationStructure.html) being set.  
nameID | The ID of the [RayTracingAccelerationStructure](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RayTracingAccelerationStructure.html) as given by Shader.PropertyToID.  
accelerationStructure | The value to set the [RayTracingAccelerationStructure](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RayTracingAccelerationStructure.html) to.  
### Description
Sets the value for [RayTracingAccelerationStructure](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RayTracingAccelerationStructure.html) property of this [RayTracingShader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RayTracingShader.html).
The RayTracingAccelerationStructure you specify as an argument is globally visible in all ray tracing shader types (e.g. closest hit, any hit, miss, etc.).
* * *
