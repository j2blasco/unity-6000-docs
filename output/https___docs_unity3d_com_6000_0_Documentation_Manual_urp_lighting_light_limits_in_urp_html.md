* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/urp/lighting/light-limits-in-urp.html

  * [Lighting](https://docs.unity3d.com/6000.0/Documentation/Manual/LightingOverview.html)
  * [Lighting in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/lighting-landing.html)
  * Light limits in URP


[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/lighting/lighting-in-urp.html)
Introduction to lighting in the Universal Render Pipeline
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/lights-placement-tool.html)
View and control a light from its perspective in URP
# Light limits in URP
If you use the default Forward [rendering path](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/rendering-paths-introduction-urp.html)The technique that a render pipeline uses to render graphics. Choosing a different rendering path affects how lighting and shading are calculated. Some rendering paths are more suited to different platforms and hardware than others. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/RenderingPaths.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#RenderingPath), the Universal **Render Pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Renderpipeline) (URP) has a maximum of 9 lights for each **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject):
  * 1 Main Light, which is a per-pixel light by default. This is the main Directional Light in your **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene), or the brightest light.
  * 8 Additional Lights, which are also per-pixel lights by default. You can set them as per-vertex lights instead.


For more information about per-pixel and per-vertex lights, refer to [Per-pixel and per-vertex lights](https://docs.unity3d.com/6000.0/Documentation/Manual/PerPixelLights.html).
There are also the following limits per **camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera):
  * Desktop and console platforms: 256 Additional Lights
  * Mobile platforms: 32 Additional Lights.
  * OpenGL ES 3.0 and earlier: 16 Additional Lights.


The Main Light is always visible per camera.
To add more lights per object or per camera, use the Forward+ or Deferred rendering paths instead. For more information, refer to [Choose a rendering path in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/rendering-paths-comparison.html)
## Additional resources
  * [Lighting settings in the URP Asset Inspector window](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/universalrp-asset.html#lighting)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/lighting/lighting-in-urp.html)
Introduction to lighting in the Universal Render Pipeline
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/lights-placement-tool.html)
View and control a light from its perspective in URP
