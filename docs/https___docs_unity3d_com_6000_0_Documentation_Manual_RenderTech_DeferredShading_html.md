* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/RenderTech-DeferredShading.html

  * [Rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/rendering-and-post-processing.html)
  * [Render pipelines](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)
  * [Using the Built-In Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/built-in-render-pipeline.html)
  * [Rendering paths in the Built-In Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/built-in-rendering-paths.html)
  * Deferred rendering path in the Built-In Render Pipeline 


[](https://docs.unity3d.com/6000.0/Documentation/Manual/RenderTech-ForwardRendering.html)
Forward rendering path in the Built-In Render Pipeline
[](https://docs.unity3d.com/6000.0/Documentation/Manual/RenderTech-VertexLit.html)
Legacy Vertex Lit rendering path in the Built-In Render Pipeline
# Deferred rendering path in the Built-In Render Pipeline
This page details the **Deferred Shading** [rendering path](https://docs.unity3d.com/6000.0/Documentation/Manual/RenderingPaths.html)The technique that a render pipeline uses to render graphics. Choosing a different rendering path affects how lighting and shading are calculated. Some rendering paths are more suited to different platforms and hardware than others. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/RenderingPaths.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#RenderingPath) in Unity’s Built-in **Render Pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Renderpipeline). See [Wikipedia: deferred shading](http://en.wikipedia.org/wiki/Deferred_shading) for an introductory technical overview of deferred shading.
## Overview
When using deferred shading, there is no limit on the number of lights that can affect a **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject). All lights are evaluated per-pixel, which means that they all interact correctly with **normal maps** A type of Bump Map texture that allows you to add surface detail such as bumps, grooves, and scratches to a model which catch the light as if they are represented by real geometry.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Normalmap), etc. Additionally, all lights can have cookies and shadows.
Deferred shading has the advantage that the processing overhead of lighting is proportional to the number of **pixels** The smallest unit in a computer image. Pixel size depends on your screen resolution. Pixel lighting is calculated at every screen pixel. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/ShadowPerformance.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#pixel) the light shines on. This is determined by the size of the light volume in the **Scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) regardless of how many GameObjects it illuminates. Therefore, performance can be improved by keeping lights small. Deferred shading also has highly consistent and predictable behaviour. The effect of each light is computed per-pixel, so there are no lighting computations that break down on large triangles.
On the downside, deferred shading has no real support for anti-aliasing and can’t handle semi-transparent GameObjects (these are rendered using [forward](https://docs.unity3d.com/6000.0/Documentation/Manual/RenderTech-ForwardRendering.html) rendering). There is also no support for the **Mesh** The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/mesh.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Mesh) Renderer’s Receive Shadows flag and **culling masks** Allows you to include or omit objects to be rendered by a Camera, by Layer.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#CullingMask) are only supported in a limited way. You can only use up to four culling masks. That is, your culling **layer mask** A value defining which layers to include or exclude from an operation, such as rendering, collision or your own code. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Layers.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#LayerMask) must at least contain all layers minus four arbitrary layers, so 28 of the 32 layers must be set. Otherwise you get graphical artifacts.
## Requirements
It requires a graphics card with Multiple Render Targets (MRT), **Shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) Model 3.0 (or later) and support for Depth **render textures** A special type of Texture that is created and updated at runtime. To use them, first create a new Render Texture and designate one of your Cameras to render into it. Then you can use the Render Texture in a Material just like a regular Texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-RenderTexture.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#RenderTexture). Most PC graphics cards made after 2006 support deferred shading, starting with GeForce 8xxx, Radeon X2400, Intel G45.
On mobile, deferred shading is supported on all devices running at least OpenGL ES 3.0.
**Note** : Deferred rendering isn’t supported when using Orthographic projection. If the **Camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera)’s projection mode is set to Orthographic, the Camera falls back to Forward rendering.
**Note** : Deferred Rendering doesn’t support Single Pass Stereo Instancing in the Built-in Render Pipeline..
## Performance considerations
The rendering overhead of real-time lights in deferred shading is proportional to the number of pixels illuminated by the light and _not_ dependent on Scene complexity. So small Point Lights or Spot Lights are very cheap to render and if they are fully or partially occluded by Scene GameObjects then they are even cheaper.
Of course, lights with shadows are much more expensive than lights without shadows. In deferred shading, shadow-casting GameObjects still need to be rendered once or more for each shadow-casting light. Furthermore, the lighting shader that applies shadows has a higher rendering overhead than the one used when shadows are disabled.
## Implementation details
Objects with Shaders that do not support deferred shading are rendered after deferred shading is complete, using the [forward rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/RenderTech-ForwardRendering.html)A rendering path that renders each object in one or more passes, depending on lights that affect the object. Lights themselves are also treated differently by Forward Rendering, depending on their settings and intensity. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/RenderTech-ForwardRendering.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#ForwardRendering) path.
The default layout of the render targets (RT0 - RT4) in the G-buffer is listed below. Data types are placed in the various channels of each render target. The channels used are shown in parentheses.
  * RT0, ARGB32 format: Diffuse color (RGB), occlusion (A).
  * RT1, ARGB32 format: **Specular color** The color of a specular highlight.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#specularcolor) (RGB), smoothness (A).
  * RT2, ARGB2101010 format: World space normal (RGB), unused (A).
  * RT3, ARGB2101010 (non-HDR) or ARGBHalf (HDR) format: Emission + lighting + **lightmaps** A pre-rendered texture that contains the effects of light sources on static objects in the scene. Lightmaps are overlaid on top of scene geometry to create the effect of lighting. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Lightmapping.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Lightmap) + **reflection probes** A rendering component that captures a spherical view of its surroundings in all directions, rather like a camera. The captured image is then stored as a Cubemap that can be used by objects with reflective materials. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ReflectionProbe.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#ReflectionProbe) buffer.
  * Depth+**Stencil buffer** A memory store that holds an 8-bit per-pixel value. In Unity, you can use a stencil buffer to flag pixels, and then only render to pixels that pass the stencil operation. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-RenderTexture.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#stencilbuffer).


So the default G-buffer layout is 160 bits/pixel (non-HDR) or 192 bits/pixel (HDR).
If using the [Shadowmask](https://docs.unity3d.com/6000.0/Documentation/Manual/lighting-mode.html#shadowmask) or Distance Shadowmask modes for Mixed lighting, a fifth target is used:
  * RT4, ARGB32 format: Light occlusion values (RGBA).


And thus the G-buffer layout is 192 bits/pixel (non-HDR) or 224 bits/pixel (HDR).
If the hardware does not support five concurrent rendertargets then objects using shadowmasks will fallback to the forward rendering path. Emission+lighting buffer (RT3) is logarithmically encoded to provide greater dynamic range than is usually possible with an ARGB32 texture, when the Camera is not using **HDR** high dynamic range  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#HDR).
Note that when the Camera is using HDR rendering, there’s no separate rendertarget being created for Emission+lighting buffer (RT3); instead the rendertarget that the Camera renders into (that is, the one that is passed to the image effects) is used as RT3.
### G-Buffer pass
The G-buffer pass renders each GameObject once. Diffuse and specular colors, surface smoothness, world space normal, and emission+ambient+reflections+lightmaps are rendered into G-buffer textures. The G-buffer textures are setup as global shader properties for later access by shaders (_CameraGBufferTexture0 .._ CameraGBufferTexture3 names).
### Lighting pass
The lighting pass computes lighting based on G-buffer and depth. Lighting is computed in screen space, so the time it takes to process is independent of Scene complexity. Lighting is added to the emission buffer.
Point Lights and Spot Lights that do not cross the Camera’s near plane are rendered as 3D shapes, with the Z buffer’s test against the Scene enabled. This makes partially or fully occluded Point Lights and Spot Lights very cheap to render. Directional Lights and Point or Spot Lights that cross the near plane are rendered as fullscreen **quads** A primitive object that resembles a plane but its edges are only one unit long, it uses only 4 vertices, and the surface is oriented in the XY plane of the local coordinate space. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/PrimitiveObjects.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Quad).
If a light has shadows enabled then they are also rendered and applied in this pass. Note that shadows do not come for “free”; shadow casters need to be rendered and a more complex light shader must be applied.
The only lighting model available is Standard. If you need a different lighting model, you can create a customized version of the default deferred shader file. Follow these steps:
  1. [Download the source code](https://docs.unity3d.com/6000.0/Documentation/Manual/StandardShaderMakeYourOwn.html) for the Built-In Render Pipeline shaders.
  2. Find the `Internal-DeferredShading.shader` file in the `DefaultResourcesExtra` folder.
  3. Edit the file to change the lighting model.
  4. In the **Project** window, add the file to your **Assets** folder, in a folder called **Resources**.
  5. From the main menu, select **Edit** > **Project Settings** > **Graphics**.
  6. In the **Built-in Shader Settings** section, set **Deferred** to **Custom shader** , then select your shader file.


* * *
  * 2017–06–08 Page published 
  * Light Modes (**Shadowmask** A Texture that shares the same UV layout and resolution with its corresponding lightmap. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/lighting-mode.html#shadowmask)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shadowmask) and **Distance Shadowmask** A version of the Shadowmask lighting mode that includes high quality shadows cast from static GameObjects onto dynamic GameObjects. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/lighting-mode.html#shadowmask)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#DistanceShadowmask)) added in 5.6


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/RenderTech-ForwardRendering.html)
Forward rendering path in the Built-In Render Pipeline
[](https://docs.unity3d.com/6000.0/Documentation/Manual/RenderTech-VertexLit.html)
Legacy Vertex Lit rendering path in the Built-In Render Pipeline
