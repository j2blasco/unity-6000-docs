* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/linear-color-space.html

  * [Rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/rendering-and-post-processing.html)
  * [Color](https://docs.unity3d.com/6000.0/Documentation/Manual/graphics-color.html)
  * [Color spaces](https://docs.unity3d.com/6000.0/Documentation/Manual/color-spaces-landing.html)
  * [Linear color space](https://docs.unity3d.com/6000.0/Documentation/Manual/linear-color-space-landing.html)
  * Introduction to linear color space in Unity


[](https://docs.unity3d.com/6000.0/Documentation/Manual/linear-color-space-landing.html)
Linear color space
[](https://docs.unity3d.com/6000.0/Documentation/Manual/gamma-textures-linear-color-space.html)
Gamma Textures in linear color space
# Introduction to linear color space in Unity
Working in linear color space gives more accurate rendering than working in gamma color space.
You can work in linear color space if your Textures were created in linear or gamma color space. Gamma color space Texture inputs to the linear color space **Shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) program are supplied to the Shader with gamma correction removed from them.
For information on how to set the color space of your project, refer to [Set a project’s color space](https://docs.unity3d.com/6000.0/Documentation/Manual/set-project-color-space.html).
**Note** : The **Texture preview** window in [Texture Import Settings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporter.html) displays Textures using gamma blending even if you are working in linear color space.
## Linear Textures
Selecting **Color Space: Linear** assumes your Textures are in gamma color space. Unity uses your GPU’s sRGB sampler by default to crossover from gamma to linear color space. If your Textures are authored in linear color space, you need to bypass the sRGB sampling. For more information, refer to [Disable sRGB sampling for a texture](https://docs.unity3d.com/6000.0/Documentation/Manual/disable-srgb-sampling-textures.html).
## Gamma Textures
Crossing over from gamma color space to linear color space requires some tweaking. For more information, refer to [Gamma Textures in linear color space](https://docs.unity3d.com/6000.0/Documentation/Manual/gamma-textures-linear-color-space.html).
### Gamma to linear conversion
For colors, this conversion is applied implicitly, because the Unity Editor already converts the values to floating point before passing them to the GPU as constants. When sampling Textures, the GPU automatically removes the gamma correction, converting the result to linear space.
These inputs are then passed to the Shader, with lighting calculations taking place in linear space as they normally do. When writing the resulting value to a framebuffer, it is either gamma-corrected straight away or left in linear space for later gamma correction - this depends on the current rendering configuration. For example, in high dynamic range (HDR), rendering results are left in linear space and gamma corrected later.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/linear-color-space-landing.html)
Linear color space
[](https://docs.unity3d.com/6000.0/Documentation/Manual/gamma-textures-linear-color-space.html)
Gamma Textures in linear color space
