* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.LightEvent.html

# LightEvent
enumeration
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
Defines a place in light's rendering to attach [CommandBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.html) objects to.
Unity's rendering loop can be extended by adding so called "command buffers" at various points in light rendering; mostly related to shadows. For example, you could do custom processing of the shadow map after it is rendered.  
  
Additional resources: [CommandBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.html), [CameraEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CameraEvent.html), [command buffers overview](https://docs.unity3d.com/6000.0/Documentation/Manual/GraphicsCommandBuffers.html).
### Properties
Property | Description  
---|---  
[BeforeShadowMap](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.LightEvent.BeforeShadowMap.html) | Before shadowmap is rendered.  
[AfterShadowMap](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.LightEvent.AfterShadowMap.html) | After shadowmap is rendered.  
[BeforeScreenspaceMask](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.LightEvent.BeforeScreenspaceMask.html) | Before directional light screenspace shadow mask is computed.  
[AfterScreenspaceMask](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.LightEvent.AfterScreenspaceMask.html) | After directional light screenspace shadow mask is computed.  
[BeforeShadowMapPass](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.LightEvent.BeforeShadowMapPass.html) | Before shadowmap pass is rendered.  
[AfterShadowMapPass](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.LightEvent.AfterShadowMapPass.html) | After shadowmap pass is rendered.  
* * *
