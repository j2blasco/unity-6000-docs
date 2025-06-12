* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/lighting-configuration-workflow.html

  * [Lighting](https://docs.unity3d.com/6000.0/Documentation/Manual/LightingOverview.html)
  * Lighting configuration workflow


[](https://docs.unity3d.com/6000.0/Documentation/Manual/LightingInUnity.html)
Introduction to lighting
[](https://docs.unity3d.com/6000.0/Documentation/Manual/lighting-light-sources.html)
Light sources
# Lighting configuration workflow
To set up lighting in Unity, follow these steps:
  1. [Choose a render pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/lighting-configuration-workflow.html#choose-a-render-pipeline)
  2. [Configure lighting](https://docs.unity3d.com/6000.0/Documentation/Manual/lighting-configuration-workflow.html#configure-lighting)
  3. [Fine-tune your scene lighting](https://docs.unity3d.com/6000.0/Documentation/Manual/lighting-configuration-workflow.html#fine-tune-your-scene-lighting)


## Choose a render pipeline
Unity provides **render pipelines** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Renderpipeline) that differ in customization and lighting features:
  * [Built-in Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/lighting-birp.html) (not scriptable)
  * [Universal Render Pipeline (URP)](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/lighting/lighting-in-urp.html)
  * [High-Definition Render Pipeline (HDRP)](https://docs.unity3d.com/Packages/com.unity.render-pipelines.high-definition@latest?subfolder=/manual/Light-Component.html)
  * Custom Scriptable Render Pipeline (SRP)


For more information on render pipeline selection, refer to [choose a render pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/choose-a-render-pipeline.html).
## Configure lighting
  1. Choose baked GI, realtime GI, mixed baked and realtime GI, or opt for no GI.
For more information, refer to [Lighting Settings Asset Inspector window reference](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LightingSettings.html#MixedLighting)
  2. Choose one of the following Lighting Modes:
     * Baked Indirect
     * Subtractive
     * Shadowmask
     * Distance Shadowmask
For more information, refer to [Lighting Mode](https://docs.unity3d.com/6000.0/Documentation/Manual/lighting-mode.html).


## Fine-tune your scene lighting
To fine-tune your **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) lighting, follow these tasks based on project requirements:
  1. Add [baked, realtime, or mixed lights](https://docs.unity3d.com/6000.0/Documentation/Manual/LightModes-introduction.html).
  2. Optionally configure emissive surfaces with [Baked GI or Realtime GI](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LightmapParameters.html).
  3. Add baked, realtime, or custom [Reflection Probes](https://docs.unity3d.com/6000.0/Documentation/Manual/ReflectionProbes.html)A rendering component that captures a spherical view of its surroundings in all directions, rather like a camera. The captured image is then stored as a Cubemap that can be used by objects with reflective materials. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ReflectionProbe.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#ReflectionProbe).
  4. If a GI mode is set, add [Light Probes](https://docs.unity3d.com/6000.0/Documentation/Manual/LightProbes-landing.html)Light probes store information about how light passes through space in your scene. A collection of light probes arranged within a given space can improve lighting on moving objects and static LOD scenery within that space. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/LightProbes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#LightProbe). You can also add [Light Probe Proxy Volumes (LPPVs)](https://docs.unity3d.com/6000.0/Documentation/Manual/LightProbeProxyVolume-landing.html).


## Additional resources
  * [Add light emission to a material](https://docs.unity3d.com/6000.0/Documentation/Manual/StandardShaderMaterialParameterEmission.html)
  * [Reflection Probe Inspector window reference](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ReflectionProbe.html)
  * [Light Probes](https://docs.unity3d.com/6000.0/Documentation/Manual/LightProbes.html)
  * [SRP Core](https://docs.unity3d.com/Packages/com.unity.render-pipelines.core@latest)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/LightingInUnity.html)
Introduction to lighting
[](https://docs.unity3d.com/6000.0/Documentation/Manual/lighting-light-sources.html)
Light sources
