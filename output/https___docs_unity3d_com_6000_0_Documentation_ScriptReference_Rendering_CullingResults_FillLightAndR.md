* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CullingResults.FillLightAndReflectionProbeIndices.html

#  [CullingResults](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CullingResults.html).FillLightAndReflectionProbeIndices
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
public void FillLightAndReflectionProbeIndices([ComputeBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeBuffer.html) computeBuffer); 
## Declaration
public void FillLightAndReflectionProbeIndices([GraphicsBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.html) buffer); 
### Parameters
Parameter | Description  
---|---  
computeBuffer | The compute buffer object to fill.  
buffer | The buffer object to fill.  
### Description
Fills a buffer with per-object light indices.
Additional resources: [CullingResults.lightIndexCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CullingResults-lightIndexCount.html), [CullingResults.visibleLights](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CullingResults-visibleLights.html), [CullingResults.visibleReflectionProbes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CullingResults-visibleReflectionProbes.html).
* * *
