* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-font-asset-properties.html

  * [UI systems](https://docs.unity3d.com/6000.0/Documentation/Manual/UIToolkits.html)
  * [UI Toolkit](https://docs.unity3d.com/6000.0/Documentation/Manual/UIElements.html)
  * [Work with text](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-work-with-text.html)
  * [Font assets](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-font-asset-landing.html)
  * Font Asset properties reference


[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-font-asset.html)
Introduction to font assets
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-font-creator-properties.html)
Font Asset Creator properties reference
# Font Asset properties reference
You can adjust the properties of a font asset after the font asset is created. To adjust the properties of a font asset, select the font asset, and change the values of its properties in the **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector) window. 
## Font Asset properties
This section describes all the Font Asset properties.
### Face Info
Use the Face Info properties to control the font’s line metrics. 
![Line metrics](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/font/FontAssetLineMetrics.png) Line metrics **Property** | **Description**  
---|---  
**Family Name** | Name of the font used to create this font asset.  
**Style Name** | Style of the font used to create this font asset. For example, **Regular** , **Bold** , or **Italic**.  
**Point Size** | Font size in points used to generate the font asset.  
**Scale** | Scale the font. For example, a value of `1.5` scales glyphs to 150% of the original font size.  
**Line Height** | Distance between the tops of consecutive lines.  
  
If you set a line height greater than the sum of the **Ascent Line** and **Descent Line** , it creates in a gap between lines.  
  
If you set a line height smaller than the sum of the **Ascent Line** and **Descent Line** values, characters on different lines might overlap.  
**Ascent Line** | Maximum distance that glyphs can extend above the baseline. It corresponds to the top of a line.  
**Cap Line** | Distance between the base line and the tops of uppercase glyphs.  
**Mean Line** | Maximum height for non-ascending lowercase glyphs. For example, “a” and “c”, but not “b” and “d” which have ascenders.  
  
The tops of rounded glyphs sometimes extend a slightly above the mean line.  
**Baseline** | Height of the baseline.  
  
The baseline is the horizontal line that characters sit on.  
**Descent Line** | Maximum distance that glyphs can extend below the baseline.  
**Underline Offset** | Position of underlines relative to the baseline.  
**Underline Thickness** | Thickness of underlines.  
**Strikethrough Offset** | Position of strikethrough lines relative to the baseline.  
**Superscript Offset** | Offset superscript text from the baseline.  
**Superscript Size** | Scale superscript text relative to the original font size.  
**Subscript Offset** | Offset subscript text from the baseline.  
**Subscript Size** | Scale subscript text relative to the original font size.  
**Tab Width** | Width of a TAB character.  
### Generation Settings
You can change the generation settings for a font asset. For dynamic or dynamic OS font assets, you can change the settings directly in the Inspector Window without regenerating the atlas. To update the generation settings for a static font asset, select **Update Atlas Texture** , and make changes in the Font Asset Creator window and regenerate the font atlas. 
**Property** | **Description**  
---|---  
**Source Font File** | Source file used to generate the font asset.  
**Atlas Population Mode** |  [Mode to populate the font atlas](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-font-asset.html#atlas-population-modes).  
**Atlas Render Mode** |  [Mode to render the font atlas](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-font-asset.html#atlas-render-modes).  
**Sampling Point Size** | Size, in points, of characters in the font texture.  
**Padding** |  [Padding](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-font-asset.html#padding), in **pixels** The smallest unit in a computer image. Pixel size depends on your screen resolution. Pixel lighting is calculated at every screen pixel. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/ShadowPerformance.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#pixel), between characters in the font atlas texture.  
**Atlas Width** | Width of the font atlas texture.  
**Atlas Height** | Height of the font atlas texture.  
**Multi Atlas Textures** | Store glyphs in multiple atlas textures. [Enable this option if you need more than one atlas](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-font-asset.html#multi-atlas).  
**Clear Dynamic Data** | Clear all dynamic data and restore the font asset back to its default creation and empty state.  
**Get Font Features** | Determines whether to automatically retrieve OpenType font features as needed. Currently, UI Toolkit supports only Kerning Pair adjustments. When enabled (default), Kerning Pair adjustments are dynamically added to the Glyph Adjustment Table when required.  
### Atlas & Material
**Note** : Font material isn’t supported in the current release.
**Property** | **Description**  
---|---  
**Font Atlas** | Font texture atlas created when you generated the font Asset.  
### Font Weights
You can use the Font Weights options to control the appearance of bold and italicized text in the following ways:
  * Specify regular and italic fonts for weights ranging from 100 (Thin) to 900 (Black).
  * Use the **Italic Slant** and **Bold Weight** properties to define “fake” bolding and italicization. These settings adjust characters in the current font asset when you bold or italicize text. This limits you to regular and italic versions of original and bold text (equal to weights of 400 and 700 respectively).


The following table describes the properties for the **Italic Slant** and **Bold Weight** properties:
**Property** | **Description**  
---|---  
**Regular Weight** | Regular font weight to use when no font asset is available.  
**Bold Weight** | Bold font weight assumed when no font asset is available.  
**Regular Spacing** | Space between characters when using the regular text style.  
**Bold Spacing** | Space between characters when using the bold text style if you haven’t specified a Bold font asset.  
**Italic Slant** | Slant value for the italic typeface.  
**Tab Multiple** | This value is multiplied by the width of the font’s space character to calculate the tab size.  
### Fallback Font Assets
Manage the local [fallback font assets](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-fallback-font.html) list for this font asset.
**Note** : The local fallback has precedence over the global fallback set in the [UITK Text Settings](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-text-setting-asset.html) asset.
**Property** | **Description**  
---|---  
**Fallback Font Assets List** | Click **+** and **-** to add and remove font slots.   
Click the circle icon next to a font to open an Object Picker where you can choose a font asset.  
Drag the handles on the left side of any font asset to reorder the list.  
### Character Table
The character table contains information about each character in the font asset. You can adjust the attributes of an individual glyph to correct font problems. To do so, select **Edit Glyph**.
**Property** | **Description**  
---|---  
**Character Search** | Search the character list by character, ASCII value or Hex value.  
**UTF16** | ASCII decimal value of the character.  
**Unicode** | Unicode Hex value of the character.  
**Glyph ID** | ID of the character’s glyph.  
### Glyph Table
The glyph table contains information about each glyph in the font asset. You can adjust the attributes of an individual glyph to correct font problems. 
**Property** | **Description**  
---|---  
**Glyph Search** | Search the character list by character, ASCII value, or Hex value.  
  
Search results are ordered by ASCII value, lowest to highest.  
**Glyph Rect** | Define the rectangular area the character occupies in the font atlas.  
**Glyph Metrics** | Define the metrics of the glyph. The following metrics are available:  

  * **W** : Width of the character.
  * **H** : Height of the character.
  * **BX, BY** : Control the placement of the character’s sprite, defined at its top-left corner relative to its origin on the baseline.
  * **AD** : How far to advance along the baseline before placing the next character.
  * **Scale** : Scaling value that adjusts the size of the character.

  
### Glyph Adjustment Table
The glyph adjustment table Control spacing between specific pairs of characters. Some fonts include kerning information, which is imported automatically. You can add kerning pairs for fonts that don’t include them.
**Property** | **Description**  
---|---  
**Adjustment Pair Search** | Search the adjustment table by character or ASCII value.  
  
Search results include entries where either the left or right character matches the search string.  
  
Search results are ordered by the ASCII value of the left character, lowest to highest.  
**Glyph Properties** | Display a single glyph’s properties. Each glyph has its own entry.  
  
Click an entry to make it active. You can then edit the glyph, copy it, or remove it from the list. The following properties are available:  

  * **Char** (left and right): Left and right characters for the kerning pair.
  * **ID** (left and right): Left and right characters’ ASCII decimal values for the kerning pair.
  * **OX, OY** (left and right): Left and right horizontal (**X**) and vertical (**Y**) offsets relative to the character’s initial position in the kerning pair.
  * **AX** (left and right): How far to advance along the baseline before placing the next character in the kerning pair. The left **AX** value controls the distance between the characters in the kerning pair, while the right **AX** value controls the distance between the kerning pair and the next character.

  
## Additional resources
  * [Font asset](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-font-asset.html)
  * [Font Asset Creator properties](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-font-creator-properties.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-font-asset.html)
Introduction to font assets
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-font-creator-properties.html)
Font Asset Creator properties reference
