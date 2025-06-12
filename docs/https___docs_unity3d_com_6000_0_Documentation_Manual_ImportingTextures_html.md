* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/ImportingTextures.html

  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-and-shaders.html)
  * [Textures](https://docs.unity3d.com/6000.0/Documentation/Manual/Textures-landing.html)
  * Import a texture


[](https://docs.unity3d.com/6000.0/Documentation/Manual/texture-mipmaps-introduction.html)
Mipmaps
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Texture2DArray.html)
2D texture arrays
# Import a texture
A [texture](https://docs.unity3d.com/6000.0/Documentation/Manual/Textures.html)An image used when rendering a GameObject, Sprite, or UI element. Textures are often applied to the surface of a mesh to give it visual detail. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextureImporter.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#texture) is a bitmap image. You can create textures in a digital content creation application, such as Photoshop, and import them into Unity.
In a 3D Project, Unity imports image and movie files in the Assets folder as Textures. In a 2D Project, Unity imports image and movie files in the Assets folder as **Sprites** A 2D graphic objects. If you are used to working in 3D, Sprites are essentially just standard textures but there are special techniques for combining and managing sprite textures for efficiency and convenience during development. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/sprite-landing.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Sprite).
As long as the image meets the [specified size requirements](https://docs.unity3d.com/6000.0/Documentation/Manual/ImportingTextures.html#TextureSizes), Unity imports and optimizes it for game use. This extends to [multi-layer Photoshop PSD or TIFF files](https://docs.unity3d.com/6000.0/Documentation/Manual/ImportingTextures.html#formats).
To import image and movie files as Textures and Sprites in Unity:
  1. Select the image file in the **Project window** A window that shows the contents of your `Assets` folder (Project tab) [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/ProjectView.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Projectwindow).
  2. In the **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector), set the [Texture Import Settings](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextureImporter.html).
  3. Click the **Apply** button to save the changes.
  4. To use the imported Assets in your Project: 
     * For 3D Projects, [create a Material](https://docs.unity3d.com/6000.0/Documentation/Manual/Materials.html) and assign the Texture to the new Material.
     * For 2D Projects, use the [Sprite Editor](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/sprite-editor/sprite-editor-landing.html).


### Supported file formats
Unity can read the following file formats:
  * BMP
  * EXR
  * GIF
  * HDR
  * IFF
  * JPG
  * PICT
  * PNG
  * PSD
  * TGA
  * TIFF


Unity automatically flattens multi-layer Photoshop PSD or TIFF files on import so that there is no size penalty for your game. This flattening happens to the imported data in Unity, not to the file itself, so you can continue to save and import your PSD or TIFF files without losing any of your work when using these file types natively. This allows you to have one copy of each Texture which you can use in Photoshop, your 3D modelling application, and in Unity. 
When importing from an EXR or **HDR** high dynamic range  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#HDR) file containing HDR information, the [Texture Importer](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextureImporter.html) automatically chooses the right HDR format for the output Texture. This format changes automatically depending on which platform you are building for.
## Texture dimensions
Ideally, Texture dimension sizes should be powers of two on each side (that is, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048 pixels (px), and so on). The Textures do not have to be square; the width can be different from height.
It is possible to use NPOT (non-power of two) Texture sizes with Unity. However, NPOT Texture sizes generally take slightly more memory and might be slower for the GPU to sample, so it’s better for performance to use power of two sizes whenever you can.
If the platform or GPU does not support NPOT Texture sizes, Unity scales and pads the Texture up to the next power of two size. This process uses more memory and makes loading slower (especially on older mobile devices). In general, you should only use NPOT sizes for GUI purposes.
You can scale up NPOT Texture Assets at import time using the **Non Power of 2** option in the **Advanced** section of the Texture Importer.
**Note:** Specific platforms may impose maximum Texture dimension sizes. For DirectX, the maximum Texture sizes for different feature levels are as follows:
Graphics APIs / Feature levels | Maximum 2D and **Cubemap** A collection of six square textures that can represent the reflections in an environment or the skybox drawn behind your geometry. The six squares form the faces of an imaginary cube that surrounds an object; each face represents the view along the directions of the world axes (up, down, left, right, forward and back). [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Cubemap-landing.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Cubemap) texture dimension size (px)  
---|---  
DX9 **Shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) Model 2 (PC GPUs before 2004) | 2048  
DX9 Shader Model 3 (PC GPUs before 2006) / Windows Phone DX11 9.3 level / OpenGL ES 3.0 | 4096  
DX10 Shader Model 4 / GL3 (PC GPUs before 2007) / OpenGL ES 3.1 | 8192  
DX11 Shader Model 5 / GL4 (PC GPUs since 2008) | 16384  
**Notes:**
  * The Texture Importer only allows you to choose dimension sizes up to 16384 (16384 × 16384 pixels).
  * Most [Mali GPUs](https://en.wikipedia.org/wiki/Mali_\(GPU\)) support Texture dimension sizes up to 4K for cubemaps.


## Platform-specific overrides
When building for different platforms, you need to think about the resolution, the file size with associated memory size requirements, the quality of your Textures, and what **compression** A method of storing data that reduces the amount of storage space it requires. See [Texture Compression](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextureImporterOverride), [Animation Compression](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AnimationClip.html#AssetProperties), [Audio Compression](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioClip.html), [Build Compression](https://docs.unity3d.com/6000.0/Documentation/Manual/ReducingFilesize.html).  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#compression) format to use for each target platform. The **Platform-specific overrides** panel provides one tab for the **Default** options, and one tab for every target platform you are building for. Some texture import settings can also be overridden globally in [Build Profiles](https://docs.unity3d.com/6000.0/Documentation/Manual/BuildSettings.html)A set of customizable configuration settings to use when creating a build for your target platform. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/build-profiles.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Buildprofile), mostly to speed up iteration time during development.
To set up override values:
  1. Set the default properties on the **Default** tab.
  2. Navigate to a specific target platform tab and enable the **Override for <target-platform>** option.
  3. Set the override properties.


## Additional resources
  * [Textures reference](https://docs.unity3d.com/6000.0/Documentation/Manual/textures-reference.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/texture-mipmaps-introduction.html)
Mipmaps
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Texture2DArray.html)
2D texture arrays
