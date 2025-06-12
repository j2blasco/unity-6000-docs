* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-font-creator-properties.html

  * [UI systems](https://docs.unity3d.com/6000.0/Documentation/Manual/UIToolkits.html)
  * [UI Toolkit](https://docs.unity3d.com/6000.0/Documentation/Manual/UIElements.html)
  * [Work with text](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-work-with-text.html)
  * [Font assets](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-font-asset-landing.html)
  * Font Asset Creator properties reference


[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-font-asset-properties.html)
Font Asset properties reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-text-effects.html)
Text effects
# Font Asset Creator properties reference
You can generate and update the font atlas with the Font Asset Creator. To generate and update the font atlas, select **Update Atlas Texture** in the Font Asset’s **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector) window.
The following table describes all the Font Asset creator properties:
**Property** | **Description**  
---|---  
**Source Font File** | Source font to use to generate the font asset.  
**Sampling Point Size** | Font size, in points, used to generate the font texture. The higher the Sampling Point Size, the better the rendering quality, but it takes more atlas space. This property has the following options:  

  * **Auto Sizing** : Use the largest point size possible while still fitting all characters on the texture.  
  
This is the general option for [SDF](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-font-asset.html#sdf-fonts) fonts.
  * **Custom Size** : Use a custom point size to achieve pixel-accurate control over bitmap-only fonts.

  
**Padding** |  [Padding](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-font-asset.html#padding), in **pixels** The smallest unit in a computer image. Pixel size depends on your screen resolution. Pixel lighting is calculated at every screen pixel. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/ShadowPerformance.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#pixel), between characters in the font atlas texture.  
**Packing Method** | How to fit the characters into the font texture. Choose from the following options:  

  * **Optimum** : Find the largest possible automatic font size that still fits all characters in the texture. Use this option to generate the final font texture.
  * **Fast** : Compute character packing more quickly, but might use a smaller font size than the **Optimum** mode Use this option when to test out font asset creation.

  
**Atlas Resolution** | Width and height of the font texture, in pixels.  
  
A resolution of `512 x 512` is fine for most fonts if you only include ASCII characters. Fonts with more characters may require larger resolutions, or multiple atlases.   
  
For an SDF font, a higher resolution produces finer gradients, and therefore higher quality text.  
**Character Set** | The characters in a font file aren’t included in the font Asset automatically. You must specify which ones you need. You can select a predefined character set, provide a list of characters to include, or include all the characters in an existing font asset or text asset. Choose from the following options:  

  * **ASCII** : Include the visible characters in the ASCII character set.
  * **Extended ASCII** : Include the visible characters in the extended ASCII character set.
  * **ASCII Lowercase** : Include only visible lower-case characters from the ASCII character set.
  * **ASCII Lowercase** : Include only visible lower-case characters from the ASCII character set.
  * **ASCII Lowercase** : Include only visible lower-case characters from the ASCII character set.
  * **Numbers + Symbols** : Include only the visible numbers and symbols from the ASCII character set.
  * **Custom Range** : Include a range of characters that you define.  
  
Enter a sequence of decimal values, or ranges of values, to specify which characters to include. Use a hyphen to separate the first and last values of a range. Use commas to separate values and ranges (for example `32-126,160,8230`).  
  
You can also choose an existing font asset to include the characters in that asset.
  * **Unicode Range (Hex)** : Include a range of characters that you define.  
  
Enter a sequence of unicode hexadecimal values, or ranges of values, to specify which characters to include. Use a hyphen to separate the first and last values of a range. Use commas to separate values and ranges (for example `20-7E,A0,2026`).  
  
You can also choose an existing font asset to include the characters in that asset.
  * **Custom Characters** : Include a range of characters that you define.  
  
Enter a sequence of characters to specify which characters to include. Enter characters one after the other, with no spaces or delimiting characters in between, such as `abc123*#%`.  
  
You can also choose an existing font asset to include the characters in that asset.
  * **Characters from File** : Include all the characters in a text asset that you specify. Use this option when you want to save your character set.

  
**Render Mode** |  [Mode](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-font-asset.html#atlas-render-modes) to render the font atlas.  
**Get Kerning Pairs** | Copy the kerning data from the font.  
  
Kerning data is used to adjust the spacing between specific character pairs to produce a more visually pleasing result.  
  
**Note:** It isn’t always possible to import kerning data. Some fonts store kerning pairs in their glyph positioning (GPOS) table, which is not supported. Other fonts do not store kerning pairs at all.  
## Additional resources
  * [Font asset](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-font-asset.html)
  * [Font asset properties reference](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-font-asset-properties.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-font-asset-properties.html)
Font Asset properties reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-text-effects.html)
Text effects
