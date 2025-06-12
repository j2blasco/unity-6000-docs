* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CameraEvent.html

# CameraEvent
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
Defines a place in camera's rendering to attach [CommandBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.html) objects to.
Unity's rendering loop can be extended by adding so called "command buffers" at various points in camera rendering. For example, you could add some custom geometry to be drawn right after the skybox is drawn.  
  
Additional resources: [CommandBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.html), [LightEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.LightEvent.html), [command buffers overview](https://docs.unity3d.com/6000.0/Documentation/Manual/GraphicsCommandBuffers.html).
### Properties
Property | Description  
---|---  
[BeforeDepthTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CameraEvent.BeforeDepthTexture.html) | Before camera's depth texture is generated.  
[AfterDepthTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CameraEvent.AfterDepthTexture.html) | After camera's depth texture is generated.  
[BeforeDepthNormalsTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CameraEvent.BeforeDepthNormalsTexture.html) | Before camera's depth+normals texture is generated.  
[AfterDepthNormalsTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CameraEvent.AfterDepthNormalsTexture.html) | After camera's depth+normals texture is generated.  
[BeforeGBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CameraEvent.BeforeGBuffer.html) | Before deferred rendering G-buffer is rendered.  
[AfterGBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CameraEvent.AfterGBuffer.html) | After deferred rendering G-buffer is rendered.  
[BeforeLighting](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CameraEvent.BeforeLighting.html) | Before lighting pass in deferred rendering.  
[AfterLighting](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CameraEvent.AfterLighting.html) | After lighting pass in deferred rendering.  
[BeforeFinalPass](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CameraEvent.BeforeFinalPass.html) | Before final geometry pass in deferred lighting.  
[AfterFinalPass](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CameraEvent.AfterFinalPass.html) | After final geometry pass in deferred lighting.  
[BeforeForwardOpaque](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CameraEvent.BeforeForwardOpaque.html) | Before opaque objects in forward rendering.  
[AfterForwardOpaque](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CameraEvent.AfterForwardOpaque.html) | After opaque objects in forward rendering.  
[BeforeImageEffectsOpaque](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CameraEvent.BeforeImageEffectsOpaque.html) | Before image effects that happen between opaque & transparent objects.  
[AfterImageEffectsOpaque](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CameraEvent.AfterImageEffectsOpaque.html) | After image effects that happen between opaque & transparent objects.  
[BeforeSkybox](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CameraEvent.BeforeSkybox.html) | Before skybox is drawn.  
[AfterSkybox](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CameraEvent.AfterSkybox.html) | After skybox is drawn.  
[BeforeForwardAlpha](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CameraEvent.BeforeForwardAlpha.html) | Before transparent objects in forward rendering.  
[AfterForwardAlpha](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CameraEvent.AfterForwardAlpha.html) | After transparent objects in forward rendering.  
[BeforeImageEffects](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CameraEvent.BeforeImageEffects.html) | Before image effects.  
[AfterImageEffects](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CameraEvent.AfterImageEffects.html) | After image effects.  
[AfterEverything](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CameraEvent.AfterEverything.html) | After camera has done rendering everything.  
[BeforeReflections](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CameraEvent.BeforeReflections.html) | Before reflections pass in deferred rendering.  
[AfterReflections](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CameraEvent.AfterReflections.html) | After reflections pass in deferred rendering.  
[BeforeHaloAndLensFlares](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CameraEvent.BeforeHaloAndLensFlares.html) | Before halo and lens flares.  
[AfterHaloAndLensFlares](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CameraEvent.AfterHaloAndLensFlares.html) | After halo and lens flares.  
* * *
