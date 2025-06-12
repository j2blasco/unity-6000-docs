* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.LightEvent.AfterShadowMapPass.html

#  [LightEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.LightEvent.html).AfterShadowMapPass
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
After shadowmap pass is rendered.
When this event is triggered, all shadow casters in pass have already been rendered, and current render target is still the shadowmap.  
  
This event differs from [LightEvent.AfterShadowMap](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.LightEvent.AfterShadowMap.html) in that for light types that render shadows using multiple passes, the event triggers after each pass. Additional control over when this event triggers can be achieved by passing a [ShadowMapPass](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ShadowMapPass.html) mask to [Light.AddCommandBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light.AddCommandBuffer.html).
* * *
