* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DynamicGI.html

# DynamicGI
class in UnityEngine
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
Allows to control the dynamic Global Illumination.
Additional resources: [RendererExtensions.UpdateGIMaterials](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RendererExtensions.UpdateGIMaterials.html), [TerrainExtensions.UpdateGIMaterials](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainExtensions.UpdateGIMaterials.html).
### Static Properties
Property | Description  
---|---  
[indirectScale](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DynamicGI-indirectScale.html) | Allows for scaling the contribution coming from real-time & baked lightmaps.Note: this value can be set in the Lighting Window UI and it is serialized, that is not the case for other properties in this class.  
[isConverged](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DynamicGI-isConverged.html) | Is precomputed Enlighten Realtime Global Illumination output converged?  
[materialUpdateTimeSlice](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DynamicGI-materialUpdateTimeSlice.html) | The number of milliseconds that can be spent on material updates.  
[synchronousMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DynamicGI-synchronousMode.html) | When enabled, new dynamic Global Illumination output is shown in each frame.  
[updateThreshold](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DynamicGI-updateThreshold.html) | Determines the percentage change in lighting intensity that triggers Unity to recalculate the real-time lightmap.  
### Static Methods
Method | Description  
---|---  
[SetEmissive](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DynamicGI.SetEmissive.html) | Allows to set an emissive color for a given renderer quickly, without the need to render the emissive input for the entire system.  
[SetEnvironmentData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DynamicGI.SetEnvironmentData.html) | Allows overriding the distant environment lighting for Enlighten Realtime Global Illumination, without changing the Skybox Material.  
[UpdateEnvironment](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DynamicGI.UpdateEnvironment.html) | Schedules an update of the environment cubemap.  
[UpdateMaterials](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DynamicGI.UpdateMaterials.html) | Schedules an update of the albedo and emissive textures of a system that contains the renderer or the terrain.  
* * *
