* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/urp/features/rendering-layers-introduction.html

  * [Lighting](https://docs.unity3d.com/6000.0/Documentation/Manual/LightingOverview.html)
  * [Lighting in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/lighting-landing.html)
  * [Rendering Layers in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/features/rendering-layers.html)
  * Introduction to Rendering Layers in URP


[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/features/rendering-layers.html)
Rendering Layers in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/features/rendering-layers-lights.html)
Enable Rendering Layers for Lights in URP
# Introduction to Rendering Layers in URP
The Rendering Layers feature lets you configure certain Lights to affect only specific **GameObjects** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject).
For example, in the following illustration, Light `A` affects Sphere `D`, but not Sphere `C`. Light `B` affects Sphere `C`, but not Sphere `D`.
![Light A affects Sphere D, but not Sphere C. Light B affects Sphere C, but not Sphere D.](https://docs.unity3d.com/6000.0/Documentation/uploads/urp/lighting/rendering-layers/rendering-layers-example.png) Light A affects Sphere D, but not Sphere C. Light B affects Sphere C, but not Sphere D.
## Limitations
This feature has the following limitations:
  * Rendering Layers are not supported on OpenGL and OpenGL ES API.


##  Performance
This section contains information related to the impact of Rendering Layers on performance.
  * Keep the Rendering Layer count as small as possible. Avoid creating Rendering Layers that you don’t use in the project.
  * When using Rendering Layers for decals, increasing the layer count increases the required memory bandwidth and decreases the performance.
  * When using Rendering Layers only for Lights in the Forward **Rendering Path** The technique that a render pipeline uses to render graphics. Choosing a different rendering path affects how lighting and shading are calculated. Some rendering paths are more suited to different platforms and hardware than others. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/RenderingPaths.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#RenderingPath), the performance impact is insignificant.
  * Performance impact grows more significantly when the Rendering Layer count exceeds a multiple of 8. For example: increasing the layer count from 8 to 9 layers has a bigger relative impact than increasing the layer count from 9 to 10 layers. The same consideration applies to increasing the count from 16 to 17, from 24 to 25 and so on.


## Additional resources
  * [How to use Rendering Layers](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/features/rendering-layers.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/features/rendering-layers.html)
Rendering Layers in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/features/rendering-layers-lights.html)
Enable Rendering Layers for Lights in URP
