* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.html

# Shader
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Shader.html "Go to Shader Component in the Manual")
### Description
Shader scripts used for all rendering.
Most of the advanced rendering is controlled via [Material](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html) class. Shader class is mostly used just to check whether a shader can run on the user's hardware ([isSupported](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader-isSupported.html) property), setting up global shader properties and keywords, and finding shaders by name ([Find](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.Find.html) method).  
  
Additional resources: [Material](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html) class, [Materials](https://docs.unity3d.com/6000.0/Documentation/Manual/Materials.html), [ShaderLab documentation](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html).
### Static Properties
Property | Description  
---|---  
[enabledGlobalKeywords](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader-enabledGlobalKeywords.html) | An array containing the global shader keywords that are currently enabled.  
[globalKeywords](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader-globalKeywords.html) | An array containing the global shader keywords that currently exist. This includes enabled and disabled global shader keywords.  
[globalMaximumLOD](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader-globalMaximumLOD.html) | Shader LOD level for all shaders.  
[globalRenderPipeline](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader-globalRenderPipeline.html) | Render pipeline currently in use.  
[maximumChunksOverride](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader-maximumChunksOverride.html) | Sets the limit on the number of shader variant chunks Unity loads and keeps in memory.  
### Properties
Property | Description  
---|---  
[isSupported](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader-isSupported.html) | Can this shader run on the end-users graphics card? (Read Only)  
[keywordSpace](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader-keywordSpace.html) | The local keyword space of this shader.  
[maximumLOD](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader-maximumLOD.html) | Shader LOD level for this shader.  
[passCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader-passCount.html) | Returns the number of shader passes on the active SubShader.  
[renderQueue](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader-renderQueue.html) | Render queue of this shader. (Read Only)  
[subshaderCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader-subshaderCount.html) | Returns the number of SubShaders in this shader.  
### Public Methods
Method | Description  
---|---  
[FindPassTagValue](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.FindPassTagValue.html) | Searches for the tag specified by tagName on the shader's active SubShader and returns the value of the tag.  
[FindPropertyIndex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.FindPropertyIndex.html) | Finds the index of a shader property by its name.  
[FindSubshaderTagValue](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.FindSubshaderTagValue.html) | Searches for the tag specified by tagName on the SubShader specified by subshaderIndex and returns the value of the tag.  
[FindTextureStack](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.FindTextureStack.html) | Find the name of a texture stack a texture belongs too.  
[GetDependency](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.GetDependency.html) | Returns the dependency shader.  
[GetPassCountInSubshader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.GetPassCountInSubshader.html) | Returns the number of passes in the given SubShader.  
[GetPropertyAttributes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.GetPropertyAttributes.html) | Returns an array of strings containing attributes of the shader property at the specified index.  
[GetPropertyCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.GetPropertyCount.html) | Returns the number of properties in this Shader.  
[GetPropertyDefaultFloatValue](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.GetPropertyDefaultFloatValue.html) | Returns the default float value of the shader property at the specified index.  
[GetPropertyDefaultIntValue](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.GetPropertyDefaultIntValue.html) | Returns the default int value of the shader property at the specified index.  
[GetPropertyDefaultVectorValue](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.GetPropertyDefaultVectorValue.html) | Returns the default Vector4 value of the shader property at the specified index.  
[GetPropertyDescription](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.GetPropertyDescription.html) | Returns the description string of the shader property at the specified index.  
[GetPropertyFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.GetPropertyFlags.html) | Returns the ShaderPropertyFlags of the shader property at the specified index.  
[GetPropertyName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.GetPropertyName.html) | Returns the name of the shader property at the specified index.  
[GetPropertyNameId](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.GetPropertyNameId.html) | Returns the nameId of the shader property at the specified index.  
[GetPropertyRangeLimits](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.GetPropertyRangeLimits.html) | Returns the min and max limits for a Range property at the specified index.  
[GetPropertyTextureDefaultName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.GetPropertyTextureDefaultName.html) | Returns the default Texture name of a Texture shader property at the specified index.  
[GetPropertyTextureDimension](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.GetPropertyTextureDimension.html) | Returns the TextureDimension of a Texture shader property at the specified index.  
[GetPropertyType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.GetPropertyType.html) | Returns the ShaderPropertyType of the property at the specified index.  
### Static Methods
Method | Description  
---|---  
[DisableKeyword](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.DisableKeyword.html) | Disables a global shader keyword.  
[EnableKeyword](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.EnableKeyword.html) | Enables a global shader keyword.  
[Find](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.Find.html) | Finds a shader with the given name. Returns null if the shader is not found.  
[GetGlobalColor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.GetGlobalColor.html) | Gets a global color property for all shaders previously set using SetGlobalColor.  
[GetGlobalFloat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.GetGlobalFloat.html) | Gets a global float property for all shaders previously set using SetGlobalFloat.  
[GetGlobalFloatArray](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.GetGlobalFloatArray.html) | Gets a global float array for all shaders previously set using SetGlobalFloatArray.  
[GetGlobalInt](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.GetGlobalInt.html) | This method is deprecated. Use GetGlobalFloat or GetGlobalInteger instead.  
[GetGlobalInteger](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.GetGlobalInteger.html) | Gets a global integer property for all shaders previously set using SetGlobalInteger.  
[GetGlobalMatrix](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.GetGlobalMatrix.html) | Gets a global matrix property for all shaders previously set using SetGlobalMatrix.  
[GetGlobalMatrixArray](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.GetGlobalMatrixArray.html) | Gets a global matrix array for all shaders previously set using SetGlobalMatrixArray.  
[GetGlobalTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.GetGlobalTexture.html) | Gets a global texture property for all shaders previously set using SetGlobalTexture.  
[GetGlobalVector](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.GetGlobalVector.html) | Gets a global vector property for all shaders previously set using SetGlobalVector.  
[GetGlobalVectorArray](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.GetGlobalVectorArray.html) | Gets a global vector array for all shaders previously set using SetGlobalVectorArray.  
[IsKeywordEnabled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.IsKeywordEnabled.html) | Checks whether a global shader keyword is enabled.  
[PropertyToID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.PropertyToID.html) | Gets unique identifier for a shader property name.  
[SetGlobalBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.SetGlobalBuffer.html) | Sets a global buffer property for all shaders.  
[SetGlobalColor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.SetGlobalColor.html) | Sets a global color property for all shaders.  
[SetGlobalConstantBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.SetGlobalConstantBuffer.html) | Sets a ComputeBuffer or GraphicsBuffer as a named constant buffer for all shader types.  
[SetGlobalFloat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.SetGlobalFloat.html) | Sets a global float property for all shaders.  
[SetGlobalFloatArray](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.SetGlobalFloatArray.html) | Sets a global float array property for all shaders.  
[SetGlobalInt](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.SetGlobalInt.html) | This method is deprecated. Use SetGlobalFloat or SetGlobalInteger instead.  
[SetGlobalInteger](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.SetGlobalInteger.html) | Sets a global integer property for all shaders.  
[SetGlobalMatrix](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.SetGlobalMatrix.html) | Sets a global matrix property for all shaders.  
[SetGlobalMatrixArray](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.SetGlobalMatrixArray.html) | Sets a global matrix array property for all shaders.  
[SetGlobalRayTracingAccelerationStructure](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.SetGlobalRayTracingAccelerationStructure.html) | Sets a global RayTracingAccelerationStructure property for all shaders.  
[SetGlobalTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.SetGlobalTexture.html) | Sets a global texture property for all shaders.  
[SetGlobalVector](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.SetGlobalVector.html) | Sets a global vector property for all shaders.  
[SetGlobalVectorArray](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.SetGlobalVectorArray.html) | Sets a global vector array property for all shaders.  
[SetKeyword](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.SetKeyword.html) | Sets the state of a global shader keyword.  
[WarmupAllShaders](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.WarmupAllShaders.html) | Prewarms all shader variants of all Shaders currently in memory.  
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
