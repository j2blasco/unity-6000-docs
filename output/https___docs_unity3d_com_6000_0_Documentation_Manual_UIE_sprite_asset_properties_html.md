* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-sprite-asset-properties.html

  * [UI systems](https://docs.unity3d.com/6000.0/Documentation/Manual/UIToolkits.html)
  * [UI Toolkit](https://docs.unity3d.com/6000.0/Documentation/Manual/UIElements.html)
  * [Work with text](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-work-with-text.html)
  * [Include sprites in text](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-sprite.html)
  * Sprite Asset properties reference


[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-sprite.html)
Include sprites in text
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-color-gradient.html)
Color gradients
# Sprite Asset properties reference
This page describes the **sprite** A 2D graphic objects. If you are used to working in 3D, Sprites are essentially just standard textures but there are special techniques for combining and managing sprite textures for efficiency and convenience during development. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/sprite-landing.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Sprite) asset properties.
Property | Description  
---|---  
**Update Sprite Asset** | Sync the sprite asset with the latest [Sprite Editor](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/sprite-editor/sprite-editor-landing.html) changes.  
## Atlas & Material
Property | Description  
---|---  
****Sprite Atlas** A utility that packs several sprite textures tightly together within a single texture known as an atlas. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/atlas/v2/v2-landing.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#SpriteAtlas)** | A reference to the sprite asset’s source texture.  
**Default Material** | A reference to the sprite asset’s material, which it uses to render sprites.  
## Fallback Sprite Assets
When a glyph doesn’t exist in this sprite asset, TextCore searches the fallback sprite assets list for the missing glyph. 
Property | Description  
---|---  
**Fallback Sprite Asset List** | This is the local fallback list. The local fallback list has precedence over the global fallback list set in the [UITK Text Settings](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-text-setting-asset.html) asset. You can add or remove a sprite asset in the fallback list. You can also drag the handles on the left side of any sprite asset to reorder the list.  
## Sprite Character Table
Manage the sprites in this asset.
  * Click a sprite to make it active.
  * Click **Up** or **Down** to move the sprite up or down in the list.
  * To move the sprite to a specific position, enter the index ID of the position in the text field and then click **Goto** to move the sprite to that position in the list.  
**Note:** Moving a sprite updates its index ID and the index IDs of all preceding sprites accordingly.
  * Click **+** to add a copy of the sprite to the list.
  * Click **-** to remove the sprite from the list.

Property | Description  
---|---  
**Index** | Unique index ID for the sprite, based on its position in the list.   
You can use it to reference the sprite in the [`<sprite>` rich text tag](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-supported-tags.html#sprite).  
**Unicode** | Unicode for the sprite. For more information, refer to [Assign and use Unicode for a sprite](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-sprite.html#assign-and-use-unicode-for-a-sprite).  
**Name** | Unique name for the sprite.  
You can use it to reference the sprite in the [`<sprite>` rich text tag](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-supported-tags.html#sprite).  
## Sprite Glyph Table
Manage the glyphs in this asset.
Property | Description  
---|---  
**Glyph Rect** | Define the rectangular area that the character occupies in the sprite atlas. 
  * **X, Y** : The coordinates of the glyph.
  * **W, H** : The width and height of the glyph.

  
**Glyph Metrics** | Metrics for the sprite. 
  * **W** : The width of the sprite.
  * **H** : The height of the sprite.
  * **BX, BY** : Stand for “Bearing X” and “Bearing Y,” which define the horizontal and vertical offsets from the glyph bounding box’s origin to the start of the drawings.
  * **AD** : Horizontal advance refers to the distance from the hozitontal origin of the glyph to the start of the next glyph.

  
## Global Offsets & Scale
Offsets and scale settings for all sprites in the asset.
Property | Description  
---|---  
**OX, OY** | Control the placement of the sprite, defined at its top-left corner relative to its origin on the baseline.  
**ADV** | How far to advance along the baseline to place the next sprite.  
**SF** | Adjust the size of the sprite.  
## Additional resources
  * [Include sprites in text](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-sprite.html)
  * [Rich text tags](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-rich-text-tags.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-sprite.html)
Include sprites in text
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-color-gradient.html)
Color gradients
