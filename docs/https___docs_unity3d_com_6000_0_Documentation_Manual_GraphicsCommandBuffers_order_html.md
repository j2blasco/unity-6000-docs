* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/GraphicsCommandBuffers-order.html

  * [Rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/rendering-and-post-processing.html)
  * [Render pipelines](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)
  * [Using the Built-In Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/built-in-render-pipeline.html)
  * [Custom rendering in the Built-In Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/GraphicsCommandBuffers-landing.html)
  * CameraEvent and LightEvent events order reference for the Built-In Render Pipeline


[](https://docs.unity3d.com/6000.0/Documentation/Manual/GraphicsCommandBuffers.html)
CommandBuffer fundamentals in the Built-In Render Pipeline
[](https://docs.unity3d.com/6000.0/Documentation/Manual/post-processing-and-full-screen-effects.html)
Post-processing and full-screen effects
# CameraEvent and LightEvent events order reference for the Built-In Render Pipeline
## CameraEvent
The order of execution for CameraEvents depends on the [rendering path](https://docs.unity3d.com/6000.0/Documentation/Manual/RenderingPaths.html)The technique that a render pipeline uses to render graphics. Choosing a different rendering path affects how lighting and shading are calculated. Some rendering paths are more suited to different platforms and hardware than others. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/RenderingPaths.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#RenderingPath) that your Project uses.
### Deferred rendering path
  * [BeforeGBuffer](https://docs.unity3d.com/ScriptReference/Rendering.CameraEvent.BeforeGBuffer.html): Unity renders opaque geometry
  * [AfterGBuffer](https://docs.unity3d.com/ScriptReference/Rendering.CameraEvent.AfterGBuffer.html): Unity resolves depth.
  * [BeforeReflections](https://docs.unity3d.com/ScriptReference/Rendering.CameraEvent.BeforeReflections.html): Unity renders default reflections, and **Reflection Probe** A rendering component that captures a spherical view of its surroundings in all directions, rather like a camera. The captured image is then stored as a Cubemap that can be used by objects with reflective materials. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ReflectionProbe.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#ReflectionProbe) reflections.
  * [AfterReflections](https://docs.unity3d.com/ScriptReference/Rendering.CameraEvent.AfterReflections.html): Unity copies reflections to the Emissive channel of the G-buffer.
  * [BeforeLighting](https://docs.unity3d.com/ScriptReference/Rendering.CameraEvent.BeforeLighting.html): Unity renders shadows. See [LightEvent order of execution](https://docs.unity3d.com/6000.0/Documentation/Manual/GraphicsCommandBuffers-order.html#LightEvent).
  * [AfterLighting](https://docs.unity3d.com/ScriptReference/Rendering.CameraEvent.AfterLighting.html)
  * [BeforeFinalPass](https://docs.unity3d.com/ScriptReference/Rendering.CameraEvent.BeforeFinalPass.html): Unity processes the final pass.
  * [AfterFinalPass](https://docs.unity3d.com/ScriptReference/Rendering.CameraEvent.AfterFinalPass.html)
  * [BeforeForwardOpaque](https://docs.unity3d.com/ScriptReference/Rendering.CameraEvent.BeforeForwardOpaque.html) (only called if there is opaque geometry that cannot be rendered using deferred): Unity renders opaque geometry that cannot be rendered with deferred rendering.
  * [AfterForwardOpaque](https://docs.unity3d.com/ScriptReference/Rendering.CameraEvent.AfterForwardOpaque.html) (only called if there is opaque geometry that cannot be rendered using deferred)
  * [BeforeSkybox](https://docs.unity3d.com/ScriptReference/Rendering.CameraEvent.BeforeSkybox.html): Unity renders the **skybox** A special type of Material used to represent skies. Usually six-sided. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/sky-landing.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Skybox).
  * [AfterSkybox](https://docs.unity3d.com/ScriptReference/Rendering.CameraEvent.AfterSkybox.html): Unity renders halos.
  * [BeforeImageEffectsOpaque](https://docs.unity3d.com/ScriptReference/Rendering.CameraEvent.BeforeImageEffectsOpaque.html): Unity applies opaque-only **post-processing** A process that improves product visuals by applying filters and effects before the image appears on screen. You can use post-processing effects to simulate physical camera and film properties, for example Bloom and Depth of Field. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/PostProcessingOverview.html) post processing, postprocessing, postprocess  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#post-processing) effects.
  * [AfterImageEffectsOpaque](https://docs.unity3d.com/ScriptReference/Rendering.CameraEvent.AfterImageEffectsOpaque.html)
  * [BeforeForwardAlpha](https://docs.unity3d.com/ScriptReference/Rendering.CameraEvent.BeforeForwardAlpha.html): Unity renders transparent geometry, and UI Canvases with a Rendering Mode of **Screen Space -**Camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera)**.
  * [AfterForwardAlpha](https://docs.unity3d.com/ScriptReference/Rendering.CameraEvent.AfterForwardAlpha.html): [BeforeHaloAndLensFlares](https://docs.unity3d.com/ScriptReference/Rendering.CameraEvent.BeforeHaloAndLensFlares.html): Unity renders **lens flares** A component that simulates the effect of lights refracting inside a camera lens. Use a Lens Flare to represent very bright lights or add atmosphere to your scene. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LensFlare.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#LensFlare).
  * [AfterHaloAndLensFlares](https://docs.unity3d.com/ScriptReference/Rendering.CameraEvent.AfterHaloAndLensFlares.html)
  * [BeforeImageEffects](https://docs.unity3d.com/ScriptReference/Rendering.CameraEvent.BeforeImageEffects.html): Unity applies post-processing effects.
  * [AfterImageEffects](https://docs.unity3d.com/ScriptReference/Rendering.CameraEvent.AfterImageEffects.html)
  * [AfterEverything](https://docs.unity3d.com/ScriptReference/Rendering.CameraEvent.AfterEverything.html): Unity renders UI Canvases with a Rendering Mode that is not **Screen Space - Camera**.


### Forward rendering path
  * [BeforeDepthTexture](https://docs.unity3d.com/ScriptReference/Rendering.CameraEvent.BeforeDepthTexture.html): Unity renders depth for opaque geometry.
  * [AfterDepthTexture](https://docs.unity3d.com/ScriptReference/Rendering.CameraEvent.AfterDepthTexture.html)
  * [BeforeDepthNormalsTexture](https://docs.unity3d.com/ScriptReference/Rendering.CameraEvent.BeforeDepthNormalsTexture.html): Unity renders depth normals for opaque geometry.
  * [AfterDepthNormalsTexture](https://docs.unity3d.com/ScriptReference/Rendering.CameraEvent.AfterDepthNormalsTexture.html): Unity renders shadows. See [LightEvent order of execution](https://docs.unity3d.com/6000.0/Documentation/Manual/GraphicsCommandBuffers-order.html#LightEvent).
  * [BeforeForwardOpaque](https://docs.unity3d.com/ScriptReference/Rendering.CameraEvent.BeforeForwardOpaque.html): Unity renders opaque geometry.
  * [AfterForwardOpaque](https://docs.unity3d.com/ScriptReference/Rendering.CameraEvent.AfterForwardOpaque.html)
  * [BeforeSkybox](https://docs.unity3d.com/ScriptReference/Rendering.CameraEvent.BeforeSkybox.html): Unity renders the skybox.
  * [AfterSkybox](https://docs.unity3d.com/ScriptReference/Rendering.CameraEvent.AfterSkybox.html): Unity renders halos.
  * [BeforeImageEffectsOpaque](https://docs.unity3d.com/ScriptReference/Rendering.CameraEvent.BeforeImageEffectsOpaque.html): Unity applies opaque-only post-processing effects.
  * [AfterImageEffectsOpaque](https://docs.unity3d.com/ScriptReference/Rendering.CameraEvent.AfterImageEffectsOpaque.html)
  * [BeforeForwardAlpha](https://docs.unity3d.com/ScriptReference/Rendering.CameraEvent.BeforeForwardAlpha.html): Unity renders transparent geometry, and UI Canvases with a Rendering Mode of **Screen Space - Camera**.
  * [AfterForwardAlpha](https://docs.unity3d.com/ScriptReference/Rendering.CameraEvent.AfterForwardAlpha.html)
  * [BeforeHaloAndLensFlares](https://docs.unity3d.com/ScriptReference/Rendering.CameraEvent.BeforeHaloAndLensFlares.html): Unity renders lens flares.
  * [AfterHaloAndLensFlares](https://docs.unity3d.com/ScriptReference/Rendering.CameraEvent.AfterHaloAndLensFlares.html)
  * [BeforeImageEffects](https://docs.unity3d.com/ScriptReference/Rendering.CameraEvent.BeforeImageEffects.html): Unity applies post-processing effects.
  * [AfterImageEffects](https://docs.unity3d.com/ScriptReference/Rendering.CameraEvent.AfterImageEffects.html)
  * [AfterEverything](https://docs.unity3d.com/ScriptReference/Rendering.CameraEvent.AfterEverything.html): Unity renders UI Canvases with a Rendering Mode that is not **Screen Space - Camera**.


## LightEvent order of execution
During the “render shadows” stage above, for each shadow-casting Light, Unity performs these steps:
  * [BeforeShadowMap](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.LightEvent.BeforeShadowMap.html)
  * [BeforeShadowMapPass](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.LightEvent.BeforeShadowMapPass.html): Unity renders all shadow casters for the current Pass
  * [AfterShadowMapPass](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.LightEvent.AfterShadowMapPass.html): Unity repeats the last three steps, for each Pass
  * [AfterShadowMap](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.LightEvent.AfterShadowMap.html)
  * [BeforeScreenSpaceMask](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.LightEvent.BeforeScreenSpaceMask.html): Unity gathers the shadow map into a screen space buffer and performs filtering
  * [AfterScreenSpaceMask](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.LightEvent.AfterScreenSpaceMask.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/GraphicsCommandBuffers.html)
CommandBuffer fundamentals in the Built-In Render Pipeline
[](https://docs.unity3d.com/6000.0/Documentation/Manual/post-processing-and-full-screen-effects.html)
Post-processing and full-screen effects
