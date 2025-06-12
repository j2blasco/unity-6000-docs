* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.InputExtraction.html

# InputExtraction
class in UnityEngine.LightTransport
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
Class used when extracting [BakeInput](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.InputExtraction.BakeInput.html) from the set of open scenes.
The [BakeInput](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.InputExtraction.BakeInput.html) class can be used to populate the world space data structures used by integrators. Related content: [IWorld](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.IWorld.html).
### Static Methods
Method | Description  
---|---  
[ComputeOcclusionLightIndicesFromBakeInput](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.InputExtraction.ComputeOcclusionLightIndicesFromBakeInput.html) | For each probe position, computes the indices of the brightest lights from the probe position's point of view. The function uses the information about lights stored in an existing BakeInput. This function is intended to be used with IProbeIntegrator.IntegrateOcclusion.  
[ExtractFromScene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.InputExtraction.ExtractFromScene.html) | Extract BakeInput from the set of open scenes.  
[GetShadowmaskChannelsFromLightIndices](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.InputExtraction.GetShadowmaskChannelsFromLightIndices.html) | Get's the associated baked shadowmask channels of the mixed lights with the specified indices. Use this together with InputExtraction.ComputeOcclusionLightIndicesFromBakeInput.  
[PopulateWorld](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.InputExtraction.PopulateWorld.html) | Populate the given world from a bake input.  
* * *
