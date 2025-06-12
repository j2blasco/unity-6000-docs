* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/gamma-textures-linear-color-space.html

  * [Rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/rendering-and-post-processing.html)
  * [Color](https://docs.unity3d.com/6000.0/Documentation/Manual/graphics-color.html)
  * [Color spaces](https://docs.unity3d.com/6000.0/Documentation/Manual/color-spaces-landing.html)
  * [Linear color space](https://docs.unity3d.com/6000.0/Documentation/Manual/linear-color-space-landing.html)
  * Gamma Textures in linear color space


[](https://docs.unity3d.com/6000.0/Documentation/Manual/linear-color-space.html)
Introduction to linear color space in Unity
[](https://docs.unity3d.com/6000.0/Documentation/Manual/linear-textures.html)
Linear textures
# Gamma Textures in linear color space
The Unity Editor allows you to work with traditional gamma color space as well as linear color space. You can work in linear colour space even if your [Textures](https://docs.unity3d.com/6000.0/Documentation/Manual/Textures.html)An image used when rendering a GameObject, Sprite, or UI element. Textures are often applied to the surface of a mesh to give it visual detail. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextureImporter.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#texture) are in gamma color space.
**Note:** If your Textures are in linear color space, you need to disable sRGB sampling. See documentation on [Linear Textures](https://docs.unity3d.com/6000.0/Documentation/Manual/linear-textures.html) for more information.
Linear rendering gives a different look to the rendered **Scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene). When you have authored a project to look good when rendering in gamma space, it is unlikely to look great when you change to linear rendering. Because of this, if you move to linear rendering from gamma rendering it may take some time to tweak the project so that it looks as good as before. However, the switch ultimately enables more consistent and realistic rendering and so may be worth the time spent on it. You are likely to have to tweak Textures, Materials and Lights.
## Lightmapping
The lighting calculations in the **lightmapper** A tool in Unity that bakes lightmaps according to the arrangement of lights and geometry in your scene. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Lightmapping.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Lightmapper) are always done in linear space (see [Color space](https://docs.unity3d.com/6000.0/Documentation/Manual/color-spaces-landing.html) for more information). The lightmaps are always stored in gamma space. This means that the **lightmap** A pre-rendered texture that contains the effects of light sources on static objects in the scene. Lightmaps are overlaid on top of scene geometry to create the effect of lighting. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Lightmapping.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Lightmap) textures are identical no matter whether you’re in gamma or linear color space.
When you are in linear color space, the texture sample gets converted from gamma to linear space when sampling the texture. When you’re in gamma color space, no conversion is needed. Therefore, when you change the color space setting, you must rebake lightmaps: This happens automatically when Unity’s lighting is set to auto bake (which is the default).
### Importing lightmaps
The data in lightmap EXR files created by Unity is in linear space. It gets converted to gamma space during import. When bringing in lightmaps from an external lightmapper, mark the lightmaps as **Texture Type** : **Lightmap** in the [Texture Importer](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextureImporter.html). This setting makes sure sRGB sampling is bypassed on import.
## Linear supported platforms
Linear rendering is not supported on all platforms. The build targets that support the feature are:
  * Windows, Mac OS X and Linux (Standalone)
  * Android
  * iOS
  * Web


There is no fallback to gamma when linear rendering is not supported by the device. In this situation, the Player quits. You can check the active color space from a script by looking at [QualitySettings.activeColorSpace](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings-activeColorSpace.html).
On Android, linear rendering requires at least OpenGL ES 3.0 graphics API and Android 4.3.
On iOS, linear rendering requires the Metal graphics API.
On Web, linear rendering requires at least **WebGL** A JavaScript API that renders 2D and 3D graphics in a web browser. The Unity Web build option allows Unity to publish content as JavaScript programs which use HTML5 technologies and the WebGL rendering API to run Unity content in a web browser. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#WebGL) 2.0 graphics API.
Until the minimum requirements are satisfied, the Editor prevents you from building a Player and shows a notification. This is to avoid games that would render incorrectly on user devices being deployed to digital stores.
![The Unity Editor prevents building a Player for games that would render incorrectly](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/LinearRendering-UnityIncorrectRendering.png) The Unity Editor prevents building a Player for games that would render incorrectly
## Linear color space and HDR
When using **HDR** high dynamic range  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#HDR), rendering is performed in linear space into floating point buffers. These buffers have enough precision not to require conversion to and from gamma space whenever the buffer is accessed. This means that when rendering in linear mode, the framebuffers you use store the colors in linear space. Therefore, all blending and post process effects are implicitly performed in linear space. When the final backbuffer is written to, gamma correction is applied.
## Linear color space and non-HDR
When linear color space is enabled and HDR is not enabled, a special framebuffer type is used that supports sRGB read and sRGB write (convert from gamma to linear when reading, convert from linear to gamma when writing). When this framebuffer is used for blending or it is bound as a Texture, the values are converted to linear space before being used. When these buffers are written to, the value that is being written is converted from linear space to gamma space. If you are rendering in linear mode and non-HDR mode, all post-process effects have their source and target buffers created with sRGB read and write enabled so that **post-processing** A process that improves product visuals by applying filters and effects before the image appears on screen. You can use post-processing effects to simulate physical camera and film properties, for example Bloom and Depth of Field. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/PostProcessingOverview.html) post processing, postprocessing, postprocess  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#post-processing) and post-process blending occur in linear space.
* * *
  * 2017–06–19 Page amended 
  * Linear rendering for Web added in [2017.2](https://docs.unity3d.com/2017.2/Documentation/Manual/30_search.html?q=newin20172) NewIn20172


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/linear-color-space.html)
Introduction to linear color space in Unity
[](https://docs.unity3d.com/6000.0/Documentation/Manual/linear-textures.html)
Linear textures
