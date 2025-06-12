* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.InputExtraction.GetShadowmaskChannelsFromLightIndices.html

#  [InputExtraction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.InputExtraction.html).GetShadowmaskChannelsFromLightIndices
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
public static int[] GetShadowmaskChannelsFromLightIndices([LightTransport.InputExtraction.BakeInput](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.InputExtraction.BakeInput.html) bakeInput, int[] lightIndices); 
### Parameters
Parameter | Description  
---|---  
bakeInput | The BakeInput which the passed light indices belong to.  
lightIndices | The light indices of the lights to get the shadowmask channels of.  
### Returns
**int[]** An array containing the shadowmask channel of each input light. 
### Description
Get's the associated baked shadowmask channels of the mixed lights with the specified indices. Use this together with [InputExtraction.ComputeOcclusionLightIndicesFromBakeInput](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.InputExtraction.ComputeOcclusionLightIndicesFromBakeInput.html).
The resulting channels will be in the range [0;3], representing color channels red, green, blue and alpha respectively. The only exception is a value of -1, which indicates that the light has no shadowmask channel.
* * *
