* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/texture-type-cursor.html

  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-and-shaders.html)
  * [Textures](https://docs.unity3d.com/6000.0/Documentation/Manual/Textures-landing.html)
  * [Textures reference](https://docs.unity3d.com/6000.0/Documentation/Manual/textures-reference.html)
  * Cursor texture Import Settings window reference


[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Texture3D-reference.html)
3D texture preview reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/texture-type-cookie.html)
Cookie texture Import Settings window reference
# Cursor texture Import Settings window reference
The **Cursor** texture type formats the texture asset so that it can be used as a custom mouse cursor. Unity locks **Texture Shape** to **2D** for this texture type. For more information, refer to [Texture Shape](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextureImporter.html#textureshape).
Property | Description  
---|---  
**Alpha Source** | Specifies how Unity generates the alpha value for the texture asset from the texture source file. 
  * **None** : The texture asset doesn’t have an alpha channel, whether the texture source file has one or not. 
  * **Input Texture Alpha** : Unity applies the alpha channel from the texture source file to the texture asset, if the texture source file has an alpha channel.
  * **From Gray Scale** : Unity generates the alpha channel for the texture asset from the average values the texture source files RGB channels.

  
**Alpha is Transparency** | Indicates whether to dilate the color channels. This helps to avoid filtering artifacts on the edges of the alpha channel if the alpha channel represents transparency.  
**Remove PSD Matte** | Indicates whether to apply special processing for Photoshop files that use transparency (blending color pixels with white). **Note** : This is only available for PSD files.  
**Non Power of 2** | Specifies how Unity scales the dimension size if the texture source file has a non-power of two (NPOT) dimension size. For more information on NPOT dimension sizes, see [Importing Textures](https://docs.unity3d.com/6000.0/Documentation/Manual/ImportingTextures.html). 
  * **None** : Texture dimension size stays the same.
  * **To nearest** : Scales the texture to the nearest power-of-two dimension size at import time. For example, a 257 × 511 pixels texture is scaled to 256 × 512 pixels. Note that PVRTC formats require textures to be square (that is width equal to height), so the final dimension size is upscaled to 512 × 512 pixels.
  * **To larger** : Scales the texture to the power-of-two dimension size of the largest dimension size value at import time. For example, a 257 × 511 pixels texture is scaled to 512 × 512 pixels.
  * **To smaller** : Scales the texture to the power-of-two dimension size of the smallest dimension size value at import time. For example, a 257 × 511 pixels texture is scaled to 256 × 256 pixels. 

  
**Read/Write** | Indicates whether to access the texture data from **scripts** A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/creating-scripts.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scripts) using [Texture2D.SetPixels](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.SetPixels.html), [Texture2D.GetPixels](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.GetPixels.html) and other [Texture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html)An image used when rendering a GameObject, Sprite, or UI element. Textures are often applied to the surface of a mesh to give it visual detail. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextureImporter.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#texture) methods. Internally, Unity uses a copy of the Texture data for script access, which doubles the amount of memory required for the Texture. This property is therefore disabled by default, and you should enable it only if you require script access. For more information, see [Texture.isReadable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture-isReadable.html).  
**Generate Mipmap** | Indicates whether to generate a [mipmap](https://docs.unity3d.com/6000.0/Documentation/Manual/texture-mipmaps-introduction.html) for this texture.  
**Mipmap Limit** | Disable this option to use all mipmap levels, regardless of the Mipmap Limit settings in the **Quality** menu. This property only appears if you set **Texture Shape** to **2D** or **2D Array**. Other texture shapes always use all mipmap levels.  
**Mipmap Limit Group** | Select the Mipmap Limit group this texture should be part of. The default option is **None (Use Global Mipmap Limit)**. This property only appears if you set **Texture Shape** to **2D** or **2D Array**. Other texture shapes always use all mipmap levels.  
**Mipmap Filtering** | Specifies the method Unity uses to filter mipmap levels and optimize image quality. This property is visible only when **Generate Mipmap** is enabled. 
  * **Box** : Makes mipmap levels smoother as they decrease in dimension size.
  * **Kaiser** : Runs a sharpening algorithm on mipmap levels as they decrease in dimension size. Use this option if your textures are too blurry when far away. The algorithm is of the Kaiser Window type. For more information, see [Wikipedia](https://en.wikipedia.org/wiki/Kaiser_window).

  
**Preserve Coverage** | Indicates whether the alpha channel in generated mipmaps preserves coverage during the alpha text. For more information, see [TextureImporterSettings.mipMapsPreserveCoverage](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterSettings-mipMapsPreserveCoverage.html). This property is visible only when **Generate Mipmap** is enabled.  
**Alpha Cutoff** | The reference value that controls the mipmap coverage during the alpha test. This property is visible only when **Preserve Coverage** is enabled.  
**Replicate Border** | Indicates whether to stop colors bleeding out to the edge of the lower mipmap levels. This is useful for light cookies.  
  
This property is visible only when **Generate Mipmap** is enabled.  
**Fadeout to Gray** | Indicates whether mipmap levels should fade to gray as the mipmap levels progress. This is useful for detail maps. The left-most scroll is the first mipmap level to begin fading out. The right-most scroll defines the mipmap level where the texture is completely grayed out. This property is visible only when **Generate Mipmap** is enabled.  
**Ignore PNG Gamma** | Indicates whether to ignore the gamma attribute in PNG files.  
  
This option is only visible if the texture source file is a PNG.  
**Swizzle** | Specifies how to order the texture source file color channel data.  
**Wrap Mode** | Specifies how the texture behaves when it tiles. 
  * **Repeat** : Repeats the texture in tiles.
  * **Clamp** : Stretches the texture’s edges.
  * **Mirror** : Mirrors the texture at every integer boundary to create a repeating pattern.
  * **Mirror Once** : Mirrors the texture once, then clamps it to edge pixels. **Note** : Some mobile devices don’t support Mirror Once. In this case, Unity uses Mirror instead.
  * **Per-axis** : Provides options you can use to individually control how Unity wraps textures on the u-axis and v-axis.

  
**Filter Mode** | Specifies how Unity filters the texture when the texture stretches during 3D transformations. 
  * **Point (no filter)** : The texture appears blocky up close.
  * **Bilinear** : The texture appears blurry up close.
  * **Trilinear** : Like **Bilinear** , but the texture also blurs between the different mipmap levels.

  
****Aniso Level** The anisotropic filtering (AF) level of a texture. Allows you to increase texture quality when viewing a texture at a steep angle. Good for floor and ground textures. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextureImporter.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#AnisoLevel)** | Controls the texture quality when you view the texture at a steep angle. Anisotropic filtering is good for floor and ground Textures but is resource intensive. For more information, see [Importing textures](https://docs.unity3d.com/6000.0/Documentation/Manual/ImportingTextures.html).  
In addition, you can use the [Platform-specific overrides](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextureImporter.html#platform) panel to set default options and overrides for specific platforms. 
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Texture3D-reference.html)
3D texture preview reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/texture-type-cookie.html)
Cookie texture Import Settings window reference
