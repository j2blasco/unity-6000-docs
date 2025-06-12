* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/urp/render-graph-read-write-texture.html

  * [Rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/rendering-and-post-processing.html)
  * [Render pipelines](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)
  * [Using the Universal Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/universal-render-pipeline.html)
  * [Custom rendering and post-processing in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/customizing-urp.html)
  * [Render graph system in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/render-graph.html)
  * [Textures in the Render Graph system in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/working-with-textures.html)
  * Use a texture in a render pass in URP


[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/render-graph-import-a-texture.html)
Import a texture into the render graph system in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/render-graph-pass-textures-between-passes.html)
Transfer a texture between render passes in URP
# Use a texture in a render pass in URP
You can use the render graph system API to set a texture as an input or output for a custom render pass, so you can read from or write to it.
You can’t both read from and write to the same texture in a render pass. Refer to [Change the render target during a render pass](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/render-graph-read-write-texture.html#change-the-render-target-during-a-pass) for more information.
## Set a texture as an input
To set a texture as an input for a custom render pass, follow these steps:
  1. In the `RecordRenderGraph` method, add a texture handle field to the data your pass uses.
For example:
```
// Create the data your pass uses
public class MyPassData
{
    // Add a texture handle
    public TextureHandle textureToUse;
}

```

  2. Set the texture handle to the texture you want to use.
For example:
```
// Add the texture handle to the data
RenderTextureDescriptor textureProperties = new RenderTextureDescriptor(Screen.width, Screen.height, RenderTextureFormat.Default, 0);
TextureHandle textureHandle = UniversalRenderer.CreateRenderGraphTexture(renderGraph, textureProperties, "My texture", false);
passData.textureToUse = textureHandle;

```

  3. Call the [`UseTexture`](https://docs.unity3d.com/Packages/com.unity.render-pipelines.core@17.0/api/UnityEngine.Rendering.RenderGraphModule.IBaseRenderGraphBuilder.html#UnityEngine_Rendering_RenderGraphModule_IBaseRenderGraphBuilder_UseTexture_UnityEngine_Rendering_RenderGraphModule_TextureHandle__UnityEngine_Rendering_RenderGraphModule_AccessFlags_) method to set the texture as an input.
For example:
```
builder.UseTexture(passData.textureToUse, AccessFlags.Read);

```



In your `SetRenderFunc` method, you can now use the `TextureHandle` object in the pass data as an input for APIs such as `Blitter.BlitTexture`. 
## Set a texture as the render target
To set a texture as the output for commands such as `Blit`, in the `RecordRenderGraph` method, use the [`SetRenderAttachment`](https://docs.unity3d.com/Packages/com.unity.render-pipelines.core@17.0/api/UnityEngine.Rendering.RenderGraphModule.IRasterRenderGraphBuilder.html#UnityEngine_Rendering_RenderGraphModule_IRasterRenderGraphBuilder_SetRenderAttachment_UnityEngine_Rendering_RenderGraphModule_TextureHandle_System_Int32_UnityEngine_Rendering_RenderGraphModule_AccessFlags_) method. The `SetRenderAttachment` method sets the texture as write-only by default.
For example, the following command creates a temporary texture and sets it as the render target for the render pass:
```
// Create texture properties
RenderTextureDescriptor textureProperties = new RenderTextureDescriptor(Screen.width, Screen.height, RenderTextureFormat.Default, 0);

// Create the texture
TextureHandle targetTexture = UniversalRenderer.CreateRenderGraphTexture(renderGraph, textureProperties, "My texture", false);

// Set the texture as the render target
// The second parameter is the index the shader uses to access the texture
builder.SetRenderAttachment(targetTexture, 0);

```

In your `SetRenderFunc` method, you can now write to the texture using APIs such as `Blitter.BlitTexture`. 
You don’t need to add the texture to your pass data. The render graph system sets up the texture for you automatically before it executes the render pass.
If you need to draw objects to the render target, refer to [Draw objects in a render pass](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/render-graph-draw-objects-in-a-pass.html) for additional information.
## Change the render target during a render pass
You can’t change which texture URP writes to during a render graph system render pass.
You can do either of the following instead:
  * Create a second custom render pass, and use `builder.SetRenderAttachment` during the second render pass to change the render target.
  * Use the `UnsafePass` API so you can use the `SetRenderTarget` API in the `SetRenderFunc` method. Refer to [Use Compatibility Mode APIs in render graph render passes](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/render-graph-unsafe-pass.html) for more information and an example.


You can use these methods to read from and write to the same texture, by first copying from the texture to a temporary texture you create, then copying back.
If you **blit** A shorthand term for “bit block transfer”. A blit operation is the process of transferring blocks of data from one place in memory to another.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#blit) between several textures with different properties, rendering might be slow because URP can’t merge the blits into a single native render pass. Use the `AddUnSafePass` API and the `SetRenderTarget()` method instead.
### Examples
Refer to the following:
  * [Write a render pass](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/render-graph-write-render-pass.html) for an example that creates a texture then blits to it.
  * [Import a texture into the render graph system](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/render-graph-import-a-texture.html) for an example that sets a temporary texture as the render target.


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/render-graph-import-a-texture.html)
Import a texture into the render graph system in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/render-graph-pass-textures-between-passes.html)
Transfer a texture between render passes in URP
