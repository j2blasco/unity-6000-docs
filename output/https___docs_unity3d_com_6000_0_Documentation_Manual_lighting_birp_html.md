* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/lighting-birp.html

  * [Lighting](https://docs.unity3d.com/6000.0/Documentation/Manual/LightingOverview.html)
  * Lighting in the Built-In Render Pipeline


[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/light-component.html)
Light component Inspector window reference for URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/PerPixelLights-BuiltIn.html)
Per-pixel and per-vertex lights in the Built-In Render Pipeline
# Lighting in the Built-In Render Pipeline
Resources and approaches for lighting in the Built-In **Render Pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Renderpipeline).
**Page** | **Description**  
---|---  
[Per-pixel and per-vertex lights in the Built-In Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/PerPixelLights-BuiltIn.html) | Learn about how Unity categorizes Light components so they light objects per-pixel or per-vertex.  
[Emit light from a GameObject](https://docs.unity3d.com/6000.0/Documentation/Manual/lighting-emissive-materials.html) | Make a material emissive so that it emits light across its surface area.  
[Create cookies](https://docs.unity3d.com/6000.0/Documentation/Manual/creating-cookies-built-in-render-pipeline.html) | Create a cookie by creating a grayscale texture, importing the texture into Unity, then converting the brightness of the texture to alpha.  
[Customize how shaders contribute lightmap data](https://docs.unity3d.com/6000.0/Documentation/Manual/MetaPass.html) | Make **shaders** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) compatible with **lightmap** A pre-rendered texture that contains the effects of light sources on static objects in the scene. Lightmaps are overlaid on top of scene geometry to create the effect of lighting. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Lightmapping.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Lightmap) textures.  
[Configure shadow resolution](https://docs.unity3d.com/6000.0/Documentation/Manual/shadow-resolution-birp.html) | Set the resolution of the shadow map a Light component generates.  
[Configure a GameObject to sample more Light Probes](https://docs.unity3d.com/6000.0/Documentation/Manual/LightProbeProxyVolume-landing.html) | To make lighting more realistic, use **Light Probe** Light probes store information about how light passes through space in your scene. A collection of light probes arranged within a given space can improve lighting on moving objects and static LOD scenery within that space. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/LightProbes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#LightProbe) Proxy Volumes to configure a **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) to sample multiple Light Probes.  
[Blend Reflection Probes](https://docs.unity3d.com/6000.0/Documentation/Manual/blend-reflection-probes-birp.html) | Enable Unity gradually fading between the **cubemap** A collection of six square textures that can represent the reflections in an environment or the skybox drawn behind your geometry. The six squares form the faces of an imaginary cube that surrounds an object; each face represents the view along the directions of the world axes (up, down, left, right, forward and back). [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Cubemap-landing.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Cubemap) textures from different **Reflection Probes** A rendering component that captures a spherical view of its surroundings in all directions, rather like a camera. The captured image is then stored as a Cubemap that can be used by objects with reflective materials. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ReflectionProbe.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#ReflectionProbe), as a reflective GameObject passes between them.  
[Optimize lighting](https://docs.unity3d.com/6000.0/Documentation/Manual/lighting-optimize-builtin.html) | Avoid Unity using multiple render passes to render GameObjects, or doing too much work to render lighting.  
[Light component Inspector window reference](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Light.html) | Explore the properties and settings in the Light component **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector) window to customize settings specific to the Built-In Render Pipeline.  
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/light-component.html)
Light component Inspector window reference for URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/PerPixelLights-BuiltIn.html)
Per-pixel and per-vertex lights in the Built-In Render Pipeline
