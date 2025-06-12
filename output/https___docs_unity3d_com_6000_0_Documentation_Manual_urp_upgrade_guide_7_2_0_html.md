* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/urp/upgrade-guide-7-2-0.html

  * [Rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/rendering-and-post-processing.html)
  * [Render pipelines](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)
  * [Using the Universal Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/universal-render-pipeline.html)
  * [Get started with URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/introduction-landing.html)
  * [Installing and upgrading URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/InstallingAndConfiguringURP.html)
  * [Upgrade URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/upgrade-guides.html)
  * Upgrade to version 7.2.0 of the Universal Render Pipeline


[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/upgrade-guide-7-3-0.html)
Upgrade to version 7.3.0 of the Universal Render Pipeline
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/upgrade-lwrp-to-urp.html)
Upgrade from the Lightweight Render Pipeline to the Universal Render Pipeline
# Upgrade to version 7.2.0 of the Universal Render Pipeline
On this page, you will find information about upgrading from an older version of the Universal **Render Pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Renderpipeline) (URP) to the current version.
## Building your Project for consoles
To build a Project for a console, you need to install an additional package for each platform you want to support.
## Require Depth Texture
In previous versions of URP, if **post-processing** A process that improves product visuals by applying filters and effects before the image appears on screen. You can use post-processing effects to simulate physical camera and film properties, for example Bloom and Depth of Field. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/PostProcessingOverview.html) post processing, postprocessing, postprocess  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#post-processing) was enabled it would cause the pipeline to always require depth. We have improved the post-processing integration to only require depth from the pipeline when **Depth of Field** A post-processing effect that simulates the focus properties of a camera lens. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/PostProcessingOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#DepthofField), Motion Blur or SMAA effects are enabled. This improves performance in many cases.
Because **Cameras** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera) that use post-processing no longer require depth by default, you must now manually indicate that Cameras require depth if you are using it for other effects, such as **soft particles** Particles that create semi-transparent effects like smoke, fog or fire. Soft particles fade out as they approach an opaque object, to prevent intersections with the geometry. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-StandardParticleShaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#SoftParticles).
To make all Cameras require depth, enable the the `Depth Texture` option in the [Pipeline Asset](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/universalrp-asset.html). To make an individual Camera require depth, set `Depth Texture` option to `On` in the [Camera Inspector](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/camera-component-reference.html).
## Sampling shadows from the Main Light
In previous versions of URP, if shadow cascades were enabled for the main Light, shadows would be resolved in a screen space pass. The pipeline now always resolves shadows while rendering opaque or transparent objects. This allows for consistency and solved many issues regarding shadows.
If have custom HLSL **shaders** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) and sample `_ScreenSpaceShadowmapTexture` texture, you must upgrade them to sample shadows by using the `GetMainLight` function instead.
For example:
```
float4 shadowCoord = TransformWorldToShadowCoord(positionWorldSpace);
Light mainLight = GetMainLight(inputData.shadowCoord);

// now you can use shadow to apply realtime occlusion
half shadow = mainLight.shadowAttenuation;

```

You must also define the following in your .shader file to make sure your custom shader can receive shadows correctly:
```
#pragma multi_compile _ _MAIN_LIGHT_SHADOWS
#pragma multi_compile _ _MAIN_LIGHT_SHADOWS_CASCADE

```

## Transparent receiving shadows
Transparent objects can now receive shadows when using shadow cascades. You can also optionally disable shadow receiving for transparent to improve performance. To do so, disable `Transparent Receive Shadows` in the Forward Renderer asset.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/upgrade-guide-7-3-0.html)
Upgrade to version 7.3.0 of the Universal Render Pipeline
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/upgrade-lwrp-to-urp.html)
Upgrade from the Lightweight Render Pipeline to the Universal Render Pipeline
