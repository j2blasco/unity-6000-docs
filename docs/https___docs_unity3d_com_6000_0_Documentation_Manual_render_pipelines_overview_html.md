* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines-overview.html

  * [Rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/rendering-and-post-processing.html)
  * [Render pipelines](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)
  * Introduction to render pipelines


[](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)
Render pipelines
[](https://docs.unity3d.com/6000.0/Documentation/Manual/scriptable-render-pipeline-introduction.html)
Scriptable Render Pipeline fundamentals
# Introduction to render pipelines
A **render pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Renderpipeline) takes the objects in a **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) and displays them on-screen.
## How a render pipeline works
![Stages of a render pipeline workflow.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/BestPracticeLightingPipeline3.svg) Stages of a render pipeline workflow.
A render pipeline follows these steps:
  1. Culling, where the pipeline decides which objects from the scene to display. This usually means it removes objects that are outside the **camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera) view ([frustum culling](https://docs.unity3d.com/Manual/UnderstandingFrustum.html)) or hidden behind other objects ([occlusion culling](https://docs.unity3d.com/Manual/OcclusionCulling.html)A process that disables rendering GameObjects that are hidden (occluded) from the view of the camera. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/OcclusionCulling.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Occlusionculling)).
  2. Rendering, where the pipeline draws the objects with their correct lighting into **pixel** The smallest unit in a computer image. Pixel size depends on your screen resolution. Pixel lighting is calculated at every screen pixel. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/ShadowPerformance.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#pixel) buffers.
  3. **Post-processing** A process that improves product visuals by applying filters and effects before the image appears on screen. You can use post-processing effects to simulate physical camera and film properties, for example Bloom and Depth of Field. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/PostProcessingOverview.html) post processing, postprocessing, postprocess  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#post-processing), where the pipeline modifies the pixel buffers to generate the final output frame for the display. Example of modifications include color grading, bloom, and **depth of field** A post-processing effect that simulates the focus properties of a camera lens. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/PostProcessingOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#DepthofField).


A render pipeline repeats these steps each time Unity generates a new frame.
## Render pipelines in Unity
In Unity, you can choose between different render pipelines. Unity provides three prebuilt render pipelines with different capabilities and performance characteristics, or you can create your own.
The [Universal Render Pipeline (URP)](https://docs.unity3d.com/6000.0/Documentation/Manual/universal-render-pipeline.html) is a Scriptable Render Pipeline that you can customize. It lets you create scalable graphics across a wide range of platforms.
![URP 3D sample](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/render-pipelines-overview-urp.jpg) URP 3D sample
The [High Definition Render Pipeline (HDRP)](https://docs.unity3d.com/6000.0/Documentation/Manual/high-definition-render-pipeline.html) is a Scriptable Render Pipeline that lets you create cutting-edge, high-fidelity graphics on high-end platforms.
![HDRP 3D sample](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/render-pipelines-overview-hdrp.jpg) HDRP 3D sample
The [Built-In Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/built-in-render-pipeline.html) is a general purpose render pipeline with limited options for customization.
![Built-In Render Pipeline 2D sample](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/render-pipelines-overview-builtin.jpg) Built-In Render Pipeline 2D sample
The Scriptable Render Pipelines let you inspect and change how culling, rendering, and post-processing work directly in C#. This level of customization is also possible in the Built-In Render Pipeline when you [purchase access to the Unity engine’s source code](https://unity.com/products/source-code) in C++.
If you’re an experienced graphics developer with advanced customization needs, you can also [create your own custom render pipeline](https://docs.unity3d.com/Packages/com.unity.render-pipelines.core@17.0/manual/srp-custom.html) using Unity’s Scriptable Render Pipeline API.
Refer to [Choose a render pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/choose-a-render-pipeline.html) for more information about choosing the right pipeline for your project.
## Additional resources
  * [Introduction to Lighting and Rendering tutorial](https://learn.unity.com/tutorial/introduction-to-lighting-and-rendering-2019-3)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)
Render pipelines
[](https://docs.unity3d.com/6000.0/Documentation/Manual/scriptable-render-pipeline-introduction.html)
Scriptable Render Pipeline fundamentals
