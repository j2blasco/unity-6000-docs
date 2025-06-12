* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.InputExtraction.ComputeOcclusionLightIndicesFromBakeInput.html

#  [InputExtraction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.InputExtraction.html).ComputeOcclusionLightIndicesFromBakeInput
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
## Declaration
public static int[] ComputeOcclusionLightIndicesFromBakeInput([LightTransport.InputExtraction.BakeInput](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.InputExtraction.BakeInput.html) bakeInput, Vector3[] probePositions, uint maxLightsPerProbe); 
### Parameters
Parameter | Description  
---|---  
bakeInput | The BakeInput to use to find the brightest lights.  
probePositions | The positions from which to calculate the indices of the brightest lights.  
maxLightsPerProbe | The amount of light indices to calculate per probe. Defaults to 4.  
### Returns
**int[]** The indices of the brightest lights from each probe position. The returned array will have a length equal to the length of the probePositions array multiplied by maxLightsPerProbe. 
### Description
For each probe position, computes the indices of the brightest lights from the probe position's point of view. The function uses the information about lights stored in an existing [BakeInput](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.InputExtraction.BakeInput.html). This function is intended to be used with [IProbeIntegrator.IntegrateOcclusion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.IProbeIntegrator.IntegrateOcclusion.html).
Additional resources: [IProbeIntegrator.IntegrateOcclusion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.IProbeIntegrator.IntegrateOcclusion.html).
* * *
