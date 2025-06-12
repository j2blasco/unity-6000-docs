* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/urp/anti-aliasing.html

  * [Rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/rendering-and-post-processing.html)
  * [Render pipelines](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)
  * [Using the Universal Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/universal-render-pipeline.html)
  * Add anti-aliasing in the Universal Render Pipeline


[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/URP-Config-Package.html)
Configure settings with the URP Config package
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/customizing-urp.html)
Custom rendering and post-processing in URP
# Add anti-aliasing in the Universal Render Pipeline
Aliasing is a side effect that happens when a digital sampler samples real-world information and attempts to digitize it. For example, when you sample audio or video, aliasing means that the shape of the digital signal doesn’t match the shape of the original signal. This means when Unity renders a line, it may appear jagged as the **pixels** The smallest unit in a computer image. Pixel size depends on your screen resolution. Pixel lighting is calculated at every screen pixel. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/ShadowPerformance.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#pixel) don’t align perfectly with the line’s intended path across the screen.
![An example of the rasterization process creating some aliasing.](https://docs.unity3d.com/6000.0/Documentation/uploads/urp/aliasing-example.png)  
_An example of the rasterization process creating aliasing._
To prevent aliasing, the Universal **Render Pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Renderpipeline) (URP) has multiple methods of anti-aliasing, each with their own effectiveness and resource intensity.
The anti-aliasing methods available are:
  * [Fast Approximate Anti-aliasing (FXAA)](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/anti-aliasing.html#fxaa)
  * [Subpixel Morphological Anti-aliasing (SMAA)](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/anti-aliasing.html#smaa)
  * [Temporal Anti-aliasing (TAA)](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/anti-aliasing.html#taa)
  * [Multisample Anti-aliasing (MSAA)](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/anti-aliasing.html#msaa)


## Fast Approximate Anti-aliasing (FXAA)
FXAA uses a full screen pass that smooths edges on a per-pixel level. This is the least resource intensive anti-aliasing technique in URP.
To select FXAA for a **Camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera):
  1. Select the Camera in the **Scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) view or Hierarchy window and view it in the **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector).
  2. Navigate to **Rendering** > **Anti-aliasing** , and select **Fast Approximate Anti-aliasing (FXAA)**.


**Note** : For anti-aliasing on mobile platforms, Unity recommends that you use FXAA.
## Subpixel Morphological Anti-aliasing (SMAA)
SMAA finds patterns in the borders of an image and blends the pixels on these borders according to the pattern it finds. This anti-aliasing method has much sharper results than FXAA.
To select SMAA for a Camera:
  1. Select the Camera in the **Scene view** An interactive view into the world you are creating. You use the Scene View to select and position scenery, characters, cameras, lights, and all other types of Game Object. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheSceneView.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#SceneView) or Hierarchy window and view it in the Inspector.
  2. Navigate to **Rendering** > **Anti-aliasing** , and select **Subpixel Morphological Anti-aliasing (SMAA)**.


## Temporal Anti-aliasing (TAA)
TAA uses frames from a color history buffer to smooth edges over the course of multiple frames. Because TAA calculates its effects over time, it often creates ghosting artifacts in extreme situations, such as when a **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) moves quickly in front of a surface that contrasts with it. TAA uses [motion vectors](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/features/motion-vectors.html).
To select TAA for a Camera:
  1. Select the Camera in the Scene view or Hierarchy window and view it in the Inspector.
  2. Navigate to **Rendering** > **Anti-aliasing** , and select **Temporal Anti-aliasing (TAA)**.


The following features cannot be used with TAA:
  * Multisample anti-aliasing (MSAA)
  * [Camera Stacking](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/camera-stacking.html)
  * [Dynamic Resolution](https://docs.unity3d.com/Manual/DynamicResolution.html)A Camera setting that allows you to dynamically scale individual render targets to reduce workload on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/DynamicResolution-landing.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#dynamicresolution)


## Multisample Anti-aliasing (MSAA)
MSAA samples the depth and stencil values of every pixel and combines these samples to produce the final pixel. Crucially, MSAA solves spatial aliasing issues and is better at solving triangle-edge aliasing issues than the other techniques. However, it does not fix **shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) aliasing issues such as specular or texture aliasing.
MSAA is more resource intensive than other forms of anti-aliasing on most hardware. However, when run on a tiled GPU with no **post-processing** A process that improves product visuals by applying filters and effects before the image appears on screen. You can use post-processing effects to simulate physical camera and film properties, for example Bloom and Depth of Field. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/PostProcessingOverview.html) post processing, postprocessing, postprocess  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#post-processing) anti-aliasing or custom render features in use, MSAA is a cheaper option than other anti-aliasing types.
MSAA is a hardware anti-aliasing method. This means you can use it with the other methods, as they are post-processing effects. However, you can’t use MSAA with TAA.
To enable MSAA:
  1. Open a [URP Asset](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/universalrp-asset.html) in the Inspector.
  2. Navigate to **Quality** > **Anti Aliasing (MSAA)** and select the level of MSAA you want.


For more information on the available settings, refer to the [MSAA setings in the URP Asset](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/universalrp-asset.html#quality).
**Note:** On mobile platforms that don’t support the [StoreAndResolve](https://docs.unity3d.com/ScriptReference/Rendering.RenderBufferStoreAction.StoreAndResolve.html) store action, if **Opaque Texture** is selected in the **URP Asset** , Unity ignores the **MSAA** property at runtime (as if **MSAA** is set to **Disabled**).
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/URP-Config-Package.html)
Configure settings with the URP Config package
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/customizing-urp.html)
Custom rendering and post-processing in URP
