* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/urp/accessing-frame-data.html

  * [Rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/rendering-and-post-processing.html)
  * [Render pipelines](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)
  * [Using the Universal Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/universal-render-pipeline.html)
  * [Custom rendering and post-processing in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/customizing-urp.html)
  * [Render graph system in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/render-graph.html)
  * [Frame data in the render graph system in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/render-graph-frame-data.html)
  * Get data from the current frame in URP


[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/render-graph-frame-data.html)
Frame data in the render graph system in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/render-graph-get-previous-frames.html)
Get data from previous frames in URP
# Get data from the current frame in URP
You can fetch the textures that the Universal **Render Pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Renderpipeline) (URP) creates for the current frame, for example the active color buffer or a G-buffer texture, and use them in your render passes.
These textures are called frame data, resource data, or frame resources. This documentation refers to these textures as frame data.
Some textures might not exist in the frame data, depending on which injection point you use to insert your custom render pass into the URP frame rendering loop. For more information about which textures exist when, refer to [Injection points reference](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/customize/custom-pass-injection-points.html).
## Get frame data
The frame data is in the `ContextContainer` object that URP provides when you override the `RecordRenderGraph` method.
Follow these steps to get a handle to a texture in the frame data:
  1. Get all the frame data as a `UniversalResourceData` object, using the `Get` method of the `ContextContainer` object.
For example:
```
public override void RecordRenderGraph(RenderGraph renderGraph, ContextContainer frameContext)
{
    using (var builder = renderGraph.AddRasterRenderPass<PassData>("Get frame data", out var passData))
    {
        UniversalResourceData frameData = frameContext.Get<UniversalResourceData>();
    }
}

```

  2. Get the handle to a texture in the frame data.
For example, the following gets a handle to the active color texture:
```
TextureHandle activeColorTexture = frameData.activeColorTexture;

```



You can then read from and write to the texture. Refer to [Use a texture in a render pass](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/render-graph-read-write-texture.html).
The texture handle is valid only for the current render graph in the current frame.
You can use the [ConfigureInput](https://docs.unity3d.com/Packages/com.unity.render-pipelines.universal@latest/index.html?subfolder=/api/UnityEngine.Rendering.Universal.ScriptableRenderPass.html#UnityEngine_Rendering_Universal_ScriptableRenderPass_ConfigureInput_UnityEngine_Rendering_Universal_ScriptableRenderPassInput_) API to make sure URP generates the texture you need in the frame data.
## Example
For a full example, refer to the example called **TextureReference w. FrameData** in the [Universal Render Pipeline (URP) package samples](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/package-samples.html).
## Additional resources
  * [Frame data textures reference for URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/render-graph-frame-data-reference.html)
  * [Rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/rendering-in-universalrp.html)
  * [Render pipeline concepts](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/urp-concepts.html)
  * [Deferred rendering path in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/rendering/deferred-rendering-path-landing.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/render-graph-frame-data.html)
Frame data in the render graph system in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/render-graph-get-previous-frames.html)
Get data from previous frames in URP
