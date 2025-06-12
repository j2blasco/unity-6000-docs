* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/texture-type-sprite.html

  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-and-shaders.html)
  * [Textures](https://docs.unity3d.com/6000.0/Documentation/Manual/Textures-landing.html)
  * [Textures reference](https://docs.unity3d.com/6000.0/Documentation/Manual/textures-reference.html)
  * Sprite (2D and UI) texture Import Settings window reference


[](https://docs.unity3d.com/6000.0/Documentation/Manual/texture-type-editor-gui-and-legacy-gui.html)
Editor GUI and Legacy GUI texture Import Settings window reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/texture-type-cubemap.html)
Cubemap texture Import Settings window reference
# Sprite (2D and UI) texture Import Settings window reference
Set the import settings for the texture asset when you set its **Texture Type** to **Sprite (2D and UI)**.
The **Sprite (2D and UI)** texture type formats the texture asset so that it can be used in 2D features as a [Sprite](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/sprite-landing.html)A 2D graphic objects. If you are used to working in 3D, Sprites are essentially just standard textures but there are special techniques for combining and managing sprite textures for efficiency and convenience during development. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/sprite-landing.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Sprite). Unity automatically locks [Texture Shape](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextureImporter.html#textureshape) to **2D** for this texture type.
Property | Description  
---|---  
**Sprite Mode** | Specifies how to extract the sprite graphic from the image. 
  * **Single** : Use the sprite image as is. You can clip and edit the image in the [Sprite Editor](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/sprite-editor/sprite-editor-landing.html) to refine it further, but Unity treats the sprite generated from the texture source file as a single asset. 
  * **Multiple** : Choose this value if the texture source file has several elements in the same image. You can then define the location of the elements in the Sprite Editor so that Unity knows how to split the image into different sub-assets. For example, you can create animation frames from a single sheet with multiple poses, create [Tiles](https://docs.unity3d.com/6000.0/Documentation/Manual/tilemaps/tiles-for-tilemaps/tile-asset-reference.html)A simple class that allows a sprite to be rendered on a Tilemap. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/tilemaps/tiles-for-tilemaps/scriptable-tiles/scriptable-tiles-landing.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Tile) from a single Tilesheet, or create the different parts of a character.
  * **Polygon** : Choose this value to clip the sprite texture according to the mesh defined in the Sprite Editor’s [Sprite Custom Outline](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/sprite-editor/custom-outline-editor/custom-outline-editor-landing.html).

  
****Pixels** The smallest unit in a computer image. Pixel size depends on your screen resolution. Pixel lighting is calculated at every screen pixel. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/ShadowPerformance.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#pixel) Per Unit** | The number of pixels of width/height in the Sprite image that correspond to one distance unit in world space.  
**Mesh Type** | Specifies the mesh type for the sprite asset you want Unity to generate. This property is visible only when **Sprite Mode** is set to **Single** or **Multiple**. 
  * **Full Rect** : Choose this value to create a quad (four-sided polygon) to map the sprite onto.
  * **Tight** : Choose this value to generate a mesh based on the pixel alpha value. The mesh that Unity generates follows the shape of the sprite. **Note** : Any sprite that’s smaller than 32 × 32 pixels automatically uses **Full Rect** , even when you select **Tight**.

  
****Extrude Edges** A Texture property that enables you to define how much area to leave around a sprite in a generated mesh.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#ExtrudeEdges)** | Controls how much area to leave around the sprite in the generated **mesh** The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/mesh.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Mesh).  
**Pivot** | The location in the image where the sprite’s local coordinate system originates. Choose one of the pre-set options, or select **Custom** to set your own **Pivot** location by setting the **X** and **Y** values. This property is visible only when you set **Sprite Mode** to **Single**.  
**Generate Physics Shape** | Indicates whether to generate a default Physics Shape from the outline of the sprite if you don’t define a Custom Physics Shape. This property is only visible when you set **Sprite Mode** to **Single** or **Multiple**.  
**Open Sprite Editor** | Open the [Sprite Editor](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/sprite-editor/sprite-editor-landing.html) which you can use to define how you want Unity to separate the elements on an image with multiple Sprite Mode elements (to create sub-Assets) or refine the shape, size, and pivot position of a Polygon shape. This button only appears if your project uses the [2D Sprite](https://docs.unity3d.com/Packages/com.unity.2d.sprite@latest) package. For information about how to find and install packages in the Unity Package Manager, refer to [Finding packages](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui-find.html) and [Installing from the registry](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui-install.html).  
**Install 2D Sprite Package** | Installs the 2D Sprite package. This button only appears if your project doesn’t have the 2D Sprite package installed.  
**sRGB (Color Texture)** | Indicates whether the texture is in gamma space. Enable this property for non-HDR color textures such as albedo and **specular color** The color of a specular highlight.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#specularcolor). Disable this property if the texture stores information that you need the exact value for.  
**Alpha Source** | Specifies how Unity generates the alpha value for the texture asset from the texture source file. 
  * **None** : The texture asset doesn’t have an alpha channel, whether the texture source file has one or not. 
  * **Input Texture Alpha** : Unity applies the alpha channel from the texture source file to the texture asset, if the texture source file has an alpha channel.
  * **From Gray Scale** : Unity generates the alpha channel for the texture asset from the average values the texture source files RGB channels.

  
**Alpha is Transparency** | Indicates whether to dilate the color channels. This helps to avoid filtering artifacts on the edges of the alpha channel if the alpha channel represents transparency.  
**Remove PSD Matte** | Indicates whether to apply special processing for Photoshop files that use transparency (blending color pixels with white). **Note** : This is only available for PSD files.  
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
## Additional resources
  * [2D game development QuickStart guide](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-game-development-landing.html)
  * [Sprite Editor](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/sprite-editor/sprite-editor-landing.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/texture-type-editor-gui-and-legacy-gui.html)
Editor GUI and Legacy GUI texture Import Settings window reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/texture-type-cubemap.html)
Cubemap texture Import Settings window reference
