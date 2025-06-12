* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/urp/requirements.html

  * [Rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/rendering-and-post-processing.html)
  * [Render pipelines](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)
  * [Using the Universal Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/universal-render-pipeline.html)
  * Requirements and compatibility for URP


[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/urp-introduction.html)
Introduction to the Universal Render Pipeline
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/whats-new/urp-whats-new.html)
What's new in URP 17 (Unity 6)
# Requirements and compatibility for URP
This page contains information on system requirements and compatibility of this package.
## Unity Editor compatibility
Since the release of Unity 2021.1, graphics packages are [core Unity packages](https://docs.unity3d.com/6000.0/Documentation/Manual/pack-core).
For each release of Unity (alpha, beta, or patch release), the main Unity installer contains the up-to-date versions of the following graphics packages: SRP Core, URP, HDRP, **Shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) Graph, and VFX Graph. Since the release of Unity 2021.1, the Package Manager shows only the major revisions of the graphics packages (version 11.0.0 for all Unity 2021.1.x releases and version 12.0.0 for all Unity 2021.2.x releases).
You can install a different version of a graphics package from disk using the Package Manager, or by modifying the `manifest.json` file.
## Render pipeline compatibility
Projects made using URP are not compatible with the High Definition Render Pipeline (HDRP) or the Built-in Render Pipeline. Before you start development, you must decide which render pipeline to use in your Project. For information on choosing a render pipeline, refer to the [Render Pipelines](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Renderpipeline) page.
## Graphics API compatibility
URP supports the following graphics APIs:
  * DirectX 11 (feature level 11_0 and later)
  * DirectX 12
  * Vulkan
  * Metal
  * OpenGL ES 3.0 and later
  * OpenGL Core
  * WebGL2
  * WebGPU (experimental)


## Unity Player system requirements
This package does not add any extra platform-specific requirements. General system requirements for the Unity Player apply. For more information on Unity system requirements, check the [System requirements for Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/system-requirements.html).
## Additional resources
  * [Render pipeline feature comparison reference](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines-feature-comparison.html)
  * [Hardware requirements for the Built-In Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/RenderTech-HardwareRequirements.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/urp-introduction.html)
Introduction to the Universal Render Pipeline
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/whats-new/urp-whats-new.html)
What's new in URP 17 (Unity 6)
