* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-fallback-font.html

  * [UI systems](https://docs.unity3d.com/6000.0/Documentation/Manual/UIToolkits.html)
  * [UI Toolkit](https://docs.unity3d.com/6000.0/Documentation/Manual/UIElements.html)
  * [Work with text](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-work-with-text.html)
  * Fallback font


[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-text-setting-asset.html)
UITK Text Settings assets
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-examples.html)
Examples
# Fallback font
Each font asset has a limited number of characters. When you use a character that isn’t in the current font asset, TextCore searches the **Fallback List** until it finds a font asset with that character. The text element then uses that font asset to render the character.
You can set a list of fallback fonts to distribute fonts over multiple textures, or use different fonts for specific characters. It requires extra computing resources to search the list for missing characters and additional draw calls to use additional fonts.
You can use the same character for multiple font assets in the fallback list. Match the style of the characters in the fallback list to style of the main font asset as possible as you can.
## Fallback font usage
In general, use fallback font assets to:
  * Work with languages that have large alphabets, such as Chinese, Korean, and Japanese. Use fallback fonts to distribute an alphabet across several assets.
  * Include special characters from other alphabets in your text.


**Tips** : Dynamic OS font assets are great candidates for fallback font assets.
## Fallback font chain
You can create local and global fallback font asset lists. Set local font asset lists in the [Font Assets property](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-font-asset-properties.html) and set global font asset lists in [UITK Text Settings](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-text-setting-asset.html). In addition to the fallback fonts, TextCore searches other assets, such as the default **sprite** A 2D graphic objects. If you are used to working in 3D, Sprites are essentially just standard textures but there are special techniques for combining and managing sprite textures for efficiency and convenience during development. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/sprite-landing.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Sprite) asset, for missing glyphs. Together, these assets form the fallback chain.
The following is the asset order in the fallback chain:
  1. Local fallback font assets list
  2. Global fallback font assets list
  3. Default sprite asset
  4. Dynamic OS fallback
  5. Missing glyphs character


## Additional resources
  * [Font assets](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-font-asset.html)
  * [Include sprites in text](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-sprite.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-text-setting-asset.html)
UITK Text Settings assets
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-examples.html)
Examples
