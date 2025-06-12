* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/urp/render-graph-create-a-texture.html

  * [Rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/rendering-and-post-processing.html)
  * [Render pipelines](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)
  * [Using the Universal Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/universal-render-pipeline.html)
  * [Custom rendering and post-processing in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/customizing-urp.html)
  * [Render graph system in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/render-graph.html)
  * [Textures in the Render Graph system in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/working-with-textures.html)
  * Create a texture in the render graph system in URP


[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/working-with-textures.html)
Textures in the Render Graph system in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/render-graph-import-a-texture.html)
Import a texture into the render graph system in URP
# Create a texture in the render graph system in URP
To create a texture in the render graph system, use the `UniversalRenderer.CreateRenderGraphTexture` API.
When the Universal **Render Pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Renderpipeline) (URP) optimizes the render graph, it might not create a texture if the final frame doesn’t use the texture, to reduce the memory and bandwidth the render passes use. For more information about how URP optimizes render graphs, refer to [Introduction to the render graph system](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/render-graph-introduction.html).
For more information about using a texture in multiple frames or on multiple **cameras** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera), for example a texture asset you imported in your project, refer to [Import a texture into the render graph system](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/render-graph-import-a-texture.html).
## Create a texture
To create a texture, in the `RecordRenderGraph` method of your `ScriptableRenderPass` class, follow these steps:
  1. Create a [`RenderTextureDescriptor`](https://docs.unity3d.com/ScriptReference/RenderTextureDescriptor.html) object with the texture properties you need.
  2. Use the [`UniversalRenderer.CreateRenderGraphTexture`](https://docs.unity3d.com/Packages/com.unity.render-pipelines.universal@latest/index.html?subfolder=/api/UnityEngine.Rendering.Universal.UniversalRenderer.html#UnityEngine_Rendering_Universal_UniversalRenderer_CreateRenderGraphTexture_UnityEngine_Rendering_RenderGraphModule_RenderGraph_UnityEngine_RenderTextureDescriptor_System_String_System_Boolean_UnityEngine_FilterMode_UnityEngine_TextureWrapMode_) method to create a texture and return a texture handle.


For example, the following creates a texture the same size as the screen.
```
RenderTextureDescriptor textureProperties = new RenderTextureDescriptor(Screen.width, Screen.height, RenderTextureFormat.Default, 0);
TextureHandle textureHandle = UniversalRenderer.CreateRenderGraphTexture(renderGraph, textureProperties, "My texture", false);

```

You can then [use the texture](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/render-graph-read-write-texture.html) in the same custom render pass.
Only the current camera can access the texture. To access the texture somewhere else, for example from another camera or in custom rendering code, [import a texture](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/render-graph-import-a-texture.html) instead.
The render graph system manages the lifetime of textures you create with `CreateRenderGraphTexture`, so you don’t need to manually release the memory they use when you’re finished with them.
### Example
The following Scriptable Renderer Feature contains an example render pass that creates a texture and clears it to yellow. For more information about adding the render pass to the render pipeline, refer to [Inject a pass using a Scriptable Renderer Feature](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/renderer-features/scriptable-renderer-features/inject-a-pass-using-a-scriptable-renderer-feature.html).
Use the [Frame Debugger](https://docs.unity3d.com/2023.3/Documentation/Manual/frame-debugger-window.html) to check the texture the render pass adds.
```
using UnityEngine;
using UnityEngine.Rendering.Universal;
using UnityEngine.Rendering.RenderGraphModule;
using UnityEngine.Rendering;

public class CreateYellowTextureFeature : ScriptableRendererFeature
{
    CreateYellowTexture customPass;

    public override void Create()
    {
        customPass = new CreateYellowTexture();
        customPass.renderPassEvent = RenderPassEvent.AfterRenderingPostProcessing;
    }

    public override void AddRenderPasses(ScriptableRenderer renderer, ref RenderingData renderingData)
    {
        renderer.EnqueuePass(customPass);
    }

    class CreateYellowTexture : ScriptableRenderPass
    {
        class PassData
        {
            internal TextureHandle cameraColorTexture;
        }

        public override void RecordRenderGraph(RenderGraph renderGraph, ContextContainer frameContext)
        {
            using (var builder = renderGraph.AddRasterRenderPass<PassData>("Create yellow texture", out var passData))
            {
                // Create texture properties that match the screen size
                RenderTextureDescriptor textureProperties = new RenderTextureDescriptor(Screen.width, Screen.height, RenderTextureFormat.Default, 0);

                // Create a temporary texture
                TextureHandle texture = UniversalRenderer.CreateRenderGraphTexture(renderGraph, textureProperties, "My texture", false);

                // Set the texture as the render target
                builder.SetRenderAttachment(texture, 0, AccessFlags.Write);
    
                builder.AllowPassCulling(false);

                builder.SetRenderFunc((PassData data, RasterGraphContext context) => ExecutePass(data, context));
            }
        }

        static void ExecutePass(PassData data, RasterGraphContext context)
        {          
            // Clear the render target to yellow
            context.cmd.ClearRenderTarget(true, true, Color.yellow);            
        }
    }

}

```

For another example, refer to the example called **OutputTexture** in the [Universal Render Pipeline (URP) package samples](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/package-samples.html).
## Additional resources
  * [Import a texture into the render graph system](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/render-graph-import-a-texture.html)
  * [Use frame data](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/accessing-frame-data.html)
  * [Textures](https://docs.unity3d.com/Manual/Textures.html)An image used when rendering a GameObject, Sprite, or UI element. Textures are often applied to the surface of a mesh to give it visual detail. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextureImporter.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#texture)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/working-with-textures.html)
Textures in the Render Graph system in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/render-graph-import-a-texture.html)
Import a texture into the render graph system in URP
