* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/urp/render-graph-add-textures-to-camera-history.html

  * [Rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/rendering-and-post-processing.html)
  * [Render pipelines](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)
  * [Using the Universal Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/universal-render-pipeline.html)
  * [Custom rendering and post-processing in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/customizing-urp.html)
  * [Render graph system in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/render-graph.html)
  * [Frame data in the render graph system in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/render-graph-frame-data.html)
  * Add textures to the camera history


[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/render-graph-get-previous-frames.html)
Get data from previous frames in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/render-graph-framebuffer-fetch.html)
Get the current framebuffer from GPU memory in URP
# Add textures to the camera history
To add your own texture to the **camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera) history and read the data in later frames, create a camera history type to store the texture between frames.
## Create a camera history type
Follow these steps:
  1. Create a class that inherits from `CameraHistoryItem`. For example:
```
public class ExampleHistoryType : CameraHistoryItem {
    ...
}

```

  2. In the class, add an id for the camera history system. For example:
```
    private int uniqueId;

```

The id represents the complete history of one texture, including the current and previous frames. 
You can also add any other data you need, for example a texture descriptor you need to store between frames.
  3. Override the `OnCreate` method. In the method, call the `OnCreate` method of the parent class, and generate the unique id. For example:
```
public override void OnCreate(BufferedRTHandleSystem owner, uint typeId)
{
    // Call the OnCreate method of the parent class
    base.OnCreate(owner, typeId);

    // Generate the unique id
    uniqueId = MakeId(0);
}

```

  4. Create public properties for the current and previous textures, so that render passes can access them. For example:
```
public RTHandle currentTexture => GetCurrentFrameRT(uniqueId);
public RTHandle previousTexture => GetPreviousFrameRT(uniqueId);

```

  5. Allocate memory for the texture. For example:
```
// Allocate 2 textures using a texture descriptor, assign them to the uniqueId, and give them a name.
AllocHistoryFrameRT(uniqueId, 2, ref textureDescriptor, "ExampleHistoryTexture");

```

  6. Implement the `Reset` method to release the history textures when the camera history system resets the type. For example:
```
public override void Reset()
{
    ReleaseHistoryFrameRT(uniqueId);
}

```



You might also need to reallocate memory each frame if a render pass writes a texture with a different size or format.
## Write to the texture
To write to the texture you created, follow these steps:
  1. To request access to the texture in a `ScriptableRenderPass` class, use the `RequestAccess` API with your camera history type. For example:
```
cameraData.historyManager.RequestAccess<ExampleHistoryType>();

```

  2. Get the texture for the current frame for writing, and convert it to a handle the render graph system can use. For example:
```
// Get the textures 
ExampleHistoryType history = cameraData.historyManager.GetHistoryForWrite<ExampleHistoryType>();

// Get the texture for the current frame
RTHandle historyTexture = history?.currentTexture;

// Convert the texture into a handle the render graph system can use
historyTexture = renderGraph.ImportTexture(historyTexture);

```



You can then write to the texture in your render pass. For more information, refer to [Using textures](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/working-with-textures.html).
## Read from the texture
To read from the texture, use the `RequestAccess` API with the camera history type you created.
You must write to the texture before you read from it.
For more information, refer to [Get data from previous frames](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/render-graph-get-previous-frames.html).
## Examples
The following is an example of a camera history type.
```
using UnityEngine;
using UnityEngine.Rendering;

public class ExampleHistoryType : CameraHistoryItem
{
    private int m_Id;

    // Add a descriptor for the size and format of the texture.
    private RenderTextureDescriptor m_Descriptor;

    // Add a hash key to track changes to the descriptor.
    private Hash128 m_DescKey;

    public override void OnCreate(BufferedRTHandleSystem owner, uint typeId)
    {
        base.OnCreate(owner, typeId);
        m_Id = MakeId(0);
    }

    // Release the history GPU resources (textures) when the camera history system resets the type.
    public override void Reset()
    {
        ReleaseHistoryFrameRT(m_Id);
    }

    public RTHandle currentTexture => GetCurrentFrameRT(m_Id);
    public RTHandle previousTexture => GetPreviousFrameRT(m_Id);

    // The render pass calls the Update method every frame, to initialize, update, or dispose of the textures.
    public void Update(RenderTextureDescriptor textureDescriptor)
    {
        // Dispose of the textures if the memory needs to be reallocated.
        if (m_DescKey != Hash128.Compute(ref textureDescriptor))
            ReleaseHistoryFrameRT(m_Id);

        // Allocate the memory for the textures if it's not already allocated.
        if (currentTexture == null)
        {
            AllocHistoryFrameRT(m_Id, 2, ref textureDescriptor, "HistoryTexture");

            // Store the descriptor and hash key for future changes.
            m_Descriptor = textureDescriptor;
            m_DescKey = Hash128.Compute(ref textureDescriptor);
        }
    }
}

```

The following is an example of a render pass that writes to the texture. You can use a URP material as the `material`, and a Scriptable Renderer Feature to inject the render pass into the **render pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Renderpipeline).
```
using UnityEngine;
using UnityEngine.Rendering;
using UnityEngine.Rendering.Universal;
using UnityEngine.Rendering.RenderGraphModule;

class WriteToHistoryTexture : ScriptableRenderPass
{
    // Property for the custom material that writes to the history texture.
    public Material m_Material;

    private class PassData
    {
        internal Material material;
    }

    public override void RecordRenderGraph(RenderGraph renderGraph, ContextContainer frameData)
    {
        var cameraData = frameData.Get<UniversalCameraData>();

        // Request access to the history texture.
        cameraData.historyManager.RequestAccess<ExampleHistoryType>();
        var history = cameraData.historyManager.GetHistoryForWrite<ExampleHistoryType>();

        if (history != null)
        {
            // Make the history a color-only texture to match the camera target.
            var historyDesc = cameraData.cameraTargetDescriptor;
            historyDesc.depthBufferBits = 0;
            historyDesc.msaaSamples = 1;
            
            // Call the Update method of the camera history type.
            history.Update(historyDesc);

            using (var builder = renderGraph.AddRasterRenderPass<PassData>("Write to history texture", out var passData))
            {
                UniversalResourceData resourceData = frameData.Get<UniversalResourceData>();
                RTHandle historyTexture = history?.currentTexture;

                // Set the render graph to render to the history texture.
                builder.SetRenderAttachment(renderGraph.ImportTexture(historyTexture), 0, AccessFlags.Write);

                passData.material = m_Material;

                builder.SetRenderFunc(static (PassData data, RasterGraphContext context) =>
                {
                    // Draw a triangle to the history texture
                    context.cmd.DrawProcedural(Matrix4x4.identity, data.material, 0, MeshTopology.Triangles, 3, 1);
                });
            }
        }
    }
}

```

## Additional resources
  * [Injecting a render pass via a Scriptable Renderer Feature](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/renderer-features/scriptable-renderer-features/scriptable-renderer-features-landing.html)
  * [Writing custom shaders in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/writing-custom-shaders-urp.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/render-graph-get-previous-frames.html)
Get data from previous frames in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/render-graph-framebuffer-fetch.html)
Get the current framebuffer from GPU memory in URP
