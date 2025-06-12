* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/set-project-color-space.html

  * [Rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/rendering-and-post-processing.html)
  * [Color](https://docs.unity3d.com/6000.0/Documentation/Manual/graphics-color.html)
  * [Color spaces](https://docs.unity3d.com/6000.0/Documentation/Manual/color-spaces-landing.html)
  * Set a project's color space


[](https://docs.unity3d.com/6000.0/Documentation/Manual/linear-textures.html)
Linear textures
[](https://docs.unity3d.com/6000.0/Documentation/Manual/disable-srgb-sampling-textures.html)
Disable sRGB sampling for a texture
# Set a project’s color space
The Unity Editor offers both linear and gamma workflows. The linear workflow has a color space crossover where [Textures](https://docs.unity3d.com/6000.0/Documentation/Manual/Textures.html)An image used when rendering a GameObject, Sprite, or UI element. Textures are often applied to the surface of a mesh to give it visual detail. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextureImporter.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#texture) that were authored in gamma color space can be correctly and precisely rendered in linear color space. See documentation on [Linear rendering overview](https://docs.unity3d.com/6000.0/Documentation/Manual/color-spaces-landing.html) for more information about gamma and linear color space.
Textures tend to be saved in gamma color space, while Shaders expect linear color space. As such, when Textures are sampled in Shaders, the gamma-based values lead to inaccurate results. To overcome this, you can set Unity to use an sRGB sampler to cross over from gamma to linear sampling. This ensures a linear workflow with all inputs and outputs of a **Shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) in the correct color space, resulting in a correct outcome.
## Select the color space
Select the color space for your project with the following steps:
  1. Go to **Edit** > **Project Settings** , then select the **Player** category.
  2. Navigate to the **Other Settings** , open the **Rendering** section, and set the **Color Space** property to **Linear** or **Gamma** , depending on your preference.


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/linear-textures.html)
Linear textures
[](https://docs.unity3d.com/6000.0/Documentation/Manual/disable-srgb-sampling-textures.html)
Disable sRGB sampling for a texture
