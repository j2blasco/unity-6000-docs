* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/gamma-color-space.html

  * [Rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/rendering-and-post-processing.html)
  * [Color](https://docs.unity3d.com/6000.0/Documentation/Manual/graphics-color.html)
  * [Color spaces](https://docs.unity3d.com/6000.0/Documentation/Manual/color-spaces-landing.html)
  * Gamma color space


[](https://docs.unity3d.com/6000.0/Documentation/Manual/differences-linear-gamma-color-space.html)
Differences between linear and gamma color space
[](https://docs.unity3d.com/6000.0/Documentation/Manual/linear-color-space-landing.html)
Linear color space
# Gamma color space
While a linear workflow ensures more precise rendering, sometimes you may want a gamma workflow (for example, on some platforms the hardware only supports the gamma format).
For information on how to set the color space of your project, refer to [Set a project’s color space](https://docs.unity3d.com/6000.0/Documentation/Manual/set-project-color-space.html).
Unity uses the gamma color space for color calculations, and keeps imported textures in the gamma color space. Unity also makes sure **shaders** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) keep textures in gamma color space, calculate in gamma color space, and write to a framebuffer that doesn’t reapply gamma correction.
[Texture Import Settings](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextureImporter.html) might show textures as being in linear format, because this avoids shaders recognising the textures as being in gamma color space and automatically removing the gamma correction.
**Note** : You can choose to bypass sRGB sampling in **Color Space: Gamma** mode. For more information on how to do this, refer to [Disable sRGB sampling for a texture](https://docs.unity3d.com/6000.0/Documentation/Manual/disable-srgb-sampling-textures.html).
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/differences-linear-gamma-color-space.html)
Differences between linear and gamma color space
[](https://docs.unity3d.com/6000.0/Documentation/Manual/linear-color-space-landing.html)
Linear color space
