* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/urp/render-graph-get-previous-frames.html

  * [Rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/rendering-and-post-processing.html)
  * [Render pipelines](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)
  * [Using the Universal Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/universal-render-pipeline.html)
  * [Custom rendering and post-processing in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/customizing-urp.html)
  * [Render graph system in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/render-graph.html)
  * [Frame data in the render graph system in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/render-graph-frame-data.html)
  * Get data from previous frames in URP


[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/accessing-frame-data.html)
Get data from the current frame in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/render-graph-add-textures-to-camera-history.html)
Add textures to the camera history
# Get data from previous frames in URP
To fetch the previous frames that the **camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera) rendered in the Universal **Render Pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Renderpipeline) (URP), use the [`UniversalCameraData.historyManager`](https://docs.unity3d.com/Packages/com.unity.render-pipelines.universal@17.2/api/UnityEngine.Rendering.Universal.UniversalCameraData.html) API. These textures are sometimes called history textures or history buffers.
The frames are the output of the GPU rendering pipeline, so they don’t include any processing that occurs after GPU rendering, such as **post-processing** A process that improves product visuals by applying filters and effects before the image appears on screen. You can use post-processing effects to simulate physical camera and film properties, for example Bloom and Depth of Field. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/PostProcessingOverview.html) post processing, postprocessing, postprocess  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#post-processing) effects.
To fetch previous frames from outside a scriptable render pass, refer to [Get data from previous frames in a script](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/render-graph-get-previous-frames.html#get-data-from-previous-frames-in-a-script).
Follow these steps:
  1. In the `RecordRenderGraph` method, get the `UniversalCameraData` object from the `ContextContainer` object. For example:
```
public override void RecordRenderGraph(RenderGraph renderGraph, ContextContainer frameContext)
{
    UniversalCameraData cameraData = frameContext.Get<UniversalCameraData>();
}    

```

  2. To request access to either the color textures or the depth textures in the rendering history, use the `RequestAccess` API. For example:
```
// Request access to the color textures
cameraData.historyManager.RequestAccess<RawColorHistory>();

```

Use `RawDepthHistory` instead to request access to the depth textures.
  3. Get one of the previous textures. For example:
```
// Get the previous textures 
RawColorHistory history = cameraData.historyManager.GetHistoryForRead<RawColorHistory>();

// Get the first texture, which the camera rendered in the previous frame
RTHandle historyTexture = history?.GetPreviousTexture(0);

```

  4. Convert the texture into a handle the render graph system can use. For example:
```
passData.historyTexture = renderGraph.ImportTexture(historyTexture);

```



You can then read the texture in the render pass.
For more information about using the `historyManager` API, refer to [`UniversalCameraData.historyManager`](https://docs.unity3d.com/Packages/com.unity.render-pipelines.universal@17.2/api/UnityEngine.Rendering.Universal.UniversalCameraData.html).
## Example
The following is a Scriptable Renderer Feature that creates a material and uses the previous frame as the material’s texture.
To use the example, follow these steps:
  1. Create a URP **shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) that samples a texture called `_BaseMap`. For an example, refer to [Drawing a texture](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/writing-shaders-urp-unlit-texture.html).
  2. Create a material from the shader.
  3. Create a new C# script called `RenderLastFrameInMaterial.cs`, paste the following code into it, and save the file.
  4. In the active URP renderer, [add the Scriptable Renderer Feature](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/urp-renderer-feature.html).
  5. In the ****Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector)** window of the active URP renderer, in the **Render Last Frame In Material** section of the Scriptable Renderer Feature you added in step 4, assign the material you created in step 2 to the **Object Material** field.

```
using UnityEngine;
using UnityEngine.Rendering;
using UnityEngine.Rendering.Universal;
using UnityEngine.Rendering.RenderGraphModule;
public class RenderLastFrameInMaterial : ScriptableRendererFeature
{
    public Material objectMaterial;
    CustomRenderPass renderLastFrame;

    public override void Create()
    {
        renderLastFrame = new CustomRenderPass();
        renderLastFrame.renderPassEvent = RenderPassEvent.BeforeRenderingOpaques;
    }

    public override void AddRenderPasses(ScriptableRenderer renderer, ref RenderingData renderingData)
    {
        renderLastFrame.passMaterial = objectMaterial;
        renderer.EnqueuePass(renderLastFrame);
    }

    class CustomRenderPass : ScriptableRenderPass
    {
        public Material passMaterial;

        public class PassData
        {
            internal Material material;
            internal TextureHandle historyTexture;
        }

        public override void RecordRenderGraph(RenderGraph renderGraph, ContextContainer contextData)
        {
            UniversalCameraData cameraData = contextData.Get<UniversalCameraData>();

            // Return if the history manager isn't available
            // For example, there are no history textures during the first frame
            if (cameraData.historyManager == null) { return; }
  
            // Request access to the color and depth textures
            cameraData.historyManager.RequestAccess<RawColorHistory>();

            using (var builder = renderGraph.AddRasterRenderPass<PassData>("Get last frame", out var passData))
            {
                UniversalResourceData resourceData = contextData.Get<UniversalResourceData>();

                // Set the render graph to render to the active color texture
                builder.SetRenderAttachment(resourceData.activeColorTexture, 0, AccessFlags.Write);

                // Add the material to the pass data
                passData.material = passMaterial;
                
                // Get the color texture the camera rendered to in the previous frame
                RawColorHistory history = cameraData.historyManager.GetHistoryForRead<RawColorHistory>();
                RTHandle historyTexture = history?.GetPreviousTexture(0);
                passData.historyTexture = renderGraph.ImportTexture(historyTexture);

                builder.SetRenderFunc(static (PassData data, RasterGraphContext context) =>
                {
                    // Set the material to use the texture
                    data.material.SetTexture("_BaseMap", data.historyTexture);
                });
            }
        }
    }
}

```

## Get data from previous frames in a script
To get data from previous frames in a script, for example a `MonoBehaviour`, do the following:
  1. Use the Scriptable Render Pipeline (SRP) Core [`RequestAccess`](https://docs.unity3d.com/Packages/com.unity.render-pipelines.core@17.0/api/UnityEngine.Rendering.IPerFrameHistoryAccessTracker.html#UnityEngine_Rendering_IPerFrameHistoryAccessTracker_RequestAccess__1) API to request the texture.
  2. Use the [`UniversalAdditionalCameraData.history`](https://docs.unity3d.com/Packages/com.unity.render-pipelines.universal@17.2/api/UnityEngine.Rendering.Universal.UniversalAdditionalCameraData.html#UnityEngine_Rendering_Universal_UniversalAdditionalCameraData_history) API to get the data.


To make sure Unity finishes rendering the frame first, use the `UniversalAdditionalCameraData.history` API in the [`LateUpdate`](https://docs.unity3d.com/ScriptReference/MonoBehaviour.LateUpdate.html) method.
For more information, refer to the following in the Scriptable Render Pipeline (SRP) Core package:
  * [`ICameraHistoryReadAccess`](https://docs.unity3d.com/Packages/com.unity.render-pipelines.core@17.0/api/UnityEngine.Rendering.ICameraHistoryReadAccess.html)
  * [`IPerFrameHistoryTracker`](https://docs.unity3d.com/Packages/com.unity.render-pipelines.core@17.0/api/UnityEngine.Rendering.IPerFrameHistoryAccessTracker.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/accessing-frame-data.html)
Get data from the current frame in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/render-graph-add-textures-to-camera-history.html)
Add textures to the camera history
