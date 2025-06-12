* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CullingOptions.ShadowCasters.html

#  [CullingOptions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CullingOptions.html).ShadowCasters
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
When this flag is set, Unity culls shadow casters as part of the culling operation.
Default value: set, if your project uses the Scriptable Render Pipeline.  
  
If your project uses the Built-in Render Pipeline, this value is unset if [QualitySettings.shadows](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings-shadows.html) is set to [ShadowQuality.Disable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShadowQuality.Disable.html); otherwise, it is set. Note that changing this value has no effect in the Built-in Render Pipeline.  
  
Additional resources: [ScriptableCullingParameters.cullingOptions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ScriptableCullingParameters-cullingOptions.html), [ScriptableRenderContext.Cull](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ScriptableRenderContext.Cull.html), [CullingResults](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CullingResults.html).
* * *
