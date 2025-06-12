* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.html

# ComputeShader
class in UnityEngine
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ComputeShader.html "Go to ComputeShader Component in the Manual")
### Description
Compute Shader asset.
Compute shaders are programs that run on the GPU outside of the normal rendering pipeline. They correspond to compute shader assets in the project (.compute files).  
  
Compute shader support can be queried runtime using [SystemInfo.supportsComputeShaders](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-supportsComputeShaders.html). See [Compute Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ComputeShader.html) overview for more info about platforms supporting compute shaders.  
  
Additional resources: [ComputeBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeBuffer.html) class, [Compute Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ComputeShader.html) overview.
### Properties
Property | Description  
---|---  
[enabledKeywords](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader-enabledKeywords.html) | An array containing the local shader keywords that are currently enabled for this compute shader.  
[keywordSpace](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader-keywordSpace.html) | The local keyword space of this compute shader.  
[shaderKeywords](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader-shaderKeywords.html) | An array containing names of the local shader keywords that are currently enabled for this compute shader.  
### Public Methods
Method | Description  
---|---  
[DisableKeyword](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.DisableKeyword.html) | Disables a local shader keyword for this compute shader.  
[Dispatch](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.Dispatch.html) | Execute a compute shader.  
[DispatchIndirect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.DispatchIndirect.html) | Execute a compute shader.  
[EnableKeyword](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.EnableKeyword.html) | Enables a local shader keyword for this compute shader.  
[FindKernel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.FindKernel.html) | Find ComputeShader kernel index.  
[GetKernelThreadGroupSizes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.GetKernelThreadGroupSizes.html) | Get kernel thread group sizes.  
[HasKernel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.HasKernel.html) | Checks whether a shader contains a given kernel.  
[IsKeywordEnabled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.IsKeywordEnabled.html) | Checks whether a local shader keyword is enabled for this compute shader.  
[IsSupported](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.IsSupported.html) | Allows you to check whether the current end user device supports the features required to run the specified compute shader kernel.  
[SetBool](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.SetBool.html) | Set a bool parameter.  
[SetBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.SetBuffer.html) | Sets an input or output compute buffer.  
[SetConstantBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.SetConstantBuffer.html) | Sets a ComputeBuffer or GraphicsBuffer as a named constant buffer for the ComputeShader.  
[SetFloat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.SetFloat.html) | Set a float parameter.  
[SetFloats](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.SetFloats.html) | Set multiple consecutive float parameters at once.  
[SetInt](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.SetInt.html) | Set an integer parameter.  
[SetInts](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.SetInts.html) | Set multiple consecutive integer parameters at once.  
[SetKeyword](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.SetKeyword.html) | Sets the state of a local shader keyword for this compute shader.  
[SetMatrix](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.SetMatrix.html) | Set a Matrix parameter.  
[SetMatrixArray](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.SetMatrixArray.html) | Set a Matrix array parameter.  
[SetRayTracingAccelerationStructure](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.SetRayTracingAccelerationStructure.html) | Sets a RayTracingAccelerationStructure to be used for Inline Ray Tracing (Ray Queries).  
[SetTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.SetTexture.html) | Set a texture parameter.  
[SetTextureFromGlobal](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.SetTextureFromGlobal.html) | Set a texture parameter from a global texture property.  
[SetVector](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.SetVector.html) | Set a vector parameter.  
[SetVectorArray](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.SetVectorArray.html) | Set a vector array parameter.  
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
