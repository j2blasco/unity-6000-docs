* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.SupportedRenderingFeatures.html

# SupportedRenderingFeatures
class in UnityEngine.Rendering
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
Describes the rendering features supported by a given render pipeline.
Set the active supported rendering features when enabling a render pipeline. This will change the state of the editor UI to reflect the changes.
### Static Properties
Property | Description  
---|---  
[active](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.SupportedRenderingFeatures-active.html) | Get / Set a SupportedRenderingFeatures.  
### Properties
Property | Description  
---|---  
[ambientProbeBaking](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.SupportedRenderingFeatures-ambientProbeBaking.html) | Determines if this renderer supports ambient probe baking.  
[defaultMixedLightingModes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.SupportedRenderingFeatures-defaultMixedLightingModes.html) | This is the fallback mode if the mode the user had previously selected is no longer available. See SupportedRenderingFeatures.mixedLightingModes.  
[defaultReflectionProbeBaking](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.SupportedRenderingFeatures-defaultReflectionProbeBaking.html) | Specifies whether this renderer bakes a default Reflection Probe.  
[editableMaterialRenderQueue](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.SupportedRenderingFeatures-editableMaterialRenderQueue.html) | Determines whether the Scriptable Render Pipeline will override the default Material’s Render Queue settings and, if true, hides the Render Queue property in the Inspector.  
[enlighten](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.SupportedRenderingFeatures-enlighten.html) | Determines if Enlighten Realtime Global Illumination lightmapper is supported by the currently selected pipeline. If it is not supported, Enlighten-specific settings do not appear in the Editor, which then defaults to the CPU Lightmapper.  
[lightmapBakeTypes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.SupportedRenderingFeatures-lightmapBakeTypes.html) | What baking types are supported. The unsupported ones will be hidden from the UI. See LightmapBakeType.  
[lightmapsModes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.SupportedRenderingFeatures-lightmapsModes.html) | Specifies what modes are supported. Has to be at least one. See LightmapsMode.  
[lightProbeProxyVolumes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.SupportedRenderingFeatures-lightProbeProxyVolumes.html) | Are light probe proxy volumes supported?  
[mixedLightingModes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.SupportedRenderingFeatures-mixedLightingModes.html) | Specifies what LightmapMixedBakeModes that are supported. Please define a SupportedRenderingFeatures.defaultMixedLightingModes in case multiple modes are supported.  
[motionVectors](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.SupportedRenderingFeatures-motionVectors.html) | Are motion vectors supported?  
[overridesEnableLODCrossFade](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.SupportedRenderingFeatures-overridesEnableLODCrossFade.html) | Specifies whether the renderer overrides the Enable LOD Cross Fade settings in the Quality Settings Panel. If It does, the renderer does not need the built-in UI for Enable LOD Cross Fade settings.  
[overridesEnvironmentLighting](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.SupportedRenderingFeatures-overridesEnvironmentLighting.html) | Determines if the renderer will override the Environment Lighting and will no longer need the built-in UI for it.  
[overridesFog](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.SupportedRenderingFeatures-overridesFog.html) | Determines if the renderer will override the fog settings in the Lighting Panel and will no longer need the built-in UI for it.  
[overridesLightProbeSystem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.SupportedRenderingFeatures-overridesLightProbeSystem.html) | Determines if the renderer will override the light probe system with a different one.  
[overridesLightProbeSystemWarningMessage](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.SupportedRenderingFeatures-overridesLightProbeSystemWarningMessage.html) | The message to display in the LightProbeGroup editor if the light probe system is overridden by the renderer.  
[overridesLODBias](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.SupportedRenderingFeatures-overridesLODBias.html) | Specifies whether the renderer overrides the LOD bias settings in the Quality Settings Panel. If It does, the renderer does not need the built-in UI for LOD bias settings.  
[overridesMaximumLODLevel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.SupportedRenderingFeatures-overridesMaximumLODLevel.html) | Specifies whether the renderer overrides the maximum LOD level settings in the Quality Settings Panel. If It does, the renderer does not need the built-in UI for maximum LOD level settings.  
[overridesOtherLightingSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.SupportedRenderingFeatures-overridesOtherLightingSettings.html) | Determines if the renderer will override halo and flare settings in the Lighting Panel and will no longer need the built-in UI for it.  
[overridesRealtimeReflectionProbes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.SupportedRenderingFeatures-overridesRealtimeReflectionProbes.html) | Specifies whether the render pipeline overrides the real-time Reflection Probes settings in the Quality settings. If It does, the render pipeline does not need the built-in UI for real-time Reflection Probes settings.  
[overridesShadowmask](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.SupportedRenderingFeatures-overridesShadowmask.html) | Specifies whether the render pipeline overrides the Shadowmask settings in the Quality settings.  
[particleSystemInstancing](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.SupportedRenderingFeatures-particleSystemInstancing.html) | Determines if the renderer supports Particle System GPU instancing.  
[receiveShadows](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.SupportedRenderingFeatures-receiveShadows.html) | Can renderers support receiving shadows?  
[reflectionProbeModes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.SupportedRenderingFeatures-reflectionProbeModes.html) | Flags for supported reflection probes.  
[reflectionProbes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.SupportedRenderingFeatures-reflectionProbes.html) | Are reflection probes supported?  
[reflectionProbesBlendDistance](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.SupportedRenderingFeatures-reflectionProbesBlendDistance.html) | If this property is true, the blend distance field in the Reflection Probe Inspector window is editable.  
[rendererPriority](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.SupportedRenderingFeatures-rendererPriority.html) | Determines if the renderer supports renderer priority sorting.  
[rendererProbes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.SupportedRenderingFeatures-rendererProbes.html) | Determines whether the Renderer supports probe lighting.  
[rendersUIOverlay](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.SupportedRenderingFeatures-rendersUIOverlay.html) | Determines whether the function to render UI overlays is called by SRP and not by the engine.  
[skyOcclusion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.SupportedRenderingFeatures-skyOcclusion.html) | If True, the renderer supports sky occlusion in Probe Volumes.  
[supportsClouds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.SupportedRenderingFeatures-supportsClouds.html) | If True, the renderer supports cloud layers or volumetric clouds.  
[supportsHDR](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.SupportedRenderingFeatures-supportsHDR.html) | If True, the renderer supports HDR display output.  
* * *
