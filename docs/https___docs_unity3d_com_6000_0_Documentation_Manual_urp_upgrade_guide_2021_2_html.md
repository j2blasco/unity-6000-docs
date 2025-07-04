* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/urp/upgrade-guide-2021-2.html

  * [Rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/rendering-and-post-processing.html)
  * [Render pipelines](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)
  * [Using the Universal Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/universal-render-pipeline.html)
  * [Get started with URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/introduction-landing.html)
  * [Installing and upgrading URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/InstallingAndConfiguringURP.html)
  * [Upgrade URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/upgrade-guides.html)
  * Upgrade to URP 12 (Unity 2021.2)


[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/upgrade-guide-2022-1.html)
Upgrade to URP 13 (Unity 2022.1)
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/upgrade-guide-11-0-x.html)
Upgrade to version 11.0.x of the Universal Render Pipeline
# Upgrade to URP 12 (Unity 2021.2)
This page describes how to upgrade from an older version of the Universal **Render Pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Renderpipeline) (URP) to version 12.0.x.
For information on converting assets made for a Built-in Render Pipeline project to assets compatible with URP, refer to the page [Render Pipeline Converter](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/features/rp-converter.html).
## Upgrading from URP 11.x.x
  * The Forward Renderer asset is renamed to the Universal Renderer asset. When you open an existing project in the Unity Editor containing URP 12, Unity updates the existing Forward Renderer assets to Universal Renderer assets.
  * The Universal Renderer asset contains the property ****Rendering Path** The technique that a render pipeline uses to render graphics. Choosing a different rendering path affects how lighting and shading are calculated. Some rendering paths are more suited to different platforms and hardware than others. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/RenderingPaths.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#RenderingPath)** that lets you select the Forward or the Deferred Rendering Path.
  * The method `ClearFlag.Depth` does not implicitly clear the **Stencil buffer** A memory store that holds an 8-bit per-pixel value. In Unity, you can use a stencil buffer to flag pixels, and then only render to pixels that pass the stencil operation. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-RenderTexture.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#stencilbuffer) anymore. Use the new method `ClearFlag.Stencil`.
  * URP 12 implements the [Render Pipeline Converter](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/features/rp-converter.html) feature. This feature replaces the asset upgrade functions that were previously available at **Edit > Render Pipeline > Universal Render Pipeline > Upgrade…**


## Upgrading from URP 10.0.x–10.2.x
  1. The file names of the following Shader Graph shaders were renamed. The new file names do not have spaces:  
`Autodesk Interactive`  
`Autodesk Interactive Masked`  
`Autodesk Interactive Transparent`
If your code uses the `Shader.Find()` method to search for the shaders, remove spaces from the **shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) names, for example, `Shader.Find("AutodeskInteractive)`.


## Upgrading from URP 7.2.x and later releases
  1. URP 12.x.x does not support the package **Post-Processing** A process that improves product visuals by applying filters and effects before the image appears on screen. You can use post-processing effects to simulate physical camera and film properties, for example Bloom and Depth of Field. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/PostProcessingOverview.html) post processing, postprocessing, postprocess  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#post-processing) Stack v2. If your Project uses the package Post-Processing Stack v2, migrate the effects that use that package first.


### DepthNormals Pass
Starting from version 10.0.x, URP can generate a normal texture called `_CameraNormalsTexture`. To render to this texture in your custom shader, add a Pass with the name `DepthNormals`. For an example, check the implementation in `Lit.shader`.
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
### Shadow Normal Bias
In 11.0.x the formula used to apply Shadow Normal Bias has been slightly fix in order to work better with punctual lights. As a result, to match exactly shadow outlines from earlier revisions, the parameter might to be adjusted in some **scenes** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene). Typically, using 1.4 instead of 1.0 for a Directional light is usually enough.
### Intermediate Texture
In previous URP versions, URP performed the rendering via an intermediate Renderer if the Renderer had any active Renderer Features. On some platforms, this had significant performance implications. In this release, URP mitigates the issue in the following way: URP expects Renderer Features to declare their inputs using the `ScriptableRenderPass.ConfigureInput` method. The method provides the information that URP uses to determine automatically whether rendering via an intermediate texture is necessary.
For compatibility purpose, there is a new property **Intermediate Texture** in the Universal Renderer. If you select **Always** in the property, URP uses an intermediate texture. Selecting **Auto** enables the new behavior. Use the **Always** option only if a Renderer Feature does not declare its inputs using the `ScriptableRenderPass.ConfigureInput` method.
To ensure that existing projects work correctly, all existing Universal Renderer assets that were using any Renderer Features (excluding those included with URP) have the option **Always** selected in the **Intermediate Texture** property. Any newly created Universal Renderer assets have the option **Auto** selected.
## Upgrading from URP 7.0.x–7.1.x
  1. Upgrade to URP 7.2.0 first. Refer to [Upgrading to version 7.2.0 of the Universal Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/upgrade-guide-7-2-0.html).
  2. URP 8.x.x does not support the package Post-Processing Stack v2. If your Project uses the package Post-Processing Stack v2, migrate the effects that use that package first.


## Upgrading from LWRP to 12.x.x
  * There is no direct upgrade path from LWRP to URP 12.x.x. Follow the steps to upgrade LWRP to URP 11.x.x first, and then upgrade from URP 11.x.x to URP 12.x.x.


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/upgrade-guide-2022-1.html)
Upgrade to URP 13 (Unity 2022.1)
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/upgrade-guide-11-0-x.html)
Upgrade to version 11.0.x of the Universal Render Pipeline
