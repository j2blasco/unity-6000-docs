* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RayTracingShader.html

# RayTracingShader
class in UnityEngine.Rendering
/
Inherits from:[Object](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.html)
/
Implemented in:[UnityEngine.CoreModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.CoreModule.html)
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
### Description
A shader for GPU ray tracing.
This shader should contain at least a `raygeneration` shader.
### Properties
Property | Description  
---|---  
[maxRecursionDepth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RayTracingShader-maxRecursionDepth.html) | The maximum number of ray bounces this shader can trace (Read Only).  
### Public Methods
Method | Description  
---|---  
[Dispatch](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RayTracingShader.Dispatch.html) | Dispatches this RayTracingShader.  
[DispatchIndirect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RayTracingShader.DispatchIndirect.html) | Dispatches this RayTracingShader.  
[SetAccelerationStructure](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RayTracingShader.SetAccelerationStructure.html) | Sets the value for RayTracingAccelerationStructure property of this RayTracingShader.  
[SetBool](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RayTracingShader.SetBool.html) | Sets the value of a boolean uniform.  
[SetBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RayTracingShader.SetBuffer.html) | Binds an input or output compute buffer.  
[SetConstantBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RayTracingShader.SetConstantBuffer.html) | Binds a constant buffer created through a ComputeBuffer or a GraphicsBuffer.  
[SetFloat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RayTracingShader.SetFloat.html) | Sets the value of a float uniform.  
[SetFloats](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RayTracingShader.SetFloats.html) | Sets the values for a float array uniform.  
[SetInt](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RayTracingShader.SetInt.html) | Sets the value of a int uniform.  
[SetInts](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RayTracingShader.SetInts.html) | Sets the values for a int array uniform.  
[SetMatrix](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RayTracingShader.SetMatrix.html) | Sets the value of a matrix uniform.  
[SetMatrixArray](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RayTracingShader.SetMatrixArray.html) | Sets a matrix array uniform.  
[SetShaderPass](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RayTracingShader.SetShaderPass.html) | Selects which Shader Pass to use when executing ray/geometry intersection shaders.  
[SetTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RayTracingShader.SetTexture.html) | Binds a texture resource. This can be a input or an output texture (UAV).  
[SetTextureFromGlobal](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RayTracingShader.SetTextureFromGlobal.html) | Binds a global texture to a RayTracingShader.  
[SetVector](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RayTracingShader.SetVector.html) | Sets the value for a vector uniform.  
[SetVectorArray](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RayTracingShader.SetVectorArray.html) | Sets a vector array uniform.  
### Inherited Members
### Properties
Property | Description  
---|---  
[hideFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-hideFlags.html) | Should the object be hidden, saved with the Scene or modifiable by the user?  
[name](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-name.html) | The name of the object.  
### Public Methods
Method | Description  
---|---  
[GetInstanceID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.GetInstanceID.html) | Gets the instance ID of the object.  
[ToString](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.ToString.html) | Returns the name of the object.  
### Static Methods
Method | Description  
---|---  
[Destroy](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.Destroy.html) | Removes a GameObject, component or asset.  
[DestroyImmediate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.DestroyImmediate.html) | Destroys the object obj immediately. You are strongly recommended to use Destroy instead.  
[DontDestroyOnLoad](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.DontDestroyOnLoad.html) | Do not destroy the target Object when loading a new Scene.  
[FindAnyObjectByType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.FindAnyObjectByType.html) | Retrieves any active loaded object of Type type.  
[FindFirstObjectByType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.FindFirstObjectByType.html) | Retrieves the first active loaded object of Type type.  
[FindObjectsByType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.FindObjectsByType.html) | Retrieves a list of all loaded objects of Type type.  
[Instantiate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.Instantiate.html) | Clones the object original and returns the clone.  
[InstantiateAsync](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.InstantiateAsync.html) | Captures a snapshot of the original object (that must be related to some GameObject) and returns the AsyncInstantiateOperation.  
### Operators
Operator | Description  
---|---  
[bool](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-operator_Object.html) | Does the object exist?  
[operator !=](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-operator_ne.html) | Compares if two objects refer to a different object.  
[operator ==](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-operator_eq.html) | Compares two object references to see if they refer to the same object.  
* * *
