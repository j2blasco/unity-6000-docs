* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings.html

# QualitySettings
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-QualitySettings.html "Go to QualitySettings Component in the Manual")
### Description
This represents the script interface for [Quality Settings](https://docs.unity3d.com/6000.0/Documentation/Manual/class-QualitySettings.html).
Use the `QualitySettings` class to change the current quality level at runtime. You can check the details of quality settings in your project's [Quality Settings](https://docs.unity3d.com/6000.0/Documentation/Manual/class-QualitySettings.html).
### Static Properties
Property | Description  
---|---  
[activeColorSpace](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings-activeColorSpace.html) | Active color space (Read Only).  
[anisotropicFiltering](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings-anisotropicFiltering.html) | Global anisotropic filtering mode.  
[antiAliasing](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings-antiAliasing.html) | Choose the level of Multi-Sample Anti-aliasing (MSAA) that the GPU performs.  
[asyncUploadBufferSize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings-asyncUploadBufferSize.html) | Sets the ring buffer size used for asynchronous texture and mesh data uploads.  
[asyncUploadPersistentBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings-asyncUploadPersistentBuffer.html) | This flag determines whether Unity retains the ring buffer allocation used for asynchronous texture and mesh uploads after all upload operations have completed.  
[asyncUploadTimeSlice](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings-asyncUploadTimeSlice.html) | Sets the time-slice allocated per frame for asynchronous texture and mesh data uploads.  
[billboardsFaceCameraPosition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings-billboardsFaceCameraPosition.html) | If enabled, billboards will face towards camera position rather than camera orientation.  
[count](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings-count.html) | The number of Quality Levels.  
[desiredColorSpace](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings-desiredColorSpace.html) | Desired color space (Read Only).  
[enableLODCrossFade](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings-enableLODCrossFade.html) | Enables or disables LOD Cross Fade.  
[globalTextureMipmapLimit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings-globalTextureMipmapLimit.html) | Indicates how many of the highest-resolution mips of each texture Unity does not upload at the given quality level. To set more specific mipmap limits, you can flag textures to ignore mipmap limits or assign them to mipmap limit groups.  
[lodBias](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings-lodBias.html) | Global multiplier for the LOD's switching distance.  
[maximumLODLevel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings-maximumLODLevel.html) | A maximum LOD level. All LOD groups.  
[maxQueuedFrames](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings-maxQueuedFrames.html) | Maximum number of frames queued up by graphics driver.  
[names](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings-names.html) | The indexed list of available Quality Settings.  
[particleRaycastBudget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings-particleRaycastBudget.html) | Budget for how many ray casts can be performed per frame for approximate collision testing.  
[pixelLightCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings-pixelLightCount.html) | The maximum number of pixel lights that should affect any object.  
[realtimeGICPUUsage](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings-realtimeGICPUUsage.html) | How much CPU usage to assign to the final lighting calculations at runtime.  
[realtimeReflectionProbes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings-realtimeReflectionProbes.html) | Enables or disables real-time reflection probes.  
[renderPipeline](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings-renderPipeline.html) | The RenderPipelineAsset that defines the override render pipeline for the current quality level.  
[resolutionScalingFixedDPIFactor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings-resolutionScalingFixedDPIFactor.html) | In resolution scaling mode, this factor is used to multiply with the target Fixed DPI specified to get the actual Fixed DPI to use for this quality setting.  
[shadowCascade2Split](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings-shadowCascade2Split.html) | The normalized cascade distribution for a 2 cascade setup. The value defines the position of the cascade with respect to Zero.  
[shadowCascade4Split](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings-shadowCascade4Split.html) | The normalized cascade start position for a 4 cascade setup. Each member of the vector defines the normalized position of the coresponding cascade with respect to Zero.  
[shadowCascades](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings-shadowCascades.html) | Number of cascades to use for directional light shadows.  
[shadowDistance](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings-shadowDistance.html) | Shadow drawing distance.  
[shadowmaskMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings-shadowmaskMode.html) | The rendering mode of Shadowmask.  
[shadowNearPlaneOffset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings-shadowNearPlaneOffset.html) | Offset shadow frustum near plane.  
[shadowProjection](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings-shadowProjection.html) | Directional light shadow projection.  
[shadowResolution](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings-shadowResolution.html) | The default resolution of the shadow maps.  
[shadows](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings-shadows.html) | Real-time Shadows type to be used.  
[skinWeights](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings-skinWeights.html) | The maximum number of bones per vertex that are taken into account during skinning, for all meshes in the project.  
[softParticles](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings-softParticles.html) | Should soft blending be used for particles?  
[softVegetation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings-softVegetation.html) | Use a two-pass shader for the vegetation in the terrain engine.  
[streamingMipmapsActive](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings-streamingMipmapsActive.html) | Enable automatic streaming of texture mipmap levels based on their distance from all active cameras.  
[streamingMipmapsAddAllCameras](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings-streamingMipmapsAddAllCameras.html) | Process all enabled Cameras for texture streaming (rather than just those with StreamingController components).  
[streamingMipmapsMaxFileIORequests](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings-streamingMipmapsMaxFileIORequests.html) | The maximum number of active texture file IO requests from the texture streaming system.  
[streamingMipmapsMaxLevelReduction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings-streamingMipmapsMaxLevelReduction.html) | The maximum number of mipmap levels to discard for each texture.  
[streamingMipmapsMemoryBudget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings-streamingMipmapsMemoryBudget.html) | The total amount of memory (in megabytes) to be used by streaming and non-streaming textures.  
[streamingMipmapsRenderersPerFrame](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings-streamingMipmapsRenderersPerFrame.html) | The number of renderer instances that are processed each frame when calculating which texture mipmap levels should be streamed.  
[terrainBasemapDistance](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings-terrainBasemapDistance.html) | Value set to Terrain.basemapDistance if TerrainQualityOverrides.BasemapDistance is set in terrainQualityOverrides.  
[terrainBillboardStart](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings-terrainBillboardStart.html) | Value set to Terrain.treeBillboardDistance if TerrainQualityOverrides.BillboardStart is set in terrainQualityOverrides.  
[terrainDetailDensityScale](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings-terrainDetailDensityScale.html) | Value set to Terrain.detailObjectDensity if TerrainQualityOverrides.DetailDensity is set in terrainQualityOverrides.  
[terrainDetailDistance](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings-terrainDetailDistance.html) | Value set to Terrain.detailObjectDistance if TerrainQualityOverrides.DetailDistance is set in terrainQualityOverrides.  
[terrainFadeLength](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings-terrainFadeLength.html) | Value set to Terrain.treeCrossFadeLength if TerrainQualityOverrides.FadeLength is set in terrainQualityOverrides.  
[terrainMaxTrees](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings-terrainMaxTrees.html) | Value set to Terrain.treeMaximumFullLODCount if TerrainQualityOverrides.MaxTrees is set in terrainQualityOverrides.  
[terrainPixelError](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings-terrainPixelError.html) | Value set to Terrain.heightmapPixelError if TerrainQualityOverrides.PixelError is set in terrainQualityOverrides.  
[terrainQualityOverrides](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings-terrainQualityOverrides.html) | Controls which fields should have their values overriden in active Terrains.  
[terrainTreeDistance](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings-terrainTreeDistance.html) | Value set to Terrain.treeDistance if TerrainQualityOverrides.TreeDistance is set in terrainQualityOverrides.  
[useLegacyDetailDistribution](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings-useLegacyDetailDistribution.html) | Use the legacy pre-2022.2 algorithm for distributing details on terrain.  
[vSyncCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings-vSyncCount.html) | Represents the number of vertical syncs that should pass between each frame.  
### Static Methods
Method | Description  
---|---  
[DecreaseLevel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings.DecreaseLevel.html) | Decrease the current quality level.  
[ForEach](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings.ForEach.html) | Executes the given Action for each tier on the QualitySettings.  
[GetActiveQualityLevelsForPlatform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings.GetActiveQualityLevelsForPlatform.html) | [Editor Only] Obtains an array with the Quality Level indexes that are selected for the given platform.  
[GetActiveQualityLevelsForPlatformCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings.GetActiveQualityLevelsForPlatformCount.html) | [Editor Only] Obtains the number of Quality Levels that are selected for a given platform.  
[GetAllRenderPipelineAssetsForPlatform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings.GetAllRenderPipelineAssetsForPlatform.html) | [Editor Only] Fills the given list with all the Render Pipeline Assets on any Quality Level for the given platform. Without filtering by Render Pipeline Asset type or null.  
[GetQualityLevel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings.GetQualityLevel.html) | Returns the current graphics quality level.  
[GetQualitySettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings.GetQualitySettings.html) | Provides a reference to the QualitySettings object.  
[GetRenderPipelineAssetAt](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings.GetRenderPipelineAssetAt.html) | Provides a reference to the RenderPipelineAsset that defines the override render pipeline for a given quality level.   
[GetRenderPipelineAssetsForPlatform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings.GetRenderPipelineAssetsForPlatform.html) | [Editor Only] Obtains a set with the non null Render Pipeline Assets selected on all the Quality Levels for the given platform.  
[GetTextureMipmapLimitSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings.GetTextureMipmapLimitSettings.html) | Retrieves a copy of the TextureMipmapLimitSettings from a texture mipmap limit group.  
[IncreaseLevel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings.IncreaseLevel.html) | Increase the current quality level.  
[IsPlatformIncluded](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings.IsPlatformIncluded.html) | [Editor Only] Returns if the given platform is included by the Quality Level.  
[SetLODSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings.SetLODSettings.html) | Sets the lodBias and maximumLODLevel at the same time.  
[SetQualityLevel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings.SetQualityLevel.html) | Sets a new graphics quality level.  
[SetTextureMipmapLimitSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings.SetTextureMipmapLimitSettings.html) | Applies new TextureMipmapLimitSettings to the indicated texture mipmap limit group.  
[TryExcludePlatformAt](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings.TryExcludePlatformAt.html) | [Editor Only] Excludes a platform for the given Quality Level.  
[TryIncludePlatformAt](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings.TryIncludePlatformAt.html) | [Editor Only] Includes a platform to be supported by the Quality Level.  
### Events
Event | Description  
---|---  
[activeQualityLevelChanged](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings-activeQualityLevelChanged.html) | Delegate that you can use to invoke custom code when Unity changes the current Quality Level.  
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
