* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/Textures.html

  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-and-shaders.html)
  * [Textures](https://docs.unity3d.com/6000.0/Documentation/Manual/Textures-landing.html)
  * [Get started with textures](https://docs.unity3d.com/6000.0/Documentation/Manual/textures-getting-started.html)
  * Introduction to textures


[](https://docs.unity3d.com/6000.0/Documentation/Manual/textures-getting-started.html)
Get started with textures
[](https://docs.unity3d.com/6000.0/Documentation/Manual/texture-types.html)
Texture types
# Introduction to textures
Normally, the **mesh** The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/mesh.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Mesh) geometry of an object only gives a rough approximation of the shape while most of the fine detail is supplied by **Textures** An image used when rendering a GameObject, Sprite, or UI element. Textures are often applied to the surface of a mesh to give it visual detail. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextureImporter.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#texture). A texture is just a standard bitmap image that is applied over the mesh surface. You can think of a texture image as though it were printed on a rubber sheet that is stretched and pinned onto the mesh at appropriate positions. The positioning of the texture is done with the 3D modelling software that is used to create the mesh.
![Cylinder with tree bark](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/CylinderTreeBark.png) Cylinder with tree bark
Unity can import textures from most common image file formats.
## Terminology
This page uses the following terminology:
  * **Bits per**pixel** The smallest unit in a computer image. Pixel size depends on your screen resolution. Pixel lighting is calculated at every screen pixel. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/ShadowPerformance.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#pixel) (bpp)** is the amount of storage required for a single texture pixel. Textures with a lower bpp value have a smaller size on disk and in memory. A lower bpp value also means that the GPU can store more pixels in its cache, which results in faster texture access.
  * LDR (Low Dynamic Range) refers to most typical images where colors are conceptually between 0.0 (black) and 1.0 (white) values. The majority of image files (such as PNG and JPG) have low dynamic range.
  * **HDR** high dynamic range  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#HDR) (High Dynamic Range) refers to special image and **texture formats** A file format for handling textures during real-time rendering by 3D graphics hardware, such as a graphics card or mobile device. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextureImporterOverride)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#TextureFormat) where colors can have a higher range than 0 through 1. Image file formats like .exr or .hdr are often used for HDR image data. At runtime and on the GPU, there are several HDR formats, trading off accuracy, range and memory usage.
  * **RGB** is a color model in which red, green and blue combine to reproduce an array of colors.
  * **RGBA** is a version of **RGB** with an alpha channel, which supports blending and opacity alteration.
  * **Variable bit rate (VBR)** means that bits per pixel is not a fixed value, and depends on the actual content instead. VBR only applies to **Crunch**compression** A method of storing data that reduces the amount of storage space it requires. See [Texture Compression](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextureImporterOverride), [Animation Compression](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AnimationClip.html#AssetProperties), [Audio Compression](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioClip.html), [Build Compression](https://docs.unity3d.com/6000.0/Documentation/Manual/ReducingFilesize.html).  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#compression)**, and only texture size on disk. The size in memory is the same as when using the underlying texture format (for example, RGB Compressed DXT1 for RGB Crunched DXT1).


## Textures for use on 3D models
Textures are applied to objects using [Materials](https://docs.unity3d.com/6000.0/Documentation/Manual/Materials.html)An asset that defines how a surface should be rendered. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Material.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Material). Materials use specialised graphics programs called [Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) to render a texture on the mesh surface. Shaders can implement lighting and colouring effects to simulate shiny or bumpy surfaces among many other things. They can also make use of two or more textures at a time, combining them for even greater flexibility.
You should make your textures in dimensions that are to the power of two (e.g. 32x32, 64x64, 128x128, 256x256, etc.) Simply placing them in your project’s Assets folder is sufficient, and they will appear in the Project View.
Once your texture has been imported, you should assign it to a [Material](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Material.html). The material can then be applied to a mesh, **Particle System** A component that simulates fluid entities such as liquids, clouds and flames by generating and animating large numbers of small 2D images in the scene. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ParticleSystem.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#particlesystem), or **GUI Texture**. Using the **Import Settings** , it can also be converted to a **Cubemap** A collection of six square textures that can represent the reflections in an environment or the skybox drawn behind your geometry. The six squares form the faces of an imaginary cube that surrounds an object; each face represents the view along the directions of the world axes (up, down, left, right, forward and back). [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Cubemap-landing.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Cubemap) or **Normalmap** for different types of applications in the game. For more information about importing textures, please read the [Texture Component page](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextureImporter.html).
## 2D graphics
In 2D games, the **Sprites** A 2D graphic objects. If you are used to working in 3D, Sprites are essentially just standard textures but there are special techniques for combining and managing sprite textures for efficiency and convenience during development. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/sprite-landing.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Sprite) are implemented using textures applied to flat meshes that approximate the objects’ shapes.
![Sprite from a 3D viewpoint](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/SpriteFrom3DViewPt.png) Sprite from a 3D viewpoint
An object in a 2D game may require a set of related graphic images to represent animation frames or different states of a character. Special techniques are available to allow these sets of images to be designed and rendered efficiently. See the manual page about the [Sprite Editor](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/sprite-editor/sprite-editor-landing.html) for more information.
## GUI
A game’s _graphic user interface_ (GUI) consists of graphics that are not used directly in the game **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) but are there to allow the player to make choices and see information. For example, the score display and the options menu are typical examples of game GUI. These graphics are clearly very different from the kind used to detail a mesh surface but they are handled using standard Unity textures nevertheless. See the manual chapter on [GUI Scripting Guide](https://docs.unity3d.com/6000.0/Documentation/Manual/GUIScriptingGuide.html) for further details about Unity’s GUI system.
## Particles
Meshes are ideal for representing solid objects but less suited for things like flames, smoke and sparkles left by a magic spell. This type of effect is handled much better by **Particle Systems**. A _particle_ is a small 2D graphic representing a small portion of something that is basically fluid or gaseous, such as a smoke cloud. When many of these particles are created at once and set in motion, optionally with random variations, they can create a very convincing effect. For example, you might display an explosion by sending particles with a fire texture out at great speed from a central point. A waterfall could be simulated by accelerating water particles downward from a line high in the scene.
![Star particle system](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/ParticleSystemCone.png) Star particle system
Unity’s particle systems have a wealth of options for creating all kinds of fluid effects. See the [manual chapter](https://docs.unity3d.com/6000.0/Documentation/Manual/ParticleSystems.html) on the subject for further information. 
## Anisotropic filtering
Anisotropic filtering increases Texture quality when viewed from a grazing angle. This rendering is resource-intensive on the graphics card. Increasing the level of anisotropy is usually a good idea for ground and floor Textures. Use [Quality](https://docs.unity3d.com/6000.0/Documentation/Manual/class-QualitySettings.html) settings to force anisotropic filtering for all Textures or disable it completely. Although, if a texture has its ****Aniso level** The anisotropic filtering (AF) level of a texture. Allows you to increase texture quality when viewing a texture at a steep angle. Good for floor and ground textures. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextureImporter.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#AnisoLevel)** set to 0 in [Texture Import Settings](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextureImporter.html), forced anisotropic filtering does not appear on this texture.
![Anisotropy used on the ground Texture {No anisotropy \(left\) | Maximum anisotropy \(right\)} ](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/ImportingTextures-AnisoFiltering.png)
## Additional resources
  * [Editor GUI and Legacy GUI texture Import Settings window reference](https://docs.unity3d.com/6000.0/Documentation/Manual/texture-type-editor-gui-and-legacy-gui.html)
  * [Sprite (2D and UI) texture Import Settings window reference](https://docs.unity3d.com/6000.0/Documentation/Manual/texture-type-sprite.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/textures-getting-started.html)
Get started with textures
[](https://docs.unity3d.com/6000.0/Documentation/Manual/texture-types.html)
Texture types
