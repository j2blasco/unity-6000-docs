* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/post-processing-effect-availability-reference.html

  * [Rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/rendering-and-post-processing.html)
  * [Post-processing and full-screen effects](https://docs.unity3d.com/6000.0/Documentation/Manual/post-processing-and-full-screen-effects.html)
  * Post-processing effect availability reference


[](https://docs.unity3d.com/6000.0/Documentation/Manual/PostProcessingOverview.html)
Introduction to post-processing
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/post-processing-and-full-screen-effects-urp.html)
Post-processing and full-screen effects in URP
# Post-processing effect availability reference
This table contains information on which **post-processing** A process that improves product visuals by applying filters and effects before the image appears on screen. You can use post-processing effects to simulate physical camera and film properties, for example Bloom and Depth of Field. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/PostProcessingOverview.html) post processing, postprocessing, postprocess  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#post-processing) effects and full-screen effects are available in Unity’s different post-processing solutions, how to find those effects, and what other effects you can use to achieve a similar result.
In previous versions of Unity, you applied all post-processing effects and full-screen effects in the same way; by adding components to a **Camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera). In more recent versions of Unity, you can apply these effects in different ways.
**Note** : Unity implements effects differently depending on the **render pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Renderpipeline) you are using. This means that effects vary in terms of performance, appearance, and configuration between packages.
## Post-processing effects and pipeline support
**Effect Name** | **Description** | **Available in URP integrated solution?** | **Available in HDRP integrated solution?** | **Available in PPv2 package?**  
---|---|---|---|---  
Ambient Occlusion | The **Ambient Occlusion** effect darkens the areas in your scene that are not exposed to ambient lighting. | Yes   
  
See [Universal Render Pipeline: Ambient Occlusion ](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/post-processing-ssao.html)   
  
You can also apply Ambient Occlusion as part of your baked lighting. For more information, see [Baked Ambient Occlusion](https://docs.unity3d.com/6000.0/Documentation/Manual/LightingBakedAmbientOcclusion.html) | Yes   
  
Choose from [SSAO](https://docs.unity3d.com/Packages/com.unity.render-pipelines.high-definition@9.0/manual/Override-Ambient-Occlusion.html) using a Volume Override, or [Ray-Traced Ambient Occlusion](https://docs.unity3d.com/Packages/com.unity.render-pipelines.high-definition@latest?subfolder=/manual/Ray-Traced-Ambient-Occlusion.html?q=ambientocclusion)   
  
You can also apply [per-Material Ambient Occlusion](https://docs.unity3d.com/Packages/com.unity.render-pipelines.high-definition@latest?subfolder=/manual/Ambient-Occlusion.html?q=ambient)   
  
You can also apply Ambient Occlusion as part of your baked lighting. For more information, see [Baked Ambient Occlusion](https://docs.unity3d.com/Manual/LightingBakedAmbientOcclusion.html) | Yes   
  
See[ Post Processing: Ambient Occlusion](https://docs.unity3d.com/Packages/com.unity.postprocessing@latest?subfolder=/manual/Ambient-Occlusion.html)   
You can also apply Ambient Occlusion as part of your baked lighting. For more information, see [Baked Ambient Occlusion](https://docs.unity3d.com/Manual/LightingBakedAmbientOcclusion)  
Anti-aliasing | The **Anti-aliasing** effect softens the appearance of edges in your scene.   
Depending on your render pipeline, you can use MSAA (hardware anti-aliasing), or FXAA, SMAA, or TAA (anti-aliasing post-processing effects) | Yes   
  
FXAA and SMAA can be enabled in the [Camera ](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/camera-component-reference.html#rendering)component   
  
You can also configure MSAA (hardware anti-aliasing) in [Quality Settings](https://docs.unity3d.com/Manual/class-QualitySettings.html) | Yes   
  
FXAA, SMAA, and TAA are implemented in **Project Settings > Frame Settings > HDRP Default Settings**; see [Anti-aliasing in the High Definition Render Pipeline](https://docs.unity3d.com/Packages/com.unity.render-pipelines.high-definition@latest?subfolder=/manual/Anti-Aliasing.html?q=ANTI)  
  
You can also configure MSAA (hardware anti-aliasing) in the HDRP Asset - see [Anti-aliasing in the High Definition Render Pipeline](https://docs.unity3d.com/Packages/com.unity.render-pipelines.high-definition@latest?subfolder=/manual/Anti-Aliasing.html?q=ANTI). | Yes   
  
For FXAA, SMAA, and TAA, see [Post Processing: Anti-aliasing](https://docs.unity3d.com/Packages/com.unity.postprocessing@latest?subfolder=/manual/Anti-aliasing.html)   
  
You can also configure MSAA (hardware anti-aliasing) in [Quality Settings](https://docs.unity3d.com/Manual/class-QualitySettings.html)  
Auto Exposure | The **Auto Exposure** effect dynamically adjusts the exposure of an image to match its mid-tone. | No | Yes   
  
In [High Definition Render Pipeline: Exposure Volume Override](https://docs.unity3d.com/Packages/com.unity.render-pipelines.high-definition@latest?subfolder=/manual/Override-Exposure.html), when **Mode** is set to **Automatic** | Yes   
  
See [Post Processing:Auto Exposure](https://docs.unity3d.com/Packages/com.unity.postprocessing@latest?subfolder=/manual/Auto-Exposure.html)  
Bloom | The **Bloom** effect makes bright areas in your image glow. Note that Bloom works differently in each package, and requires different settings; read the documentation for a given package for more information. | Yes   
  
See [Universal Render Pipeline: Bloom](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/post-processing-bloom.html) | Yes   
  
See [High Definition Render Pipeline: Bloom](https://docs.unity3d.com/Packages/com.unity.render-pipelines.high-definition@latest?subfolder=/manual/Post-Processing-Bloom.html) | Yes  
  
See [Post Processing: Bloom](https://docs.unity3d.com/Packages/com.unity.postprocessing@latest?subfolder=/manual/Bloom.html)  
Channel Mixer | The **Channel mixer** lets you adjust the balance of each input color. | Yes  
  
See [Universal Render Pipeline: Channel Mixer](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/Post-Processing-Channel-Mixer.html) | Yes  
  
See [High Definition Render Pipeline: Channel Mixer](https://docs.unity3d.com/Packages/com.unity.render-pipelines.high-definition@latest?subfolder=/manual/Post-Processing-Channel-Mixer.html) | Yes  
  
See **Channel Mixer** [in Post Processing: Color Grading ](https://docs.unity3d.com/Packages/com.unity.postprocessing@latest?subfolder=/manual/Color-Grading.html)  
Chromatic Aberration | The **Chromatic Aberration** effect disperses colors along the boundaries between dark and light areas of the image. | Yes  
  
See [Universal Render Pipeline: Chromatic Aberration](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/post-processing-chromatic-aberration.html) | Yes  
  
See [High Definition Render Pipeline: Chromatic Aberration](https://docs.unity3d.com/Packages/com.unity.render-pipelines.high-definition@latest?subfolder=/manual/Post-Processing-Chromatic-Aberration.html) | Yes  
  
See [Post Processing: Chromatic Aberration](https://docs.unity3d.com/Packages/com.unity.postprocessing@latest?subfolder=/manual/Chromatic-Aberration.html)  
Color Adjustments | The **Color Adjustments** effect lets you change the overall tone, brightness, and contrast of the final rendered image. | Yes  
  
See[ Universal Render Pipeline: Color Adjustments](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/Post-Processing-Color-Adjustments.html) | Yes  
  
See [High Definition Render Pipeline: Color Adjustments](https://docs.unity3d.com/Packages/com.unity.render-pipelines.high-definition@latest?subfolder=/manual/Post-Processing-Color-Adjustments.html) | Yes  
  
See **Tone** in [Post Processing: Color Grading](https://docs.unity3d.com/Packages/com.unity.postprocessing@latest?subfolder=/manual/Color-Grading.html)  
Color Curves | The **Color Curves** effect lets you adjust specific ranges in hue, saturation, or luminosity. | Yes  
  
See [Universal Render Pipeline: Color Curves](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/Post-Processing-Color-Curves.html) | Yes  
  
See [High Definition Render Pipeline: Color Curves](https://docs.unity3d.com/Packages/com.unity.render-pipelines.high-definition@latest?subfolder=/manual/Post-Processing-Color-Curves.html) | Yes  
  
See **Grading Curves** in [Post Processing: Color Grading](https://docs.unity3d.com/Packages/com.unity.postprocessing@latest?subfolder=/manual/Color-Grading.html)  
Fog | The **Fog** effect simulates the look of fog or mist in outdoor environments. | No | Yes  
  
See [High Definition Render Pipeline: Fog Volume Override](https://docs.unity3d.com/Packages/com.unity.render-pipelines.high-definition@latest?subfolder=/manual/Override-Fog.html?q=fog) (note that this is not implemented as a full-screen effect or post-processing effect) | Yes  
  
See [Post Processing: Deferred Fog](https://docs.unity3d.com/Packages/com.unity.postprocessing@latest?subfolder=/manual/Deferred-Fog.html)  
Depth of Field | The **Depth of Field** effect blurs the background of your image while the objects in the foreground stay in focus. | Yes  
  
See [Universal Render Pipeline: Depth of Field ](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/depth-of-field-urp.html) | Yes  
  
See [High Definition Render Pipeline: Depth of Field](https://docs.unity3d.com/Packages/com.unity.render-pipelines.high-definition@latest?subfolder=/manual/Post-Processing-Depth-of-Field.html) | Yes  
  
See [Post Processing: Depth of Field](https://docs.unity3d.com/Packages/com.unity.postprocessing@latest?subfolder=/manual/Depth-of-Field.html)  
Grain | The **Grain** effect overlays film noise onto your image. | Yes  
  
See [Universal Render Pipeline: Film Grain](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/Post-Processing-Film-Grain.html) | Yes  
  
See [High Definition Render Pipeline: Film Grain](https://docs.unity3d.com/Packages/com.unity.render-pipelines.high-definition@latest?subfolder=/manual/Post-Processing-Film-Grain.html) | Yes  
  
See[ Post Processing: Grain](https://docs.unity3d.com/Packages/com.unity.postprocessing@2.3/manual/Grain.html)  
Lens Distortion | The **Lens Distortion** effect simulates distortion caused by the shape of a real-world camera lens. | Yes  
  
See [Universal Render Pipeline: Lens Distortion](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/Post-Processing-Lens-Distortion.html) | Yes  
  
See [High Definition Render Pipeline: Lens Distortion](https://docs.unity3d.com/Packages/com.unity.render-pipelines.high-definition@9.0/manual/Post-Processing-Lens-Distortion.html) | Yes   
  
See [Post Processing: Lens Distortion](https://docs.unity3d.com/Packages/com.unity.postprocessing@latest?subfolder=/manual/Lens-Distortion)  
Lift, Gamma, Gain | The **Lift, Gamma, Gain** effect allows you to perform three-way color grading. | Yes   
  
See [Universal Render Pipeline: Lift, Gamma, Gain](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/Post-Processing-Lift-Gamma-Gain.html) | Yes   
  
See [High Definition Render Pipeline: Lift, Gamma, Gain](https://docs.unity3d.com/Packages/com.unity.render-pipelines.high-definition@latest?subfolder=/manual/Post-Processing-Lift-Gamma-Gain.html) | Yes  
  
See **Trackballs** in [Post Processing: Color Grading](https://docs.unity3d.com/Packages/com.unity.postprocessing@latest?subfolder=/manual/Color-Grading.html)  
Motion Blur | The **Motion Blur** effect blurs the image in the direction of the **camera’s** movement | Yes   
  
See [Universal Render Pipeline: Motion Blur](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/Post-Processing-Motion-Blur.html) | Yes  
  
See [High Definition Render Pipeline: Motion Blur](https://docs.unity3d.com/Packages/com.unity.render-pipelines.high-definition@latest?subfolder=/manual/Post-Processing-Motion-Blur.html) | Yes  
  
See [Post Processing: Motion Blur](https://docs.unity3d.com/Packages/com.unity.postprocessing@latest?subfolder=/manual/Motion-Blur.html)  
Panini Projection | The **Panini Projection** effect corrects distortion at the edge of an image caused by a wide field of view. | Yes   
  
See [Universal Render Pipeline: Panini Projection](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/Post-Processing-Panini-Projection.html) | Yes   
  
See [High Definition Render Pipeline: Panini Projection](https://docs.unity3d.com/Packages/com.unity.render-pipelines.high-definition@latest?subfolder=/manual/Post-Processing-Panini-Projection.html) | No  
Screen Space Reflection | The **Screen Space Reflection** effect creates subtle reflections that simulate wet floor surfaces or puddles. | No | Yes   
  
See [High Definition Render Pipeline: Screen Space Reflection](https://docs.unity3d.com/Packages/com.unity.render-pipelines.high-definition@latest?subfolder=/manual/Override-Screen-Space-Reflection.html?q=screenspace) | Yes  
  
See [Post Processing: Screen Space Reflection](https://docs.unity3d.com/Packages/com.unity.postprocessing@latest?subfolder=/manual/Screen-Space-Reflections.html)  
Shadows Midtones Highlights | The **Shadows Midtones Highlights** effect separately controls the tint and brightness of the shadows, midtones, and highlights in your image | Yes  
  
See [Universal Render Pipeline: Shadows, Midtones, Highlights](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/Post-Processing-Shadows-Midtones-Highlights.html) | Yes  
  
See [High Definition Render Pipeline: Shadows Midtones Highlights](https://docs.unity3d.com/Packages/com.unity.render-pipelines.high-definition@latest?subfolder=/manual/Post-Processing-Shadows-Midtones-Highlights.html) | No  
Split Toning | The **Split Toning** effect maps two different tones in your image to two specific colors. | Yes   
  
See [Universal Render Pipeline: Split Toning](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/Post-Processing-Split-Toning.html) | Yes  
  
See [High Definition Render Pipeline: Split Toning](https://docs.unity3d.com/Packages/com.unity.render-pipelines.high-definition@9.0/manual/Post-Processing-Split-Toning.html) | No  
Tonemapping | The **Tonemapping** effect remaps the values of an image to high dynamic range (HDR) colors | Yes  
  
See [Universal Render Pipeline: Tonemapping](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/post-processing-tonemapping.html) | Yes  
  
See [High Definition Render Pipeline: Tonemapping](https://docs.unity3d.com/Packages/com.unity.render-pipelines.high-definition@latest?subfolder=/manual/Post-Processing-Tonemapping.html) | Yes  
  
See **Tonemapping** in [Post Processing: Color Grading](https://docs.unity3d.com/Packages/com.unity.postprocessing@latest?subfolder=/manual/Color-Grading)  
Vignette | The **Vignette** effect darkens the edges of an image | Yes  
  
See [Universal Render Pipeline: Vignette](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/post-processing-vignette.html) | Yes  
  
See[ High Definition Render Pipeline:Vignette](https://docs.unity3d.com/Packages/com.unity.render-pipelines.high-definition@latest?subfolder=/manual/Post-Processing-Vignette.html) | Yes  
  
See [Post Processing: Vignette](https://docs.unity3d.com/Packages/com.unity.postprocessing@latest?subfolder=/manual/Vignette.html)  
White Balance | The **White Balance** effect preserves the white areas in your image and balances other tones around the white areas | Yes  
  
See[ Universal Render Pipeline: White Balance](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/Post-Processing-White-Balance.html) | Yes  
  
See [High Definition Render Pipeline: White Balance](https://docs.unity3d.com/Packages/com.unity.render-pipelines.high-definition@latest?subfolder=/manual/Post-Processing-White-Balance.html) | Yes  
  
**See White balance** in [Post Processing: Color Grading](https://docs.unity3d.com/Packages/com.unity.postprocessing@latest?subfolder=/manual/Color-Grading.html)  
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/PostProcessingOverview.html)
Introduction to post-processing
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/post-processing-and-full-screen-effects-urp.html)
Post-processing and full-screen effects in URP
