* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Lightmapping.html

# Lightmapping
class in UnityEditor
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
Allows to control the lightmapping job.
Before starting the job the bake settings can be set via [LightingSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightingSettings.html).  
  
Additional resources: [LightingSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightingSettings.html).
### Static Properties
Property | Description  
---|---  
[bakedGI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Lightmapping-bakedGI.html) | This property is now obsolete. Use LightingSettings.bakedGI.  
[bakeOnSceneLoad](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Lightmapping-bakeOnSceneLoad.html) | Determines whether lighting data should be generated when loading a scene, for scenes that have not already been baked.  
[buildProgress](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Lightmapping-buildProgress.html) | Returns the current lightmapping build progress or 0 if Lightmapping.isRunning is false.  
[isRunning](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Lightmapping-isRunning.html) | Returns true when the bake job is running, false otherwise (Read Only).  
[lightingDataAsset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Lightmapping-lightingDataAsset.html) | The lighting data asset used by the active Scene.  
[lightingSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Lightmapping-lightingSettings.html) | The LightingSettings that will be used for the current Scene. Will throw an exception if it is null.  
[lightingSettingsDefaults](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Lightmapping-lightingSettingsDefaults.html) | Default LightingSettings that Unity uses for Scenes where lightingSettings is not assigned. (Read only)  
[realtimeGI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Lightmapping-realtimeGI.html) | This property is now obsolete. Use LightingSettings.realtimeGI.  
### Static Methods
Method | Description  
---|---  
[Bake](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Lightmapping.Bake.html) | Starts a synchronous bake job.  
[BakeAsync](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Lightmapping.BakeAsync.html) | Starts an asynchronous bake job.  
[BakeMultipleScenes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Lightmapping.BakeMultipleScenes.html) | Bakes an array of Scenes.  
[BakeReflectionProbe](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Lightmapping.BakeReflectionProbe.html) | Starts a synchronous bake job for the probe.  
[Cancel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Lightmapping.Cancel.html) | Cancels the currently running asynchronous bake job.  
[Clear](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Lightmapping.Clear.html) | Deletes all runtime data for the currently loaded Scenes.  
[ClearDiskCache](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Lightmapping.ClearDiskCache.html) | Clears the cache used by lightmaps, reflection probes and default reflection.  
[ClearLightingDataAsset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Lightmapping.ClearLightingDataAsset.html) | For the currently loaded Scenes, this method deletes the Lighting Data Asset and any linked lightmaps and Reflection Probe assets.  
[GetAdditionalBakeDelegate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Lightmapping.GetAdditionalBakeDelegate.html) | Get the currently set additional bake delegate.  
[GetLightingDataAssetForScene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Lightmapping.GetLightingDataAssetForScene.html) | Gets the LightingDataAsset associated with a specific scene. This method will return null if the scene has no LightingDataAsset, or the scene is invalid.  
[GetLightingSettingsForScene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Lightmapping.GetLightingSettingsForScene.html) | Gets the LightingSettings object of a Scene object.  
[GetTerrainGIChunks](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Lightmapping.GetTerrainGIChunks.html) | Get how many chunks the terrain is divided into for GI baking.  
[ResetAdditionalBakeDelegate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Lightmapping.ResetAdditionalBakeDelegate.html) | Resets the additional bake delegate to Unity's default.  
[SetAdditionalBakeDelegate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Lightmapping.SetAdditionalBakeDelegate.html) | Set a delegate that bakes additional data. This delegates must set its done parameter to true once baking is finished to unlock the baking pipeline. Must be reset by calling ResetDelegate again.  
[SetLightingDataAssetForScene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Lightmapping.SetLightingDataAssetForScene.html) | Sets the LightingDataAsset associated with a specific scene.  
[SetLightingSettingsForScene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Lightmapping.SetLightingSettingsForScene.html) | Applies the settings specified in the LightingSettings object to the Scene object.  
[SetLightingSettingsForScenes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Lightmapping.SetLightingSettingsForScenes.html) | Applies the settings specified in the LightingSettings object to an array of Scene objects.  
[Tetrahedralize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Lightmapping.Tetrahedralize.html) | Calculates tetrahderons from positions using Delaunay Tetrahedralization.  
[TryGetLightingSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Lightmapping.TryGetLightingSettings.html) | Fetches the Lighting Settings for the current Scene. Will return false if it is null.  
### Events
Event | Description  
---|---  
[bakeCancelled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Lightmapping-bakeCancelled.html) | Event which is called when bake job is cancelled.  
[bakeCompleted](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Lightmapping-bakeCompleted.html) | Event which is called when bake job is completed. Only called when LightingSettings.autoGenerate is set to false.  
[bakeStarted](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Lightmapping-bakeStarted.html) | Event which is called when a bake is started. Only called when LightingSettings.autoGenerate is set to false.  
[lightingDataAssetCleared](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Lightmapping-lightingDataAssetCleared.html) | Event which is called when a LightingData asset is removed from the project.  
[lightingDataCleared](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Lightmapping-lightingDataCleared.html) | Event which is called when baked Global Illumination data is cleared from the scene and from renderers.  
[lightingDataUpdated](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Lightmapping-lightingDataUpdated.html) | Event which is called when any lighting data is updated as part of the GI backing process.  
[started](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Lightmapping-started.html) | Delegate which is called when bake job is started.  
### Delegates
Delegate | Description  
---|---  
[AdditionalBakeDelegate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Lightmapping.AdditionalBakeDelegate.html) | Delegate called at the last stage of the baking pipeline.  
[OnCompletedFunction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Lightmapping.OnCompletedFunction.html) | Delegate used by Lightmapping.completed callback.  
[OnStartedFunction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Lightmapping.OnStartedFunction.html) | Delegate used by Lightmapping.started callback.  
* * *
