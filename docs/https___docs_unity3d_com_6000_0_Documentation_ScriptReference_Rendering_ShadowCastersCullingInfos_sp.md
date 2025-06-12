* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ShadowCastersCullingInfos-splitBuffer.html

#  [ShadowCastersCullingInfos](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ShadowCastersCullingInfos.html).splitBuffer
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
splitBuffer; 
### Description
An array that works as a buffer to store all the [ShadowSplitData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ShadowSplitData.html) structs you want to use for shadow casters culling.
This buffer is referred to by the [LightShadowCasterCullingInfo.splitRange](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.LightShadowCasterCullingInfo-splitRange.html) of each [LightShadowCasterCullingInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.LightShadowCasterCullingInfo.html) in [ShadowCastersCullingInfos.perLightInfos](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ShadowCastersCullingInfos-perLightInfos.html).
* * *
