* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/urp/rendering-paths-comparison.html

  * [Rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/rendering-and-post-processing.html)
  * [Render pipelines](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)
  * [Using the Universal Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/universal-render-pipeline.html)
  * [Get started with URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/introduction-landing.html)
  * [Universal Render Pipeline fundamentals](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/urp-concepts.html)
  * [Rendering paths in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/rendering-paths-landing.html)
  * Choose a rendering path in URP


[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/rendering-paths-introduction-urp.html)
Introduction to rendering paths in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/rendering-paths-set.html)
Set the rendering path in URP
# Choose a rendering path in URP
Deciding on which [rendering path](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/rendering-paths-introduction-urp.html)The technique that a render pipeline uses to render graphics. Choosing a different rendering path affects how lighting and shading are calculated. Some rendering paths are more suited to different platforms and hardware than others. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/RenderingPaths.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#RenderingPath) is most suitable for your Universal **Render Pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Renderpipeline) (URP) project depends on the type of project, and on the target hardware.
Use the default **Forward rendering** A rendering path that renders each object in one or more passes, depending on lights that affect the object. Lights themselves are also treated differently by Forward Rendering, depending on their settings and intensity. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/RenderTech-ForwardRendering.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#ForwardRendering) path if you don’t have many lights in the **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) or you’re rendering on a mobile or low-end platform, because Unity limits both the number of lights and the number of per-pixel lights.
Choose the Forward+ rendering path in the following cases:
  * You have many lights in your scene, and the Deferred rendering path renders too slowly on the platform you build for.
  * You need to blend more than 2 **Reflection Probes** A rendering component that captures a spherical view of its surroundings in all directions, rather like a camera. The captured image is then stored as a Cubemap that can be used by objects with reflective materials. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ReflectionProbe.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#ReflectionProbe).
  * You use the [Entities package](https://docs.unity3d.com/Packages/com.unity.entities@1.3/manual/index.html).


Choose the Deferred rendering path in the following cases:
  * You don’t need to use [Rendering Layers](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/features/rendering-layers.html). URP renders an extra G-buffer render target if you use Rendering Layers in the Deferred rendering path, which might impact performance.
  * You don’t need accurate **terrain** The landscape in your scene. A Terrain GameObject adds a large flat plane to your scene and you can use the Terrain’s Inspector window to create a detailed landscape. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-UsingTerrains.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Terrain) blending. For more information, refer to [Introduction to the deferred rendering path](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/rendering/deferred-rendering-path-introduction.html).


Avoid using lights with a Subtractive or **Shadowmask** A Texture that shares the same UV layout and resolution with its corresponding lightmap. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/lighting-mode.html#shadowmask)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shadowmask) [Lighting Mode](https://docs.unity3d.com/6000.0/Documentation/Manual/lighting-mode-landing.html) with the Deferred rendering path, because these lights are optimized only for the Forward rendering path.
Unity falls back to a different rendering path in the following situations:
  * If you select the Deferred rendering path but a **shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) doesn’t support **deferred shading** A rendering path in the Built-in Render Pipeline that places no limit on the number of Lights that can affect a GameObject. All Lights are evaluated per-pixel, which means that they all interact correctly with normal maps and so on. Additionally, all Lights can have cookies and shadows. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/RenderTech-DeferredShading.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Deferredshading). Unity renders the **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) using a Forward rendering path at the end of rendering.
  * If the GPU on the device you build for doesn’t support the rendering path you select. Unity falls back to a different rendering path.


## Rendering path comparison
The following table lists the differences between the rendering paths in URP.
**Feature** | **Forward** | **Forward+** | **Deferred**  
---|---|---|---  
Mobile performance | Low performance impact. | Low performance impact. | High performance impact, because Unity adds extra render passes to render the G-buffer.  
Render passes per object | 1 | 1 | 1  
[Realtime lights per object](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/lighting/light-limits-in-urp.html) | 9 | Unlimited | Unlimited for opaque objects. 9 for transparent objects. |   
[Realtime lights per camera](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/lighting/light-limits-in-urp.html) | Up to 257 depending on the platform. | Up to 256 depending on the platform. The Forward+ Rendering Path treats the Main Light and Additional Lights the same way, so the per-camera limits are one light less. | Up to 257 depending on the platform.  
Per-vertex lights | Yes | No | No  
Disable the Main Light | Yes | No | No  
Per-pixel normals | Accurate, with no encoding. | Accurate, with no encoding. | Less accurate encoded normals, or you can select more accurate but slower normals. For more information, refer to [G-buffer layout in the Deferred rendering path](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/rendering/g-buffer-layout.html).  
[Multisample anti-aliasing (MSAA)](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/anti-aliasing.html) | Yes | Yes | No  
[Camera stacking](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/camera-stacking.html) | Yes | Yes | Yes, but the Base **Camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera) uses the Deferred rendering path, and Overlay Cameras use the Forward rendering path. For more information, refer to [Introduction to camera render types](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/camera-types-and-render-type-introduction.html).  
## Additional resources
  * [Light limits in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/lighting/light-limits-in-urp.html)
  * [Per-pixel and per-vertex lights](https://docs.unity3d.com/6000.0/Documentation/Manual/PerPixelLights.html)
  * [Rendering paths in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/rendering-paths-introduction-urp.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/rendering-paths-introduction-urp.html)
Introduction to rendering paths in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/rendering-paths-set.html)
Set the rendering path in URP
