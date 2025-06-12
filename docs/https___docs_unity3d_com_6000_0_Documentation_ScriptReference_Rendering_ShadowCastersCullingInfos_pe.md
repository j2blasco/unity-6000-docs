* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ShadowCastersCullingInfos-perLightInfos.html

#  [ShadowCastersCullingInfos](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ShadowCastersCullingInfos.html).perLightInfos
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
perLightInfos; 
### Description
An array of [LightShadowCasterCullingInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.LightShadowCasterCullingInfo.html).
Each entry in this array is associated with the [VisibleLight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VisibleLight.html) at the same position in the array [CullingResults.visibleLights](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CullingResults-visibleLights.html). Therefore, both arrays must have the same size. The [LightShadowCasterCullingInfo.splitRange](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.LightShadowCasterCullingInfo-splitRange.html) of each entry describes a range in the array [ShadowCastersCullingInfos.splitBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ShadowCastersCullingInfos-splitBuffer.html). An entry with [LightShadowCasterCullingInfo.splitRange](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.LightShadowCasterCullingInfo-splitRange.html) set to (0,0) will cause shadow casters culling and shadow maps rendering to be skipped for this light.
* * *
