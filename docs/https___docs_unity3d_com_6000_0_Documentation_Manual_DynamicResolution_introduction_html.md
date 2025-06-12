* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/DynamicResolution-introduction.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [Cameras](https://docs.unity3d.com/6000.0/Documentation/Manual/Cameras.html)
  * [Changing resolution scale](https://docs.unity3d.com/6000.0/Documentation/Manual/resolution-scale.html)
  * [Dynamic Resolution](https://docs.unity3d.com/6000.0/Documentation/Manual/DynamicResolution-landing.html)
  * Introduction to Dynamic Resolution


[](https://docs.unity3d.com/6000.0/Documentation/Manual/DynamicResolution-landing.html)
Dynamic Resolution
[](https://docs.unity3d.com/6000.0/Documentation/Manual/DynamicResolution-control.html)
Control scaling with Dynamic Resolution
# Introduction to Dynamic Resolution
Dynamic resolution is a **Camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera) setting that allows you to dynamically scale individual render targets, to reduce workload on the GPU. For example, you can gradually scale down the resolution to maintain a consistent frame rate. If scaled gradually, **dynamic resolution** A Camera setting that allows you to dynamically scale individual render targets to reduce workload on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/DynamicResolution-landing.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#dynamicresolution) can be almost unnoticeable.
## Render pipeline compatibility
Dynamic resolution support depends on which [render pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Renderpipeline) your project uses.
**Feature** | **Universal Render Pipeline (URP)** | **High Definition Render Pipeline (HDRP)** | **Built-in Render Pipeline**  
---|---|---|---  
**Dynamic resolution** | Yes (1) | Yes (2) | Yes (1)  
**Notes** :
  1. The [Built-in Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/built-in-render-pipeline.html), and the [Universal Render Pipeline (URP)](https://docs.unity3d.com/6000.0/Documentation/Manual/universal-render-pipeline.html) both support dynamic resolution as described in this document.
  2. The [High Definition Render Pipeline (HDRP)](https://docs.unity3d.com/6000.0/Documentation/Manual/high-definition-render-pipeline.html) supports dynamic resolution, but you enable and use it in a different way. For information on dynamic resolution in HDRP, see [Dynamic resoluton in HDRP](https://docs.unity3d.com/Packages/com.unity.render-pipelines.high-definition@latest?subfolder=/manual/Dynamic-Resolution.html).


## Supported platforms
Unity supports dynamic resolution on iOS, macOS and tvOS (Metal only), Android (Vulkan only), Windows Standalone (DirectX 12 only), and UWP (DirectX 12 only).
## Impact on render targets
With dynamic resolution, Unity does not re-allocate render targets. Conceptually, Unity scales the render target; however, in reality, Unity uses aliasing, and the scaled-down render target only uses a small portion of the original render target. Unity allocates the render targets at their full resolution, and then the dynamic resolution system scales them down and back up again, using a portion of the original target instead of re-allocating a new target.
## Additional resources
  * [FrameTimingManager API reference](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FrameTimingManager.html)
  * [FrameTimingManager User Manual documentation](https://docs.unity3d.com/6000.0/Documentation/Manual/frame-timing-manager.html)
  * [ScalableBufferManager API reference](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScalableBufferManager.html)
  * [RenderTexture API reference](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/DynamicResolution-landing.html)
Dynamic Resolution
[](https://docs.unity3d.com/6000.0/Documentation/Manual/DynamicResolution-control.html)
Control scaling with Dynamic Resolution
