* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-sprite.html

  * [UI systems](https://docs.unity3d.com/6000.0/Documentation/Manual/UIToolkits.html)
  * [UI Toolkit](https://docs.unity3d.com/6000.0/Documentation/Manual/UIElements.html)
  * [Work with text](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-work-with-text.html)
  * Include sprites in text


[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-style-sheet.html)
Style sheets
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-sprite-asset-properties.html)
Sprite Asset properties reference
# Include sprites in text
To use sprites in your rich text tags, such as emojis, you need a **sprite** A 2D graphic objects. If you are used to working in 3D, Sprites are essentially just standard textures but there are special techniques for combining and managing sprite textures for efficiency and convenience during development. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/sprite-landing.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Sprite) asset. You create sprite assets from atlas [textures](https://docs.unity3d.com/6000.0/Documentation/Manual/Textures.html)An image used when rendering a GameObject, Sprite, or UI element. Textures are often applied to the surface of a mesh to give it visual detail. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextureImporter.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#texture) that contain a set of sprites.
![An example atlas texture](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/font/sprite-asset.png) An example atlas texture
You can use as many sprite atlases and assets as you want. However, if you use multiple atlases per text object results in multiple draw calls for that object and consumes more system resources. As a rule, when you import multiple sprites, pack them into a single atlas to reduce draw calls. Make sure the **sprite atlas** A utility that packs several sprite textures tightly together within a single texture known as an atlas. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/atlas/v2/v2-landing.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#SpriteAtlas) has a suitable resolution for your target platform.
Use the [`<sprite>` rich text tag](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-supported-tags.html#sprite) to include sprites in your text.
See information for all the [Sprite asset properties](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-sprite-asset-properties.html).
## Create a sprite asset
You create sprite assets from atlas textures. Although sprite assets and their source textures are separate entities, you must keep the source textures in the project after you’ve created the sprite assets. 
To create a sprite asset:
  1. [Import the sprite atlas](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/sprite-landing.html).
  2. Select the atlas and change the following texture options in the **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector) window:
     * Set the **Texture Type** to **Sprite (2D and UI)**.
     * Set the **Sprite Mode** to **Multiple**.
  3. Select **[Sprite Editor](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/sprite-editor/sprite-editor-landing.html)** and divide the texture into individual sprites.
  4. Right-click the sprite and select **Create** > **Text Core** > **Sprite Asset**. This creates a new sprite asset.
  5. From the Inspector window, you can further customize the appearance and names of each glyph. Refer to [Sprite Asset properties](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-sprite-asset-properties.html) for more information.
  6. Place the sprite asset to the path set in the [UITK Text Settings](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-text-setting-asset.html).


Once you’ve created the sprite asset, you can revert the atlas texture’s **Texture Type** to its original setting.
## Use a sprite asset
To use sprites in the rich text tag, reference the sprite asset name and the sprite name as `<sprite="assetName" name="spriteName">` or by index as `<sprite="assetName" index=1>`.
You can add the `tint=1` attribute to the tag to tint the sprite with the text object’s vertex color. You can also choose a different color by adding a color attribute to the tag, for example: `<sprite="assetName" index=1 color=#55FF55FF>`.
For runtime UI, if you have set a sprite asset as the default in the [UITK Text Settings](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-text-setting-asset.html), you can omit the asset name as `<sprite index=1>` (or shorthand `<sprite=1>`), or `<sprite name="spriteName">`.
## Assign and use Unicode for a sprite
You can assign a Unicode to a sprite and use the Unicode directly in your text object instead of the `<sprite>` tag.
For example, the Unicode for a smiling face emoji is `U+1F60A`. To assign it to a sprite in your sprite asset:
  1. In the sprite asset’s Inspector window, find the glyph in the **Sprite Character Table**. You can browse or search by index or name.
  2. Click the glyph to enable the edit mode.
  3. In the Unicode box, enter `+1F60A`.
  4. Click the **Unicode** label to save your changes. The Unicode changes to `0xF1F60A`.


To use the smiling face emoji in your text object, enter `\U00F1F60A`.
## Additional resources
  * [Sprite asset properties](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-sprite-asset-properties.html)
  * [Rich text tags](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-rich-text-tags.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-style-sheet.html)
Style sheets
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-sprite-asset-properties.html)
Sprite Asset properties reference
