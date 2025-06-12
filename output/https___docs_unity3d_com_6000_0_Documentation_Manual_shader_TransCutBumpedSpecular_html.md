* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/shader-TransCutBumpedSpecular.html

  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-and-shaders.html)
  * [Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)
  * [Prebuilt shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-built-in-landing.html)
  * [Legacy prebuilt shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/Built-inShaderGuide.html)
  * [Transparent Cutout Shader Family](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-TransparentCutoutFamily.html)
  * Transparent Cutout Bumped Specular


[](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-TransCutBumpedDiffuse.html)
Transparent Cutout Bumped Diffuse
[](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-SelfIllumFamily.html)
Self-Illuminated Shader Family
# Transparent Cutout Bumped Specular
**Note.** Unity 5 introduced the [Standard Shader](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-StandardShader.html) which replaces this **shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader).
![Transparent Cutout Bumped Specular shader.](https://docs.unity3d.com/6000.0/Documentation/uploads/Shaders/Shader-TransCutoutBumpSpec.jpg) Transparent Cutout Bumped Specular shader.
One consideration for this shader is that the Base texture’s alpha channel defines both the Transparent areas as well as the Specular Map.
## Transparent Cutout Properties
**Note.** Unity 5 introduced the [Standard Shader](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-StandardShader.html) which replaces this shader.
Cutout shader is an alternative way of displaying transparent objects. Differences between Cutout and regular [Transparent](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-TransparentFamily.html) shaders are:
  * This shader cannot have partially transparent areas. Everything will be either fully opaque or fully transparent.
  * Objects using this shader can cast and receive shadows!
  * The graphical sorting problems normally associated with Transparent shaders do not occur when using this shader.


This shader uses an alpha channel contained in the **Base** Texture to determine the transparent areas. If the alpha contains a blend between transparent and opaque areas, you can manually determine the cutoff point for the which areas will be shown. You change this cutoff by adjusting the **Alpha Cutoff** slider.
## Normal Mapped Properties
Like a **Diffuse** shader, this computes a simple (Lambertian) lighting model. The lighting on the surface decreases as the angle between it and the light decreases. The lighting depends only on the angle, and does not change as the **camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera) moves or rotates around.
**Normal mapping** simulates small surface details using a texture, instead of spending more polygons to actually carve out details. It does not actually change the shape of the object, but uses a special texture called a **Normal Map** A type of Bump Map texture that allows you to add surface detail such as bumps, grooves, and scratches to a model which catch the light as if they are represented by real geometry.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Normalmap) to achieve this effect. In the normal map, each **pixel** The smallest unit in a computer image. Pixel size depends on your screen resolution. Pixel lighting is calculated at every screen pixel. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/ShadowPerformance.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#pixel)’s color value represents the angle of the surface normal. Then by using this value instead of the one from geometry, lighting is computed. The normal map effectively overrides the **mesh** The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/mesh.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Mesh)’s geometry when calculating lighting of the object.
### Creating Normal maps
You can import normal maps created outside of Unity, or you can import a regular grayscale image and convert it to a Normal Map from within Unity. (This page refers to a legacy shader which has been superseded by the [Standard Shader](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-StandardShader.html), but you can learn more about how to use [Normal Maps in the Standard Shader](https://docs.unity3d.com/6000.0/Documentation/Manual/StandardShaderMaterialParameterNormalMap.html))
### Technical Details
The Normal Map is a tangent space type of normal map. Tangent space is the space that “follows the surface” of the model geometry. In this space, Z always points away from the surface. Tangent space Normal Maps are a bit more expensive than the other “object space” type Normal Maps, but have some advantages:
  1. It’s possible to use them on deforming models - the bumps will remain on the deforming surface and will just work.
  2. It’s possible to reuse parts of the normal map on different areas of a model; or use them on different models.


## Specular Properties
Specular computes the same simple (Lambertian) lighting as Diffuse, plus a viewer dependent specular highlight. This is called the Blinn-Phong lighting model. It has a specular highlight that is dependent on surface angle, light angle, and viewing angle. The highlight is actually just a realtime-suitable way to simulate blurred reflection of the light source. The level of blur for the highlight is controlled with the **Shininess** slider in the **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector).
Additionally, the alpha channel of the main texture acts as a Specular Map (sometimes called “gloss map”), defining which areas of the object are more reflective than others. Black areas of the alpha will be zero specular reflection, while white areas will be full specular reflection. This is very useful when you want different areas of your object to reflect different levels of specularity. For example, something like rusty metal would use low specularity, while polished metal would use high specularity. Lipstick has higher specularity than skin, and skin has higher specularity than cotton clothes. A well-made Specular Map can make a huge difference in impressing the player.
## Performance
Generally, this shader is moderately expensive to render. For more details, please view the [Shader Peformance page](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-Performance.html).
TransCutBumpedSpecular
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-TransCutBumpedDiffuse.html)
Transparent Cutout Bumped Diffuse
[](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-SelfIllumFamily.html)
Self-Illuminated Shader Family
