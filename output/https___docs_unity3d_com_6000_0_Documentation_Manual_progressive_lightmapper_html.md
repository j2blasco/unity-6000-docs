* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/progressive-lightmapper.html

  * [Lighting](https://docs.unity3d.com/6000.0/Documentation/Manual/LightingOverview.html)
  * [Direct and indirect lighting](https://docs.unity3d.com/6000.0/Documentation/Manual/direct-and-indirect-lighting.html)
  * [Precalculating surface lighting with lightmaps](https://docs.unity3d.com/6000.0/Documentation/Manual/Lightmapping-landing.html)
  * [Baking lightmaps before runtime](https://docs.unity3d.com/6000.0/Documentation/Manual/Lightmapping-baking-before-runtime.html)
  * [Configuring lightmaps and baking](https://docs.unity3d.com/6000.0/Documentation/Manual/Lightmapping-configure.html)
  * Select the CPU or GPU for baking


[](https://docs.unity3d.com/6000.0/Documentation/Manual/Lightmapping-configure.html)
Configuring lightmaps and baking
[](https://docs.unity3d.com/6000.0/Documentation/Manual/Lightmapping-baked-tags.html)
Group GameObjects together in a lightmap with Baked Tags
# Select the CPU or GPU for baking
You can choose between two backends for the Progressive Lightmapper. The Progressive CPU Lightmapper backend is a backend for the Progressive Lightmapper that uses your computer’s CPU and system RAM. The Progressive GPU Lightmapper is a backend for the Progressive Lightmapper that uses your computer’s GPU and VRAM.
For information on the Progressive GPU Lightmapper backend, see the [Progressive GPU Lightmapper](https://docs.unity3d.com/6000.0/Documentation/Manual/GPUProgressiveLightmapper.html).
## GPU lightmapper
The **Progressive GPU Lightmapper** is a backend for the [Progressive Lightmapper](https://docs.unity3d.com/6000.0/Documentation/Manual/progressive-lightmapper.html) which uses your computer’s GPU and Dedicated Video Ram (VRAM) to generate baked **lightmaps** A pre-rendered texture that contains the effects of light sources on static objects in the scene. Lightmaps are overlaid on top of scene geometry to create the effect of lighting. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Lightmapping.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Lightmap) and **Light Probes** Light probes store information about how light passes through space in your scene. A collection of light probes arranged within a given space can improve lighting on moving objects and static LOD scenery within that space. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/LightProbes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#LightProbe).
## Hardware and software requirements
In order to use the Progressive GPU Lightmapper, your computer must meet these minimum specifications:
  * At least one GPU with OpenCL 1.2 support
  * At least 2GB of VRAM dedicated to that GPU
  * A CPU that supports SSE4.1 instructions


If the **Scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) you are baking requires more VRAM than is available on the designated GPU, bake times can significantly increase. See Performance for information to help you reduce the time it takes to bake your Scene.
The Progressive GPU Lightmapper does not support OpenCL CPU devices.
The Apple silicon version of the Unity Editor is not compatible with the CPU Progressive Lightmapper. However, it is compatible with the [Progressive GPU Lightmapper](https://docs.unity3d.com/6000.0/Documentation/Manual/GPUProgressiveLightmapper.html).
## Render pipeline support
See [render pipeline feature comparison](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines-feature-comparison.html) for more information about support for the Progressive Lightmapper across **render pipelines** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Renderpipeline).
## Select the Progressive Lightmapper
To select the Progressive Lightmapper:
  1. Go to **Window** > **Rendering** > **Lighting**
  2. Navigate to **Lightmapping Settings**
  3. Set **Lightmapper** A tool in Unity that bakes lightmaps according to the arrangement of lights and geometry in your scene. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Lightmapping.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Lightmapper) to **Progressive CPU** or **Progressive GPU**


You can perform many of the functions available in this window via **scripts** A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/creating-scripts.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scripts), using the [LightmapEditorSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightmapEditorSettings.html) and [Lightmapping](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Lightmapping.html) APIs.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/Lightmapping-configure.html)
Configuring lightmaps and baking
[](https://docs.unity3d.com/6000.0/Documentation/Manual/Lightmapping-baked-tags.html)
Group GameObjects together in a lightmap with Baked Tags
