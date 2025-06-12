* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/urp/customize/blit-overview.html

  * [Rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/rendering-and-post-processing.html)
  * [Render pipelines](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)
  * [Using the Universal Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/universal-render-pipeline.html)
  * [Custom rendering and post-processing in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/customizing-urp.html)
  * Blit in URP


[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/renderer-features/custom-rendering-pass-workflow-in-urp.html)
Custom render pass workflow in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/render-graph.html)
Render graph system in URP
# Blit in URP
To **blit** A shorthand term for “bit block transfer”. A blit operation is the process of transferring blocks of data from one place in memory to another.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#blit) from one texture to another in a custom render pass in the Universal **Render Pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Renderpipeline) (URP), use the [Blitter API](https://docs.unity3d.com/Packages/com.unity.render-pipelines.core@latest?subfolder=/api/UnityEngine.Rendering.Blitter.html) from the Core Scriptable Render Pipeline (SRP).
The **shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) you use with the `Blitter` API must be a hand-coded shader. [Shader Graph](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-graph.html) shaders aren’t compatible with the `Blitter` API.
**Note:** Don’t use the `CommandBuffer.Blit` or `Graphics.Blit` APIs, or APIs that use them internally such as `RenderingUtils.Blit`. These APIs might break **XR** An umbrella term encompassing Virtual Reality (VR), Augmented Reality (AR) and Mixed Reality (MR) applications. Devices supporting these forms of interactive applications can be referred to as XR devices. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/XR.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#XR) rendering, and aren’t compatible with native render passes.
For example in the `Execute` function in a render pass, add the following:
```
{
    Blitter.BlitCameraTexture(commandBuffer, sourceTexture, destinationTexture, materialToUse, passNumber);
}

```

For a full example, refer to [Example of a Scriptable Renderer Feature in Compatibility Mode](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/renderer-features/create-custom-renderer-feature.html).
## Additional resources
  * The blit examples in the [URP RenderGraph Samples](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/package-sample-urp-package-samples.html)
  * [Custom render pass workflow](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/renderer-features/custom-rendering-pass-workflow-in-urp.html)
  * [Textures in the Render Graph system](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/working-with-textures.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/renderer-features/custom-rendering-pass-workflow-in-urp.html)
Custom render pass workflow in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/render-graph.html)
Render graph system in URP
