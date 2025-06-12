* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/urp/render-graph-import-a-texture.html

  * [Rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/rendering-and-post-processing.html)
  * [Render pipelines](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)
  * [Using the Universal Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/universal-render-pipeline.html)
  * [Custom rendering and post-processing in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/customizing-urp.html)
  * [Render graph system in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/render-graph.html)
  * [Textures in the Render Graph system in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/working-with-textures.html)
  * Import a texture into the render graph system in URP


[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/render-graph-create-a-texture.html)
Create a texture in the render graph system in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/render-graph-read-write-texture.html)
Use a texture in a render pass in URP
# Import a texture into the render graph system in URP
When you [create a texture in the render graph system](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/render-graph-create-a-texture.html) in a render pass, the render graph system handles the creation and disposal of the texture. This process means the texture might not exist in the next frame, and other **cameras** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera) might not be able to use it.
To make sure a texture is available across frames and cameras, import it into the render graph system using the `ImportTexture` API.
You can import a texture if you use a texture created outside the render graph system. For example, you can create a **render texture** A special type of Texture that is created and updated at runtime. To use them, first create a new Render Texture and designate one of your Cameras to render into it. Then you can use the Render Texture in a Material just like a regular Texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-RenderTexture.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#RenderTexture) that points to a texture in your project, such as a [texture asset](https://docs.unity3d.com/Manual/ImportingTextures.html), and use it as the input to a render pass.
The render graph system doesn’t manage the lifetime of imported textures. As a result, the following applies:
  * You must [dispose of the imported render texture](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/render-graph-import-a-texture.html#dispose-of-a-render-texture) to free up the memory it uses when you’re finished with it.
  * URP can’t cull render passes that use imported textures. As a result, rendering might be slower.


For more information about the `RTHandle` API, refer to [Using the RTHandle system](https://docs.unity3d.com/Packages/com.unity.render-pipelines.core@17.0/manual/rthandle-system-using.html).
## Import a texture
To import a texture, in the `RecordRenderGraph` method of your `ScriptableRenderPass` class, follow these steps:
  1. Create a render texture handle using the [RTHandle](https://docs.unity3d.com/Packages/com.unity.render-pipelines.core@17.0/api/UnityEngine.Rendering.RTHandle.html) API.
For example:
```
private RTHandle renderTextureHandle;

```

  2. Create a [RenderTextureDescriptor](https://docs.unity3d.com/ScriptReference/RenderTextureDescriptor.html) object with the texture properties you need.
For example:
```
RenderTextureDescriptor textureProperties = new RenderTextureDescriptor(Screen.width, Screen.height, RenderTextureFormat.Default, 0);

```

  3. Use the [ReAllocateIfNeeded](https://docs.unity3d.com/Packages/com.unity.render-pipelines.universal@latest/index.html?subfolder=/api/UnityEngine.Rendering.Universal.ShadowUtils.html#UnityEngine_Rendering_Universal_ShadowUtils_ShadowRTReAllocateIfNeeded_UnityEngine_Rendering_RTHandle__System_Int32_System_Int32_System_Int32_System_Int32_System_Single_System_String_) method to create a render texture and attach it to the render texture handle. This method creates a render texture only if the render texture handle is null, or the render texture has different properties to the render texture descriptor.
For example:
```
RenderingUtils.ReAllocateIfNeeded(ref renderTextureHandle, textureProperties, FilterMode.Bilinear, TextureWrapMode.Clamp, name: "My render texture" );

```

  4. Import the texture, to convert the `RTHandle` object to a `TextureHandle` object the render graph system can use. 
For example:
```
TextureHandle texture = renderGraph.ImportTexture(renderTextureHandle);

```



You can then use the `TextureHandle` object to [read from or write to the render texture](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/render-graph-read-write-texture.html).
## Import a texture from your project
To import a texture from your project, such as an imported texture attached to a material, follow these steps:
  1. Use the [`RTHandles.Alloc`](https://docs.unity3d.com/Packages/com.unity.render-pipelines.core@17.0/api/UnityEngine.Rendering.RTHandles.html#UnityEngine_Rendering_RTHandles_Alloc_UnityEngine_RenderTexture_) API to create a render texture handle from the external texture.
For example:
```
RTHandle renderTexture = RTHandles.Alloc(texture);

```

  2. Import the texture, to convert the `RTHandle` object to a `TextureHandle` object that the render graph system can use.
For example:
```
TextureHandle textureHandle = renderGraph.ImportTexture(renderTexture);

```



You can then use the `TextureHandle` object to [read from or write to the render texture](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/render-graph-read-write-texture.html).
## Dispose of the render texture
You must free the memory a render texture uses at the end of a render pass, using the `Dispose` method. For example:
```
public void Dispose()
{
    renderTexture.Release();
}

```

## Example
The following Scriptable Renderer Feature contains an example render pass that copies a texture asset to a temporary texture. To use this example, follow these steps:
  1. Add this Scriptable Renderer Feature to a URP Asset. Refer to [Inject a pass using a Scriptable Renderer Feature](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/renderer-features/scriptable-renderer-features/inject-a-pass-using-a-scriptable-renderer-feature.html).
  2. In the **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector) window of the URP Asset, add a texture to the **Texture To Use** property.
  3. Use the [Frame Debugger](https://docs.unity3d.com/2023.3/Documentation/Manual/frame-debugger-window.html) to check the texture the render pass adds.

```
using UnityEngine;
using UnityEngine.Rendering.Universal;
using UnityEngine.Rendering.RenderGraphModule;
using UnityEngine.Rendering;

public class BlitFromExternalTexture : ScriptableRendererFeature
{
    // The texture to use as input 
    public Texture2D textureToUse;

    BlitFromTexture customPass;

    public override void Create()
    {
        // Create an instance of the render pass, and pass in the input texture 
        customPass = new BlitFromTexture(textureToUse);

        customPass.renderPassEvent = RenderPassEvent.AfterRenderingPostProcessing;
    }

    public override void AddRenderPasses(ScriptableRenderer renderer, ref RenderingData renderingData)
    {
        renderer.EnqueuePass(customPass);
    }

    class BlitFromTexture : ScriptableRenderPass
    {
        class PassData
        {
            internal TextureHandle textureToRead;
        }

        private Texture2D texturePassedIn;

        public BlitFromTexture(Texture2D textureIn)
        {
            // In the render pass's constructor, set the input texture
            texturePassedIn = textureIn;
        }

        public override void RecordRenderGraph(RenderGraph renderGraph, ContextContainer frameContext)
        {
            using (var builder = renderGraph.AddRasterRenderPass<PassData>("Copy texture", out var passData))
            {
                // Create a temporary texture and set it as the render target
                RenderTextureDescriptor textureProperties = new RenderTextureDescriptor(Screen.width, Screen.height, RenderTextureFormat.Default, 0);
                TextureHandle texture = UniversalRenderer.CreateRenderGraphTexture(renderGraph, textureProperties, "My texture", false);
                builder.SetRenderAttachment(texture, 0, AccessFlags.Write);

                // Create a render texture from the input texture
                RTHandle rtHandle = RTHandles.Alloc(texturePassedIn);

                // Create a texture handle that the render graph system can use
                TextureHandle textureToRead = renderGraph.ImportTexture(rtHandle);

                // Add the texture to the pass data
                passData.textureToRead = textureToRead;

                // Set the texture as readable
                builder.UseTexture(passData.textureToRead, AccessFlags.Read);

                builder.AllowPassCulling(false);

                builder.SetRenderFunc((PassData data, RasterGraphContext context) => ExecutePass(data, context));
            }
        }

        static void ExecutePass(PassData data, RasterGraphContext context)
        {          
            // Copy the imported texture to the render target
            Blitter.BlitTexture(context.cmd, data.textureToRead, new Vector4(0.8f,0.6f,0,0), 0, false);

            // Dispose of the texture
            RTHandles.Release(data.textureToRead);
        }
    }
}

```

## Additional resources
  * [Textures](https://docs.unity3d.com/Manual/Textures.html)An image used when rendering a GameObject, Sprite, or UI element. Textures are often applied to the surface of a mesh to give it visual detail. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextureImporter.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#texture)
  * [Render Texture assets](https://docs.unity3d.com/Manual/class-RenderTexture.html)
  * [Custom Render Texture assets](https://docs.unity3d.com/Manual/class-CustomRenderTexture.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/render-graph-create-a-texture.html)
Create a texture in the render graph system in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/render-graph-read-write-texture.html)
Use a texture in a render pass in URP
