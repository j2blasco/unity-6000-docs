* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/urp/upgrade-guide-10-0-x.html

  * [Rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/rendering-and-post-processing.html)
  * [Render pipelines](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)
  * [Using the Universal Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/universal-render-pipeline.html)
  * [Get started with URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/introduction-landing.html)
  * [Installing and upgrading URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/InstallingAndConfiguringURP.html)
  * [Upgrade URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/upgrade-guides.html)
  * Upgrade to version 10.0.x of the Universal Render Pipeline


[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/upgrade-guide-10-1-x.html)
Upgrade to version 10.1.x of the Universal Render Pipeline
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/upgrade-guide-9-0-x.html)
Upgrade to version 9.0.x of the Universal Render Pipeline
# Upgrade to version 10.0.x of the Universal Render Pipeline
This page describes how to upgrade from an older version of the Universal **Render Pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Renderpipeline) (URP) to version 10.0.x.
## Upgrading from URP 7.2.x and later releases
  1. URP 10.x.x does not support the package **Post-Processing** A process that improves product visuals by applying filters and effects before the image appears on screen. You can use post-processing effects to simulate physical camera and film properties, for example Bloom and Depth of Field. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/PostProcessingOverview.html) post processing, postprocessing, postprocess  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#post-processing) Stack v2. If your Project uses the package Post-Processing Stack v2, migrate the effects that use that package first.


### DepthNormals Pass
Starting from version 10.0.x, URP can generate a normal texture called `_CameraNormalsTexture`. To render to this texture in your custom **shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader), add a Pass with the name `DepthNormals`. For an example, check the implementation in `Lit.shader`.
### Screen Space Ambient Occlusion (SSAO)
URP 10.0.x implements the Screen Space **Ambient Occlusion** A method to approximate how much ambient light (light not coming from a specific direction) can hit a point on a surface.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Ambientocclusion) (SSAO) effect.
If you intend to use the SSAO effect with your custom shaders, consider the following entities related to SSAO:
  * The `_SCREEN_SPACE_OCCLUSION` keyword.
  * `Input.hlsl` contains the new declaration `float2  normalizedScreenSpaceUV` in the `InputData` struct.
  * `Lighting.hlsl` contains the `AmbientOcclusionFactor` struct with the variables for calculating indirect and direct occlusion:
```
struct AmbientOcclusionFactor
{
    half indirectAmbientOcclusion;
    half directAmbientOcclusion;
};

```

  * `Lighting.hlsl` contains the following function for sampling the SSAO texture:
```
half SampleAmbientOcclusion(float2 normalizedScreenSpaceUV)

```

  * `Lighting.hlsl` contains the following function:
```
AmbientOcclusionFactor GetScreenSpaceAmbientOcclusion(float2
normalizedScreenSpaceUV)

```



To support SSAO in custom shader, add the `DepthNormals` Pass and the `_SCREEN_SPACE_OCCLUSION` keyword the the shader. For an example, check `Lit.shader`.
If your custom shader implements custom lighting functions, use the function `GetScreenSpaceAmbientOcclusion(float2 normalizedScreenSpaceUV)` to get the `AmbientOcclusionFactor` value for your lighting calculations.
## Upgrading from URP 7.0.x–7.1.x
  1. Upgrade to URP 7.2.0 first. Refer to [Upgrading to version 7.2.0 of the Universal Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/upgrade-guide-7-2-0.html).
  2. URP 8.x.x does not support the package Post-Processing Stack v2. If your Project uses the package Post-Processing Stack v2, migrate the effects that use that package first.


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/upgrade-guide-10-1-x.html)
Upgrade to version 10.1.x of the Universal Render Pipeline
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/upgrade-guide-9-0-x.html)
Upgrade to version 9.0.x of the Universal Render Pipeline
