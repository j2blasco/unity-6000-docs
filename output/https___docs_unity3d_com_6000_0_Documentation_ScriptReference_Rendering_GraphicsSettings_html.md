* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsSettings.html

# GraphicsSettings
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
Script interface for [Graphics Settings](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GraphicsSettings.html).
### Static Properties
Property | Description  
---|---  
[allConfiguredRenderPipelines](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsSettings-allConfiguredRenderPipelines.html) | An array containing the RenderPipelineAsset instances that describe the default render pipeline and any quality level overrides.  
[cameraRelativeLightCulling](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsSettings-cameraRelativeLightCulling.html) | Enable or disable using the camera position as the reference point for culling lights.  
[cameraRelativeShadowCulling](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsSettings-cameraRelativeShadowCulling.html) | Enable or disable using the camera position as the reference point for culling shadows.  
[currentRenderPipeline](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsSettings-currentRenderPipeline.html) | The RenderPipelineAsset that defines the active render pipeline for the current quality level.  
[currentRenderPipelineAssetType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsSettings-currentRenderPipelineAssetType.html) | The type of the currently active RenderPipelineAsset, or null if there's no currently active Asset.  
[defaultGateFitMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsSettings-defaultGateFitMode.html) | Stores the default value for the GateFit property of newly created Cameras.  
[defaultRenderPipeline](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsSettings-defaultRenderPipeline.html) | The RenderPipelineAsset that defines the default render pipeline.  
[disableBuiltinCustomRenderTextureUpdate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsSettings-disableBuiltinCustomRenderTextureUpdate.html) | Disables the built-in update loop for Custom Render Textures, so that you can write your own update loop.  
[isScriptableRenderPipelineEnabled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsSettings-isScriptableRenderPipelineEnabled.html) | If the value is true, a Scriptable Render Pipeline is active.  
[lightProbeOutsideHullStrategy](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsSettings-lightProbeOutsideHullStrategy.html) | Defines the way Unity chooses a probe to light a Renderer that is lit by Light Probes but positioned outside the bounds of the Light Probe tetrahedral hull.  
[lightsUseColorTemperature](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsSettings-lightsUseColorTemperature.html) | Whether to use a Light's color temperature when calculating the final color of that Light."  
[lightsUseLinearIntensity](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsSettings-lightsUseLinearIntensity.html) | If this is true, Light intensity is multiplied against linear color values. If it is false, gamma color values are used.  
[logWhenShaderIsCompiled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsSettings-logWhenShaderIsCompiled.html) | If this is true, a log entry is made each time a shader is compiled at application runtime.  
[realtimeDirectRectangularAreaLights](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsSettings-realtimeDirectRectangularAreaLights.html) | Is the current render pipeline capable of rendering direct lighting for rectangular area Lights?  
[transparencySortAxis](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsSettings-transparencySortAxis.html) | An axis that describes the direction along which the distances of objects are measured for the purpose of sorting.  
[transparencySortMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsSettings-transparencySortMode.html) | Transparent object sorting mode.  
[useScriptableRenderPipelineBatching](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsSettings-useScriptableRenderPipelineBatching.html) | Enable/Disable SRP batcher (experimental) at runtime.  
[videoShadersIncludeMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsSettings-videoShadersIncludeMode.html) | If and when to include video shaders in the build.  
### Static Methods
Method | Description  
---|---  
[ForEach](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsSettings.ForEach.html) | Executes the given callback for each IRenderPipelineGraphicsSettings.  
[GetCustomShader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsSettings.GetCustomShader.html) | Get custom shader used instead of a built-in shader.  
[GetGraphicsSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsSettings.GetGraphicsSettings.html) | Provides a reference to the GraphicSettings object.  
[GetRenderPipelineSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsSettings.GetRenderPipelineSettings.html) | Gets the RenderPipelineGlobalSettings asset assigned to the given RenderPipeline asset.  
[GetSettingsForRenderPipeline](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsSettings.GetSettingsForRenderPipeline.html) | Get the registered RenderPipelineGlobalSettings for the given RenderPipeline.  
[GetShaderMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsSettings.GetShaderMode.html) | Get built-in shader mode.  
[HasShaderDefine](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsSettings.HasShaderDefine.html) | Returns true if shader define was set when compiling shaders for current GraphicsTier. Graphics Tiers are only available in the Built-in Render Pipeline.  
[SetCustomShader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsSettings.SetCustomShader.html) | Set custom shader to use instead of a built-in shader.  
[SetShaderMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsSettings.SetShaderMode.html) | Set built-in shader mode.  
[Subscribe](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsSettings.Subscribe.html) | Subscribe to changes of properties in the IRenderPipelineGraphicsSettings.  
[TryGetCurrentRenderPipelineGlobalSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsSettings.TryGetCurrentRenderPipelineGlobalSettings.html) | Obtains the current active pipeline RenderPipelineGlobalSettings.  
[TryGetRenderPipelineSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsSettings.TryGetRenderPipelineSettings.html) | Gets a IRenderPipelineGraphicsSettings from the GraphicsSettings and returns if the setting is found.  
[Unsubscribe](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsSettings.Unsubscribe.html) | Cancels any subscription to changes of properties of a settings object implemented with the IRenderPipelineGraphicsSettings interface.  
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
