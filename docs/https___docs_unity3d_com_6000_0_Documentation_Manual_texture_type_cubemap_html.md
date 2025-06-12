* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/texture-type-cubemap.html

  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-and-shaders.html)
  * [Textures](https://docs.unity3d.com/6000.0/Documentation/Manual/Textures-landing.html)
  * [Textures reference](https://docs.unity3d.com/6000.0/Documentation/Manual/textures-reference.html)
  * Cubemap texture Import Settings window reference


[](https://docs.unity3d.com/6000.0/Documentation/Manual/texture-type-sprite.html)
Sprite (2D and UI) texture Import Settings window reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Texture3D-reference.html)
3D texture preview reference
# Cubemap texture Import Settings window reference
You can further refine **Cubemap** A collection of six square textures that can represent the reflections in an environment or the skybox drawn behind your geometry. The six squares form the faces of an imaginary cube that surrounds an object; each face represents the view along the directions of the world axes (up, down, left, right, forward and back). [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Cubemap-landing.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Cubemap) shape textures with the following properties:
Here’s your fixed Markdown table with properly aligned rows: 
**Property** | **Sub-property** | **Description**  
---|---|---  
**Mapping** | - | Use **Mapping** to specify how the Texture is projected onto your **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject). This is set to **Auto** by default.  
**Mapping** | **Auto** | Unity tries to create the layout from the Texture information.  
**Mapping** | **6 Frames Layout (Cubic Environment)** | The Texture contains six images arranged in one of the standard cubemap layouts: cross, or sequence (+x -x +y -y +z -z). The images can be orientated either horizontally or vertically.  
**Mapping** | **Latitude Longitude (Cylindrical)** | Maps the Texture to a 2D Latitude-Longitude representation.  
**Mapping** | **Mirrored Ball (Sphere Mapped)** | Maps the Texture to a sphere-like cubemap.  
**Convolution Type** | - | Choose the type of pre-convolution (filtering) that you want to use for this Texture. The result of pre-convolution is stored in mipmaps.   
This property is only available for the [Default](https://docs.unity3d.com/6000.0/Documentation/Manual/texture-type-default.html) Texture type.  
**Convolution Type** | **None** | The Texture has no pre-convolution (no filtering). This is the default.  
**Convolution Type** | **Specular (Glossy Reflection)** | Select this to use cubemaps as **Reflection Probes** A rendering component that captures a spherical view of its surroundings in all directions, rather like a camera. The captured image is then stored as a Cubemap that can be used by objects with reflective materials. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ReflectionProbe.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#ReflectionProbe). The Texture mipmaps are pre-convoluted (filtered) with the engine BRDF. For more information, see Wikipedia’s page on [Bidirectional reflectance distribution function](https://en.wikipedia.org/wiki/Bidirectional_reflectance_distribution_function).  
**Convolution Type** | **Diffuse (Irradiance)** | The Texture is convoluted (filtered) to represent irradiance. This is useful if you use the cubemap as a **Light Probe** Light probes store information about how light passes through space in your scene. A collection of light probes arranged within a given space can improve lighting on moving objects and static LOD scenery within that space. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/LightProbes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#LightProbe).  
**Fixup Edge Seams** | - | This option is only available with the **None** or **Diffuse** convolution (filter). Use this on low-end platforms as a work-around for filtering limitations, such as cubemaps incorrectly filtered between faces.  
## Additional resources
  * [Cubemaps](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Cubemap-landing.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/texture-type-sprite.html)
Sprite (2D and UI) texture Import Settings window reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Texture3D-reference.html)
3D texture preview reference
