* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/urp/renderer-feature-decal.html

  * [Visual effects](https://docs.unity3d.com/6000.0/Documentation/Manual/visual-effects.html)
  * [Decals and projectors](https://docs.unity3d.com/6000.0/Documentation/Manual/visual-effects-decals.html)
  * [Decals in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/renderer-feature-decal-landing.html)
  * Introduction to decals in URP


[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/renderer-feature-decal-landing.html)
Decals in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/renderer-feature-decal-create.html)
Create a decal via a Decal Renderer Feature in URP
# Introduction to decals in URP
## Decal Renderer Feature
With the Decal Renderer Feature, Unity can project specific Materials (decals) onto other objects in the **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene). The decals interact with the scene’s lighting and wrap around Meshes.
![Sample scene without decals](https://docs.unity3d.com/6000.0/Documentation/uploads/urp/decal/decal-sample-without.png)  
_Sample scene without decals_
![Sample scene with decals](https://docs.unity3d.com/6000.0/Documentation/uploads/urp/decal/decal-sample-with.png)  
_Sample scene with decals. The decals hide the seams between materials and add artistic details._
For examples of how to use Decals, refer to the [Decals samples in URP Package Samples](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/package-sample-urp-package-samples.html#decals).
### Limitations
This feature has the following limitations:
  * The decal projection does not work on transparent surfaces.


## Decal Projector
The Decal Projector component lets Unity project decals onto other objects in the scene. A Decal Projector component must use a Material with the [Decal Shader Graph](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/decal-shader.html) assigned (`Shader Graphs/Decal`).
## Performance
Decals do not support the **SRP Batcher** by design because they use Material property blocks. To reduce the number of draw calls, decals can be batched together using GPU instancing. If the decals in your scene use the same Material, and if the Material has the **Enable GPU Instancing** property turned on, Unity instances the Materials and reduces the number of draw calls.
To reduce the number of Materials necessary for decals, put multiple decal textures into one texture (atlas). Use the UV offset properties on the decal projector to determine which part of the atlas to display.
The following image shows an example of a decal atlas.
![Decal Atlas](https://docs.unity3d.com/6000.0/Documentation/uploads/urp/decal/decal-atlas.png)   
_left: decal atlas with four decals. Right: a decal projector is projecting one of them. If the decal Material has GPU instancing enabled, any instance of the four decals is rendered in a single instanced draw call._
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/renderer-feature-decal-landing.html)
Decals in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/renderer-feature-decal-create.html)
Create a decal via a Decal Renderer Feature in URP
