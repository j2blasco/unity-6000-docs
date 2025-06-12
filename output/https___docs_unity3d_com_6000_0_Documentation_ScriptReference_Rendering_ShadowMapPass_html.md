* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ShadowMapPass.html

# ShadowMapPass
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
Allows precise control over which shadow map passes to execute [CommandBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.html) objects attached using [Light.AddCommandBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light.AddCommandBuffer.html).
These flags only take effect when used with Rendering.LightEvent/BeforeShadowMapPass or Rendering.LightEvent/AfterShadowMapPass.
### Properties
Property | Description  
---|---  
[PointlightPositiveX](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ShadowMapPass.PointlightPositiveX.html) | +X point light shadow cubemap face.  
[PointlightNegativeX](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ShadowMapPass.PointlightNegativeX.html) | -X point light shadow cubemap face.  
[PointlightPositiveY](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ShadowMapPass.PointlightPositiveY.html) | +Y point light shadow cubemap face.  
[PointlightNegativeY](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ShadowMapPass.PointlightNegativeY.html) | -Y point light shadow cubemap face.  
[PointlightPositiveZ](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ShadowMapPass.PointlightPositiveZ.html) | +Z point light shadow cubemap face.  
[PointlightNegativeZ](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ShadowMapPass.PointlightNegativeZ.html) | -Z point light shadow cubemap face.  
[DirectionalCascade0](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ShadowMapPass.DirectionalCascade0.html) | First directional shadow map cascade.  
[DirectionalCascade1](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ShadowMapPass.DirectionalCascade1.html) | Second directional shadow map cascade.  
[DirectionalCascade2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ShadowMapPass.DirectionalCascade2.html) | Third directional shadow map cascade.  
[DirectionalCascade3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ShadowMapPass.DirectionalCascade3.html) | Fourth directional shadow map cascade.  
[Spotlight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ShadowMapPass.Spotlight.html) | Spot light shadow pass.  
[AreaLight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ShadowMapPass.AreaLight.html) | Area light shadow pass.  
[Pointlight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ShadowMapPass.Pointlight.html) | All point light shadow passes.  
[Directional](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ShadowMapPass.Directional.html) | All directional shadow map passes.  
[All](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ShadowMapPass.All.html) | All shadow map passes.  
* * *
