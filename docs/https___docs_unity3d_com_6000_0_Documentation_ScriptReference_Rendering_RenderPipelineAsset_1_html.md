* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipelineAsset_1.html

# RenderPipelineAsset<T0>
class in UnityEngine.Rendering
/
Inherits from:[Rendering.RenderPipelineAsset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipelineAsset.html)
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
An asset that produces a specific IRenderPipeline.
Default implementation of IRenderPipelineAsset. This manages the lifecylces of inherited types, as well as ensures that created IRenderPipeline's are invalidated when the asset is changed.  
  
Additional resources: IRenderPipelineAsset.
### Properties
Property | Description  
---|---  
[pipelineType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipelineAsset_1-pipelineType.html) | Returns a RenderPipeline type associated with the given RenderPipelineAsset instance.  
[renderPipelineShaderTag](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipelineAsset_1-renderPipelineShaderTag.html) | Returns the Shader Tag value for the render pipeline that is described by this asset.  
### Inherited Members
### Properties
Property | Description  
---|---  
[hideFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-hideFlags.html) | Should the object be hidden, saved with the Scene or modifiable by the user?  
[name](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-name.html) | The name of the object.  
[autodeskInteractiveMaskedShader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipelineAsset-autodeskInteractiveMaskedShader.html) | Retrieves the default Autodesk Interactive masked Shader for this pipeline.  
[autodeskInteractiveShader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipelineAsset-autodeskInteractiveShader.html) | Retrieves the default Autodesk Interactive Shader for this pipeline.  
[autodeskInteractiveTransparentShader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipelineAsset-autodeskInteractiveTransparentShader.html) | Retrieves the default Autodesk Interactive transparent Shader for this pipeline.  
[default2DMaskMaterial](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipelineAsset-default2DMaskMaterial.html) | Gets the default 2D Mask Material used by Sprite Masks in Universal Render Pipeline.  
[default2DMaterial](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipelineAsset-default2DMaterial.html) | Return the default 2D Material for this pipeline.  
[defaultLineMaterial](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipelineAsset-defaultLineMaterial.html) | Return the default Line Material for this pipeline.  
[defaultMaterial](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipelineAsset-defaultMaterial.html) | Return the default Material for this pipeline.  
[defaultParticleMaterial](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipelineAsset-defaultParticleMaterial.html) | Return the default particle Material for this pipeline.  
[defaultShader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipelineAsset-defaultShader.html) | Return the default Shader for this pipeline.  
[defaultSpeedTree7Shader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipelineAsset-defaultSpeedTree7Shader.html) | Return the default SpeedTree v7 Shader for this pipeline.  
[defaultSpeedTree8Shader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipelineAsset-defaultSpeedTree8Shader.html) | Return the default SpeedTree v8 Shader for this pipeline.  
[defaultSpeedTree9Shader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipelineAsset-defaultSpeedTree9Shader.html) | Return the default SpeedTree v9 Shader for this pipeline.  
[defaultTerrainMaterial](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipelineAsset-defaultTerrainMaterial.html) | Return the default Terrain Material for this pipeline.  
[defaultUIETC1SupportedMaterial](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipelineAsset-defaultUIETC1SupportedMaterial.html) | Return the default UI ETC1 Material for this pipeline.  
[defaultUIMaterial](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipelineAsset-defaultUIMaterial.html) | Return the default UI Material for this pipeline.  
[defaultUIOverdrawMaterial](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipelineAsset-defaultUIOverdrawMaterial.html) | Return the default UI overdraw Material for this pipeline.  
[pipelineType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipelineAsset-pipelineType.html) | Returns a RenderPipeline type associated with the given RenderPipelineAsset instance.  
[renderPipelineShaderTag](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipelineAsset-renderPipelineShaderTag.html) | Returns the Shader Tag value for the render pipeline that is described by this asset.  
[terrainBrushPassIndex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipelineAsset-terrainBrushPassIndex.html) | The render index for the terrain brush in the editor.  
[terrainDetailGrassBillboardShader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipelineAsset-terrainDetailGrassBillboardShader.html) | Return the detail grass billboard Shader for this pipeline.  
[terrainDetailGrassShader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipelineAsset-terrainDetailGrassShader.html) | Return the detail grass Shader for this pipeline.  
[terrainDetailLitShader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipelineAsset-terrainDetailLitShader.html) | Return the detail lit Shader for this pipeline.  
### Public Methods
Method | Description  
---|---  
[GetInstanceID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.GetInstanceID.html) | Gets the instance ID of the object.  
[ToString](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.ToString.html) | Returns the name of the object.  
### Protected Methods
Method | Description  
---|---  
[CreatePipeline](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipelineAsset.CreatePipeline.html) | Create a IRenderPipeline specific to this asset.  
[EnsureGlobalSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipelineAsset.EnsureGlobalSettings.html) | Ensures Global Settings are ready and registered into GraphicsSettings.  
[OnDisable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipelineAsset.OnDisable.html) | Default implementation of OnDisable for RenderPipelineAsset. See ScriptableObject.OnDisable  
[OnValidate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipelineAsset.OnValidate.html) | Default implementation of OnValidate for RenderPipelineAsset. See MonoBehaviour.OnValidate  
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
[CreateInstance](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.CreateInstance.html) | Creates an instance of a scriptable object.  
### Operators
Operator | Description  
---|---  
[bool](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-operator_Object.html) | Does the object exist?  
[operator !=](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-operator_ne.html) | Compares if two objects refer to a different object.  
[operator ==](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-operator_eq.html) | Compares two object references to see if they refer to the same object.  
### Messages
Message | Description  
---|---  
[Awake](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.Awake.html) | Called when an instance of ScriptableObject is created.  
[OnDestroy](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.OnDestroy.html) | This function is called when the scriptable object will be destroyed.  
[OnDisable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.OnDisable.html) | This function is called when the scriptable object goes out of scope.  
[OnEnable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.OnEnable.html) | This function is called when the object is loaded.  
[OnValidate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.OnValidate.html) | Editor-only function that Unity calls when the script is loaded or a value changes in the Inspector.  
[Reset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.Reset.html) | Reset to default values.  
* * *
