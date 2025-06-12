* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/urp/renderer-feature-decal-reference.html

  * [Visual effects](https://docs.unity3d.com/6000.0/Documentation/Manual/visual-effects.html)
  * [Decals and projectors](https://docs.unity3d.com/6000.0/Documentation/Manual/visual-effects-decals.html)
  * [Decals in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/renderer-feature-decal-landing.html)
  * Decal Renderer Feature reference


[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/decal-shader.html)
Create a decal via a Decal Projector in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/renderer-feature-decal-projector-reference.html)
Decal Projector component reference for URP
# Decal Renderer Feature reference
This section describes the properties of the Decal Renderer Feature.
![Decal Renderer Feature, Inspector view.](https://docs.unity3d.com/6000.0/Documentation/uploads/urp/decal/decal-rf-inspector.png)  
_Decal Renderer Feature, Inspector view._
### Technique
Select the rendering technique for the Renderer Feature.
This section describes the options in this property.
#### Automatic
Unity selects the rendering technique automatically based on the build platform. The [Accurate G-buffer normals](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/rendering/accurate-g-buffer-normals.html) option is also taken into account, as it prevents normal blending from working correctly without the D-Buffer technique.
#### DBuffer
Unity renders decals into the Decal buffer (DBuffer). Unity overlays the content of the DBuffer on top of the opaque objects during the opaque rendering.
Selecting this technique reveals the **Surface Data** property. The Surface Data property lets you specify which surface properties of decals Unity blends with the underlying meshes. The Surface Data property has the following options:
  * **Albedo** : decals affect the base color and the emission color.
  * **Albedo Normal** : decals affect the base color, the emission color, and the normals.
  * **Albedo Normal MAOS** : decals affect the base color, the emission color, the normals, the metallic values, the smoothness values, and the **ambient occlusion** A method to approximate how much ambient light (light not coming from a specific direction) can hit a point on a surface.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Ambientocclusion) values.


**Limitations:**
  * This technique does not support the OpenGL and OpenGL ES API.
  * This technique requires the DepthNormal prepass, which makes the technique less efficient on GPUs that implement tile-based rendering.
  * This technique does not work on particles and **terrain** The landscape in your scene. A Terrain GameObject adds a large flat plane to your scene and you can use the Terrain’s Inspector window to create a detailed landscape. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-UsingTerrains.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Terrain) details.


####  Screen Space
Unity renders decals after the opaque objects using normals that Unity reconstructs from the depth texture, or from the G-Buffer when using the Deferred **rendering path** The technique that a render pipeline uses to render graphics. Choosing a different rendering path affects how lighting and shading are calculated. Some rendering paths are more suited to different platforms and hardware than others. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/RenderingPaths.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#RenderingPath). Unity renders decals as meshes on top of the opaque meshes. This technique supports only the normal blending. When using the Deferred rendering path with [Accurate G-buffer normals](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/rendering/accurate-g-buffer-normals.html), blending of normals is not supported, and will yield incorrect results.
Screen space decals are recommended for mobile platforms that use tile-based rendering, because URP doesn’t create a DepthNormal prepass unless you enable **Use Rendering Layers**. 
Selecting this technique reveals the following properties.
**Property** | **Description**  
---|---  
**Normal Blend** | The options in this property (Low, Medium, and High) determine the number of samples of the depth texture that Unity takes when reconstructing the normal vector from the depth texture. The higher the quality, the more accurate the reconstructed normals are, and the higher the performance impact is.  
**Low** | Unity takes one depth sample when reconstructing normals.  
**Medium** | Unity takes three depth samples when reconstructing normals.  
**High** | Unity takes five depth samples when reconstructing normals.  
### Max Draw Distance
The maximum distance from the **Camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera) at which Unity renders decals.
### Use Rendering Layers
Select this check box to enable the [Rendering Layers](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/features/rendering-layers.html) functionality.
If you enable **Use Rendering Layers** , URP creates a DepthNormal prepass. This makes decals less efficient on GPUs that implement tile-based rendering.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/decal-shader.html)
Create a decal via a Decal Projector in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/renderer-feature-decal-projector-reference.html)
Decal Projector component reference for URP
