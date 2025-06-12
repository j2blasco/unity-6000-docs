* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ScriptableRenderContext.CullShadowCasters.html

#  [ScriptableRenderContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ScriptableRenderContext.html).CullShadowCasters
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
public void CullShadowCasters([Rendering.CullingResults](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CullingResults.html) cullingResults, [Rendering.ShadowCastersCullingInfos](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ShadowCastersCullingInfos.html) infos); 
### Parameters
Parameter | Description  
---|---  
cullingResults | Culling results to use.  
infos | Shadow casters culling information.  
### Description
Performs shadow casters culling for all the visible lights.
This function schedules the shadow casters culling jobs. It is recommended to call this function as early as possible so that there is more room for the culling jobs to execute in the background. If you call this function, the fields Rendering.ShadowDrawingSettings.splitData and Rendering.ShadowDrawingSettings.projectionType are ignored by Unity. Those fields are already provided via [ShadowCastersCullingInfos](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ShadowCastersCullingInfos.html) and then stored internally so that Unity can reuse them as needed.
* * *
