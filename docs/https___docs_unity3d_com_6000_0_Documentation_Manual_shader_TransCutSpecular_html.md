* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/shader-TransCutSpecular.html

  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-and-shaders.html)
  * [Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)
  * [Prebuilt shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-built-in-landing.html)
  * [Legacy prebuilt shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/Built-inShaderGuide.html)
  * [Transparent Cutout Shader Family](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-TransparentCutoutFamily.html)
  * Transparent Cutout Specular


[](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-TransCutDiffuse.html)
Transparent Cutout Diffuse
[](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-TransCutBumpedDiffuse.html)
Transparent Cutout Bumped Diffuse
# Transparent Cutout Specular
**Note.** Unity 5 introduced the [Standard Shader](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-StandardShader.html) which replaces this **shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader).
![Transparent Cutout Specular shader.](https://docs.unity3d.com/6000.0/Documentation/uploads/Shaders/Shader-TransCutoutSpec.jpg) Transparent Cutout Specular shader.
One consideration for this shader is that the Base texture’s alpha channel defines both the Transparent areas as well as the Specular Map.
## Transparent Cutout Properties
**Note.** Unity 5 introduced the [Standard Shader](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-StandardShader.html) which replaces this shader.
Cutout shader is an alternative way of displaying transparent objects. Differences between Cutout and regular [Transparent](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-TransparentFamily.html) shaders are:
  * This shader cannot have partially transparent areas. Everything will be either fully opaque or fully transparent.
  * Objects using this shader can cast and receive shadows!
  * The graphical sorting problems normally associated with Transparent shaders do not occur when using this shader.


This shader uses an alpha channel contained in the **Base** Texture to determine the transparent areas. If the alpha contains a blend between transparent and opaque areas, you can manually determine the cutoff point for the which areas will be shown. You change this cutoff by adjusting the **Alpha Cutoff** slider.
## Specular Properties
Specular computes the same simple (Lambertian) lighting as Diffuse, plus a viewer dependent specular highlight. This is called the Blinn-Phong lighting model. It has a specular highlight that is dependent on surface angle, light angle, and viewing angle. The highlight is actually just a realtime-suitable way to simulate blurred reflection of the light source. The level of blur for the highlight is controlled with the **Shininess** slider in the **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector).
Additionally, the alpha channel of the main texture acts as a Specular Map (sometimes called “gloss map”), defining which areas of the object are more reflective than others. Black areas of the alpha will be zero specular reflection, while white areas will be full specular reflection. This is very useful when you want different areas of your object to reflect different levels of specularity. For example, something like rusty metal would use low specularity, while polished metal would use high specularity. Lipstick has higher specularity than skin, and skin has higher specularity than cotton clothes. A well-made Specular Map can make a huge difference in impressing the player.
## Performance
Generally, this shader is moderately expensive to render. For more details, please view the [Shader Peformance page](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-Performance.html).
TransCutSpecular
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-TransCutDiffuse.html)
Transparent Cutout Diffuse
[](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-TransCutBumpedDiffuse.html)
Transparent Cutout Bumped Diffuse
