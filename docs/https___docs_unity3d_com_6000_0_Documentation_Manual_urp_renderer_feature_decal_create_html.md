* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/urp/renderer-feature-decal-create.html

  * [Visual effects](https://docs.unity3d.com/6000.0/Documentation/Manual/visual-effects.html)
  * [Decals and projectors](https://docs.unity3d.com/6000.0/Documentation/Manual/visual-effects-decals.html)
  * [Decals in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/renderer-feature-decal-landing.html)
  * Create a decal via a Decal Renderer Feature in URP


[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/renderer-feature-decal.html)
Introduction to decals in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/decal-shader.html)
Create a decal via a Decal Projector in URP
# Create a decal via a Decal Renderer Feature in URP
To add decals to your **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene):
  1. [Add the Decal Renderer Feature](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/urp-renderer-feature.html) to the URP Renderer.
  2. Create a Material, and assign it the `Shader Graphs/Decal` **shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader). In the Material, select the Base Map and the **Normal Map** A type of Bump Map texture that allows you to add surface detail such as bumps, grooves, and scratches to a model which catch the light as if they are represented by real geometry.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Normalmap).
![Example decal Material](https://docs.unity3d.com/6000.0/Documentation/uploads/urp/decal/decal-example-material.png) Example decal Material
  3. Create a new Decal Projector **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject), or add a [Decal Projector component](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/renderer-feature-decal.html#decal-projector) to an existing GameObject.


The following illustration shows a Decal Projector in the scene.
![Decal Projector in the scene.](https://docs.unity3d.com/6000.0/Documentation/uploads/urp/decal/decal-projector-selected-with-inspector.png) Decal Projector in the scene.
For more information, refer to the [Decal Projector component](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/renderer-feature-decal.html#decal-projector).
An alternative way to add decals to a scene:
  1. Create a **Quad** A primitive object that resembles a plane but its edges are only one unit long, it uses only 4 vertices, and the surface is oriented in the XY plane of the local coordinate space. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/PrimitiveObjects.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Quad) GameObject.
  2. Assign a Decal Material to the GameObject.
  3. Position the Quad on the surface where you want the decal to be. If necessary, adjust the [mesh bias](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/decal-shader-graph-reference.html) value to prevent z-fighting.


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/renderer-feature-decal.html)
Introduction to decals in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/decal-shader.html)
Create a decal via a Decal Projector in URP
