* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/urp/upgrade-guide-unity-6.html

  * [Rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/rendering-and-post-processing.html)
  * [Render pipelines](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)
  * [Using the Universal Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/universal-render-pipeline.html)
  * [Get started with URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/introduction-landing.html)
  * [Installing and upgrading URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/InstallingAndConfiguringURP.html)
  * [Upgrade URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/upgrade-guides.html)
  * Upgrade to URP 17 (Unity 6.0)


[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/upgrade-guides.html)
Upgrade URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/upgrade-guide-2023-2.html)
Upgrade to URP 16 (Unity 2023.2)
# Upgrade to URP 17 (Unity 6.0)
This page describes how to upgrade from an older version of the Universal **Render Pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Renderpipeline) (URP) to URP 17 (Unity 6.0).
For information on converting assets made for a Built-in Render Pipeline project to assets compatible with URP, refer to the page [Render Pipeline Converter](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/features/rp-converter.html).
## Upgrading from URP 15 or URP 16 (Unity 2023.1, Unity 2023.2)
### Render graph system
URP 17 introduces the [render graph](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/render-graph-introduction.html) system, which includes significant changes to the way you write custom render passes.
If your project contains custom render passes, rewrite your passes using the render graph API. For more information on render graph, refer to the section [Render graph system](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/render-graph.html).
The following page contains a complete example of a Scriptable Renderer Feature with a render pass that uses the render graph API:
  * [Example of a complete Scriptable Renderer Feature](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/renderer-features/create-custom-renderer-feature.html)


**Note:** Unity no longer develops or improves the **rendering path** The technique that a render pipeline uses to render graphics. Choosing a different rendering path affects how lighting and shading are calculated. Some rendering paths are more suited to different platforms and hardware than others. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/RenderingPaths.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#RenderingPath) that doesn’t use the [render graph API](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/render-graph.html).
Render graph is enabled by default in new URP projects.
For compatibility purpose, Unity 6 includes the option to disable the render graph system and use the rendering API from previous URP versions. To disable render graph, enable the following checkbox:
  * **Project Settings** > **Graphics** > **Render Graph** > **Compatibility Mode (Render Graph Disabled)**


If you open an existing project created with a URP version without render graph, Unity automatically enables the compatibility mode after opening the project with Unity 6.
To understand a render graph implementation better, use the [Render Graph Viewer](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/render-graph-view.html#use-the-render-graph-viewer)
### Volume Framework
When you create a custom Volume component class that overrides the `VolumeComponent.Override(VolumeComponent state, float interpFactor)` method, your implementation must set the `VolumeParameter.overrideState` property to `true` whenever the `VolumeParameter` value is changed. This ensures that the Volume framework resets the parameters to their correct default values. This lets the framework to use fewer resources every frame which improves performance.
## Upgrading from URP 13 (Unity 2022.1)
### Two shader defines were removed
`SHADER_QUALITY_LOW/MEDIUM/HIGH` and `SHADER_HINT_NICE_QUALITY` **shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) defines were removed. If you used those defines in custom shaders, consider using `SHADER_API_MOBILE` or `SHADER_API_GLES` defines to replace `SHADER_QUALITY_LOW/MEDIUM/HIGH`.
## Upgrading from URP 12 (Unity 2021.2)
### Changes to ScriptableRenderer API behavior
Unity now issues an error when instances of `ScriptableRendererFeature` attempt to access render targets before they are allocated by the `ScriptableRenderer` class.
The `ScriptableRendererFeature` class has a new virtual function `SetupRenderPasses` which is called when render targets are allocated and ready to be used.
If your code uses the `ScriptableRenderer.cameraColorTarget` or the `ScriptableRenderer.cameraDepthTarget` property inside of the `AddRenderPasses` method override, you should move that implementation to the `ScriptableRendererFeature.SetupRenderPasses` method.
The calls to the `ScriptableRenderer.EnqueuePass` method should still happen in the `AddRenderPasses` method.
The following example shows how to change the code to use the new API.
Code with the old API:
```
public override void AddRenderPasses(ScriptableRenderer renderer,
                                    ref RenderingData renderingData)
{
    // The target is used before allocation
    m_CustomPass.Setup(renderer.cameraColorTarget);
     // Letting the renderer know which passes are used before allocation
    renderer.EnqueuePass(m_ScriptablePass);
}

```

Code with the new API:
```
public override void AddRenderPasses(ScriptableRenderer renderer,
                                        ref RenderingData renderingData)
{
    // Letting the renderer know which passes are used before allocation
    renderer.EnqueuePass(m_ScriptablePass);
}

public override void SetupRenderPasses(ScriptableRenderer renderer,
                                          in RenderingData renderingData)
{
    // The target is used after allocation
    m_CustomPass.Setup(renderer.cameraColorTarget);
}

```

### The Universal Renderer is now using the RTHandle system
The Universal Renderer is now using [the RTHandle system](https://docs.unity3d.com/Packages/com.unity.render-pipelines.core@14.0/manual/rthandle-system.html) for its internal targets and in its internal passes.
All usages of the `RenderTargetHandle` struct are set as obsolete and the struct will be removed in the future.
The public interfaces `ScriptableRenderer.cameraColorTarget` and `ScriptableRenderer.cameraDepthTarget` are marked as obsolete. Replace them with `ScriptableRenderer.cameraColorTargetHandle` and `ScriptableRenderer.cameraDepthTargetHandle` respectively.
`RTHandle` targets do not use the `CommandBuffer.GetTemporaryRT` method and persist for more frames than the `RenderTargetIdentifier` structs. You cannot allocate `RTHandle` targets with the properties `GraphicsFormat` and `DepthBufferBits` set to any value except for 0. The `cameraDepthTarget` properties must be separate from the `cameraColorTarget` properties.
The following helper functions let you create and use temporary render target with the `RTHandle` system in a similar way as with the `GetTemporaryRT` method previously:
  * `RenderingUtils.ReAllocateIfNeeded`
  * `ShadowUtils.ShadowRTReAllocateIfNeeded`


If the render target does not change within the lifetime of the application, use the `RTHandles.Alloc` method to allocate an `RTHandle` target. This method is efficient since the code does not have to check if a render target should be allocated on each frame.
If the render target is a full screen texture, which means that its resolution matches or is a fraction of the resolution of the screen, use a scaling factor such as `Vector2D.one` to support dynamic scaling.
The following example shows how to change the code using the `RenderTargetHandle` API to use the new API.
Code with the old API:
```
public class CustomPass : ScriptableRenderPass
{
    RenderTargetHandle m_Handle;
    // With the old API, RenderTargetIdentifier might combine color and depth
    RenderTargetIdentifier m_Destination;

    public CustomPass()
    {
        m_Handle.Init("_CustomPassHandle");
    }

    public override void OnCameraSetup(CommandBuffer cmd, ref RenderingData renderingData)
    {
        var desc = renderingData.cameraData.cameraTargetDescriptor;
        cmd.GetTemporaryRT(m_Handle.id, desc, FilterMode.Point);
    }

    public override void OnCameraCleanup(CommandBuffer cmd)
    {
        cmd.ReleaseTemporaryRT(m_Handle.id);
    }

    public void Setup(RenderTargetIdentifier destination)
    {
        m_Destination = destination;
    }

    public override void Execute(ScriptableRenderContext context,
                                    ref RenderingData renderingData)
    {
        CommandBuffer cmd = CommandBufferPool.Get();
        // Set the same target for color and depth
        ScriptableRenderer.SetRenderTarget(cmd, m_Destination, m_Destination, clearFlag,
                                              clearColor);
        context.ExecuteCommandBuffer(cmd);
        CommandBufferPool.Release(cmd);
    }
}

```

Code with the new API:
```
public class CustomPass : ScriptableRenderPass
{
    RTHandle m_Handle;
    // Then using RTHandles, the color and the depth properties must be separate
    RTHandle m_DestinationColor;
    RTHandle m_DestinationDepth;

    void Dispose()
    {
        m_Handle?.Release();
    }

    public override void OnCameraSetup(CommandBuffer cmd, ref RenderingData renderingData)
    {
        var desc = renderingData.cameraData.cameraTargetDescriptor;
        // Then using RTHandles, the color and the depth properties must be separate
        desc.depthBufferBits = 0;
        RenderingUtils.ReAllocateIfNeeded(ref m_Handle, desc, FilterMode.Point,
                                         TextureWrapMode.Clamp, name: "_CustomPassHandle");
    }

    public override void OnCameraCleanup(CommandBuffer cmd)
    {
        m_DestinationColor = null;
        m_DestinationDepth = null;
    }

    public void Setup(RTHandle destinationColor, RTHandle destinationDepth)
    {
        m_DestinationColor = destinationColor;
        m_DestinationDepth = destinationDepth;
    }

    public override void Execute(ScriptableRenderContext context,
                                    ref RenderingData renderingData)
    {
        CommandBuffer cmd = CommandBufferPool.Get();
        ScriptableRenderer.SetRenderTarget(cmd, m_DestinationColor, m_DestinationDepth,
                                              clearFlag, clearColor);
        context.ExecuteCommandBuffer(cmd);
        CommandBufferPool.Release(cmd);
    }
}

```

## Upgrading from URP 11.x.x
  * The Forward Renderer asset is renamed to the Universal Renderer asset. When you open an existing project in the Unity Editor containing URP 12, Unity updates the existing Forward Renderer assets to Universal Renderer assets.
  * The Universal Renderer asset contains the property **Rendering Path** that lets you select the Forward or the Deferred Rendering Path.
  * The method `ClearFlag.Depth` does not implicitly clear the **Stencil buffer** A memory store that holds an 8-bit per-pixel value. In Unity, you can use a stencil buffer to flag pixels, and then only render to pixels that pass the stencil operation. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-RenderTexture.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#stencilbuffer) anymore. Use the new method `ClearFlag.Stencil`.
  * URP 12 and later implements the [Render Pipeline Converter](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/features/rp-converter.html) feature. This feature replaces the asset upgrade functions that were previously available at **Edit > Render Pipeline > Universal Render Pipeline > Upgrade…**


## Upgrading from URP 10.0.x–10.2.x
  1. The file names of the following Shader Graph shaders were renamed. The new file names do not have spaces:  
`Autodesk Interactive`  
`Autodesk Interactive Masked`  
`Autodesk Interactive Transparent`
If your code uses the `Shader.Find()` method to search for the shaders, remove spaces from the shader names, for example, `Shader.Find("AutodeskInteractive)`.


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
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/upgrade-guides.html)
Upgrade URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/upgrade-guide-2023-2.html)
Upgrade to URP 16 (Unity 2023.2)
