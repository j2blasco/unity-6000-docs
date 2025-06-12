* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/urp/decal-shader-graph-reference.html

  * [Visual effects](https://docs.unity3d.com/6000.0/Documentation/Manual/visual-effects.html)
  * [Decals and projectors](https://docs.unity3d.com/6000.0/Documentation/Manual/visual-effects-decals.html)
  * [Decals in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/renderer-feature-decal-landing.html)
  * Decal Shader Graph reference for URP


[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/renderer-feature-decal-projector-reference.html)
Decal Projector component reference for URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/decals-birp.html)
Decals in the Built-In Render Pipeline
# Decal Shader Graph reference for URP
You can assign a Material that uses a Decal **Shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) Graph to a **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) directly. For example, you can [use a Quad as the Decal GameObject](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/renderer-feature-decal-create.html#decal-gameobject).
The pre-built Decal Shader has the following properties:
  * **Base Map** : the Base texture of the Material.
  * ****Normal Map** A type of Bump Map texture that allows you to add surface detail such as bumps, grooves, and scratches to a model which catch the light as if they are represented by real geometry.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Normalmap)**: the normal texture of the Material.
  * **Normal Blend** : this property defines the proportion in which the the normal texture selected in the Normal Map property blends with the normal map of the Material that the decal is projected on. 0: the decal does not affect the Material it’s projected on. 1: the normal map of the decal replaces the normal map of the Material it’s projected on.

**Property** | **Description**  
---|---  
**Affect BaseColor** | When enabled, the shader affects the base color. Most decals make use of this option. An exception is a surface damage effect, were you might want to manipulate other properties, such as normals.  
![Decal Color](https://docs.unity3d.com/6000.0/Documentation/uploads/urp/decal/decal-color.png)  
_From left to right: shader affecting only the color, affecting all properties, affecting all properties but color._  
**Affect Normal** | When enabled, the shader affects normals. Use cases: adding damage effects to materials, for example, bullet holes or cracks. Use the **Blend** property to blend the normals of the decal with the normals of the surface it’s projected to. If the **Blend** property is disabled, the decal overrides the normals all over the surface it’s projected to.  
![Decal Normal](https://docs.unity3d.com/6000.0/Documentation/uploads/urp/decal/decal-normal.png)  
_From left to right: Affect Normal is off; Affect Normal is on, Blend is off; Affect Normal and Blend are on._  
**Affect MAOS** | MOAS stands for Metallic, Ambient Occlusion, and Smoothness. These properties are grouped together to save memory. You can change values of each property separately in the shader, but all properties are blended with a single common alpha value.  
Use cases:  
Override smoothness to highlight puddles or wet paint. Override metallic values with lower values to render rust. Override AO to give the decal more depth.  
![Decal MAOS](https://docs.unity3d.com/6000.0/Documentation/uploads/urp/decal/decal-maos.png)  
_Left: the decal does not affect MAOS. Right: the decal affects MAOS._  
**Affect Emission** | Use cases: you can affect the emission values to make surfaces seem like they are emitting light, or to make surfaces seem like they are being lit by light.  
![Decal Emission](https://docs.unity3d.com/6000.0/Documentation/uploads/urp/decal/decal-emission.png)   
_Left: Affect Emission is off. Right: Affect Emission is on._  
The Decal Material properties above are defined in the pre-built Shader Graph. Custom decal Material properties depend on a custom Shader Graph.
The following table describes the properties in the **Advanced Options** section. These properties are common for all decal shaders.
**Property** | **Description**  
---|---  
**Enable GPU Instancing** | Enabling this option lets URP render meshes with the same geometry and Material in one batch, when possible. This makes rendering faster. URP cannot render Meshes in one batch if they have different Materials or if the hardware does not support GPU instancing.  
**Priority** | This property defines the order in which URP draws decals in the scene. URP draws decals with lower Priority values first, and draws decals with higher Priority values on top of those with lower values.   
If there are multiple Decal Materials with the same **Priority** in the scene, URP renders them in the order in which the Materials were created.  
**Mesh Bias Type** | Select the Mesh bias type. The Mesh bias lets you prevent z-fighting between the Decal GameObject and the GameObject it overlaps. This property is only applicable for GameObjects with a [Decal Material type assigned directly](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/renderer-feature-decal-create.html#decal-gameobject).  
_View Bias_ | A world-space bias (in meters). When drawing the Decal GameObject, Unity shifts each **pixel** The smallest unit in a computer image. Pixel size depends on your screen resolution. Pixel lighting is calculated at every screen pixel. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/ShadowPerformance.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#pixel) of the GameObject by this value along the view vector. A positive value shifts pixels closer to the **Camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera), so that Unity draws the Decal GameObject on top of the overlapping **Mesh** The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/mesh.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Mesh), which prevents z-fighting. Decal Projectors ignore this property.  
_Depth Bias_ | When drawing the Decal GameObject, Unity changes the depth value of each pixel of the GameObject by this value. A negative value shifts pixels closer to the Camera, so that Unity draws the Decal GameObject on top of the overlapping Mesh, which prevents z-fighting. Decal Projectors ignore this property.  
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/renderer-feature-decal-projector-reference.html)
Decal Projector component reference for URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/decals-birp.html)
Decals in the Built-In Render Pipeline
