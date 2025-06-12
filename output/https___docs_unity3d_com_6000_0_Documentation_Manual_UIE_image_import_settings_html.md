* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-image-import-settings.html

  * [UI systems](https://docs.unity3d.com/6000.0/Documentation/Manual/UIToolkits.html)
  * [UI Toolkit](https://docs.unity3d.com/6000.0/Documentation/Manual/UIElements.html)
  * [Style UI](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-USS.html)
  * [USS properties](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uss-properties.html)
  * Image import settings


[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIB-styling-ui-backgrounds.html)
Set background images
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-Transform.html)
USS transform
# Image import settings
After you have imported an image to your project, for the most intuitive results, it’s recommended that you apply certain import settings for Textures, **Sprites** A 2D graphic objects. If you are used to working in 3D, Sprites are essentially just standard textures but there are special techniques for combining and managing sprite textures for efficiency and convenience during development. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/sprite-landing.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Sprite), and Vector images before you use them as a background for a **visual element** A node of a visual tree that instantiates or derives from the C# [`VisualElement`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.html) class. You can style the look, define the behaviour, and display it on screen as part of the UI. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-VisualTree.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Visualelement) in the UI Builder.
## Texture
The recommended import settings for a **Texture** image that you use as a background for a visual element are as follows.
Use the following settings for Default Texture types, and Editor GUI and Legacy GUI Texture types:
**Property** | **Value**  
---|---  
**Non-Power of 2** | None  
****Compression** A method of storing data that reduces the amount of storage space it requires. See [Texture Compression](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextureImporterOverride), [Animation Compression](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AnimationClip.html#AssetProperties), [Audio Compression](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioClip.html), [Build Compression](https://docs.unity3d.com/6000.0/Documentation/Manual/ReducingFilesize.html).  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#compression)** | None  
**Alpha Is Transparency** | true  
Use the following settings for Sprite (2D and UI) Texture types:
**Property** | **Value**  
---|---  
**Compression** | None  
**Alpha Is Transparency** | true  
**Sprite Mode** | Single  
****Mesh** The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/mesh.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Mesh) Type** | Tight  
## Sprites
The recommended import settings for a **Sprite** image that you use as a background for a visual element:
**Property:** | **Value:**  
---|---  
**Compression** | None  
**Alpha Is Transparency** | true  
**Sprite Mode** | Multiple if file contains multiple sprites, Single otherwise.  
**Mesh Type** | Tight  
## Vector images
The recommended import settings for a SVG **Vector** image that you use as a background for a visual element:
**Property:** | **Value:**  
---|---  
**Generated Asset Type** | UI Toolkit Vector Image  
**Tessellation Settings** | Basic  
**Target Resolution** | Lowest value that produces satisfactory results  
**Tip** : 
  * You can [apply default presets to Assets by folder](https://docs.unity3d.com/6000.0/Documentation/Manual/DefaultPresetsByFolder.html) to automatically set your desired import settings.
  * All image types are subject to [dynamic atlasing](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.DynamicAtlasSettings.html) if they’re not already in an atlas. (An image is in an atlas if imported as a Sprite with **Sprite Mode** set to **Multiple** , or if you have manually added it to a [Sprite Atlas](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/atlas/atlas-landing.html)A utility that packs several sprite textures tightly together within a single texture known as an atlas. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/atlas/v2/v2-landing.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#SpriteAtlas) asset.) You can configure dynamic atlasing in a [Panel Settings](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-Runtime-Panel-Settings.html) asset.


## Additional resources
  * [UIE-uxml-element-Image](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-Image.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIB-styling-ui-backgrounds.html)
Set background images
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-Transform.html)
USS transform
