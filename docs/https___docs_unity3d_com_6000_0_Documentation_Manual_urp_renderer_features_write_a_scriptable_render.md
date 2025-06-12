* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/urp/renderer-features/write-a-scriptable-render-pass.html

  * [Rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/rendering-and-post-processing.html)
  * [Render pipelines](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)
  * [Using the Universal Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/universal-render-pipeline.html)
  * [Custom rendering and post-processing in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/customizing-urp.html)
  * [Compatibility Mode in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/compatibility-mode.html)
  * Write a Scriptable Render Pass in Compatibility Mode in URP


[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/compatibility-mode.html)
Compatibility Mode in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/renderer-features/how-to-fullscreen-blit.html)
Example of a Scriptable Renderer Feature in Compatibility mode in URP
# Write a Scriptable Render Pass in Compatibility Mode in URP
**Note:** Unity no longer develops or improves the rendering path that doesn’t use the [render graph API](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/render-graph.html). Use the render graph API instead when developing new graphics features. To use the instructions on this page, enable **Compatibility Mode (Render Graph Disabled)** in URP graphics settings (**Project Settings** > **Graphics**).
To create a Scriptable Render Pass in the Universal **Render Pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Renderpipeline) (URP), follow these steps:
  1. Create a C# script that inherits the `ScriptableRenderPass` class. For example:
```
using UnityEngine.Rendering;
using UnityEngine.Rendering.Universal;

public class ExampleRenderPass : ScriptableRenderPass
{
}

```

  2. In the class, add variables for the materials and textures you use in the render pass.
For example, the following code sets up a handle to a texture, and a descriptor to configure the texture.
```
private RTHandle textureHandle;
private RenderTextureDescriptor textureDescriptor;

```

  3. Override the `Configure` method to set up the render pass. Unity calls this method before executing the render pass.
For example:
```
public override void Configure(CommandBuffer cmd, RenderTextureDescriptor cameraTextureDescriptor)
{
    //Set the texture size to be the same as the camera target size.
    textureDescriptor.width = cameraTextureDescriptor.width;
    textureDescriptor.height = cameraTextureDescriptor.height;

    //Check if the descriptor has changed, and reallocate the texture handle if necessary.
    RenderingUtils.ReAllocateIfNeeded(ref textureHandle, textureDescriptor);
}

```

  4. Override the `Execute` method with your rendering commands. Unity calls this method every frame, once for each **camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera).
For example:
```
public override void Execute(ScriptableRenderContext context, ref RenderingData renderingData)
{
    // Get a CommandBuffer from pool
    CommandBuffer cmd = CommandBufferPool.Get();

    // Add rendering commands to the CommandBuffer
    ...

    // Execute the command buffer and release it back to the pool
    context.ExecuteCommandBuffer(cmd);
    CommandBufferPool.Release(cmd);
}

```



## Inject a render pass into the render loop
To inject a render pass into the render loop in Compatibility Mode, refer to the following:
  * [Use the `RenderPipelineManager` API](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/customize/inject-render-pass-via-script.html)
  * [Use a Scriptable Renderer Feature](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/renderer-features/scriptable-renderer-features/inject-a-pass-using-a-scriptable-renderer-feature.html)


For a complete example, refer to [Example of a Scriptable Renderer Feature in Compatibility mode](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/renderer-features/how-to-fullscreen-blit.html).
## Additional resources
  * [Custom render pass workflow](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/renderer-features/custom-rendering-pass-workflow-in-urp.html)
  * [Writing custom shaders in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/writing-custom-shaders-urp.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/compatibility-mode.html)
Compatibility Mode in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/renderer-features/how-to-fullscreen-blit.html)
Example of a Scriptable Renderer Feature in Compatibility mode in URP
