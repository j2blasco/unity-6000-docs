* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/urp/render-graph-framebuffer-fetch.html

  * [Rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/rendering-and-post-processing.html)
  * [Render pipelines](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)
  * [Using the Universal Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/universal-render-pipeline.html)
  * [Custom rendering and post-processing in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/customizing-urp.html)
  * [Render graph system in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/render-graph.html)
  * [Frame data in the render graph system in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/render-graph-frame-data.html)
  * Get the current framebuffer from GPU memory in URP


[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/render-graph-add-textures-to-camera-history.html)
Add textures to the camera history
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/render-graph-frame-data-reference.html)
Frame data textures reference for URP
# Get the current framebuffer from GPU memory in URP
To more efficiently read a frame that Unity rendered in a previous pass, use the `SetInputAttachment` API to set the output of a render pass as the input of the next render pass.
Using `SetInputAttachment` means the render pass can access the framebuffer from the on-chip memory of the GPU, instead of video memory. This speeds up rendering, because the GPU doesn’t need to copy the texture to and from its video memory. This process is sometimes called framebuffer fetch.
On mobile devices, rendering speed improves on mobile devices that use tile-based deferred rendering (TBDR). The GPU keeps the frame in its on-chip tile memory between render passes, using less memory bandwidth and processing time.
If you use the `SetInputAttachment` API, URP merges the render passes that write to the framebuffer and read from it. You can check this in the [Render Graph Viewer window](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/render-graph-viewer-reference.html).
You can also use `SetInputAttachment` to read other render targets, for example a G-buffer.
## Requirements
The `SetInputAttachment` API is supported if you use one of the following graphics APIs:
  * Vulkan
  * Metal


If you use `SetInputAttachment` with an unsupported API, Unity copies the texture to and from video memory, so there’s no effect on rendering speed.
## Use the `SetInputAttachment` API
To use the `SetInputAttachment` API in a render pass, use the following:
  * The `SetInputAttachment` API to set the output of the previous render pass as the input of the new render pass.
  * The `LOAD_FRAMEBUFFER_X_INPUT` macro in your fragment **shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) code to read the **pixel** The smallest unit in a computer image. Pixel size depends on your screen resolution. Pixel lighting is calculated at every screen pixel. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/ShadowPerformance.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#pixel) from the previous render pass, instead of a sampling macro such as `SAMPLE_TEXTURE2D`.


The following steps assume you already have one render pass that writes to a `TextureHandle` called `sourceTextureHandle`.
  1. Create a custom shader, then create a material from the shader. For more information about creating a custom shader, refer to [Writing custom shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/writing-custom-shaders-urp.html).
  2. Inside the HLSLPROGRAM of your custom shader, make sure you import the `Packages/com.unity.render-pipelines.core/Runtime/Utilities/Blit.hlsl` file:
```
HLSLPROGRAM
...
#include "Packages/com.unity.render-pipelines.universal/ShaderLibrary/Core.hlsl"
...
ENDHLSL

```

  3. Inside the HLSLPROGRAM, use one of the following to declare the texture from the previous render pass. For example:
     * `FRAMEBUFFER_INPUT_X_HALF`
     * `FRAMEBUFFER_INPUT_X_FLOAT`
     * `FRAMEBUFFER_INPUT_X_INT`
     * `FRAMEBUFFER_INPUT_X_UINT`
For example:
```
FRAMEBUFFER_INPUT_X_HALF(0);

```

  4. In the fragment function, use `LOAD_FRAMEBUFFER_X_INPUT` to sample the texture from on-chip GPU memory. For example:
```
half4 frag() : SV_Target
{
    half4 colorFromPreviousRenderPass = LOAD_FRAMEBUFFER_X_INPUT(0, input.positionCS.xy);
    return colorFromPreviousRenderPass;
}

```

  5. In a new render graph render pass, add the material you created to your `PassData`. For example:
```
class PassData
{
    public Material exampleMaterial;
}

```

  6. Use `builder.SetInputAttachment` to set the output of the previous render pass as the input of the new render pass. For example:
```
builder.SetInputAttachment(sourceTextureHandle, 0, AccessFlags.Read);

```

  7. In your `SetRenderFunc` method, use a command such as `BlitTexture` to render using the material. For example:
```
static void ExecutePass(PassData data, RasterGraphContext context)
{
    Blitter.BlitTexture(context.cmd, new Vector4(1, 1, 0, 0), exampleMaterial, 1);
}

```



## Example
For a full example, refer to the example called **FrameBufferFetch** in the [render graph system URP package samples](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/package-samples.html).
## Additional resources
  * [Writing custom shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/writing-custom-shaders-urp.html)
  * [Write a render pass using the render graph system](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/render-graph-write-render-pass.html)
  * [Transfer a texture between render passes](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/render-graph-pass-textures-between-passes.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/render-graph-add-textures-to-camera-history.html)
Add textures to the camera history
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/render-graph-frame-data-reference.html)
Frame data textures reference for URP
