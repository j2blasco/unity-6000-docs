* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-color-emojis.html

  * [UI systems](https://docs.unity3d.com/6000.0/Documentation/Manual/UIToolkits.html)
  * [UI Toolkit](https://docs.unity3d.com/6000.0/Documentation/Manual/UIElements.html)
  * [Work with text](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-work-with-text.html)
  * Color emojis


[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-color-gradient.html)
Color gradients
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-advanced-text-generator.html)
Advanced Text Generator
# Color emojis
You can include color emojis and glyphs in text.
For Editor UI, you can include emojis directly, and it works because the Editor UI uses the default editor font fallbacks. 
For runtime UI, you must import a font file with color emojis and set it as the fallback emoji text asset.
![Color emojis example](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/font/NativeEmojiExample.png) Color emojis example
## Set up color emojis
Create a color emojis font asset and add it to the UITK Text Settings Fallback.
  1. In your project, import a font file that has color emojis in it.
  2. Right-click the font file, and then select **Create** > **Text Core** > **Font Asset** > **Color**. This ensures that you create the font asset with the correct shader (Sprite) and the correct atlas render mode (Color).
  3. In the **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector) window of the [UITK Text Settings](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-text-setting-asset.html), in the **Fallback Emoji Text Assets** section, from the **Text Asset List** , select the color emojis font asset.


## Include emojis in text
To include emojis in text, do any of the following:
  * Include emojis in text through their Unicode value. For example, enter `\U0001F601` to represent a smile.
  * Use your operating system virtual keyboard.
  * Copy the emojis from an external text editing tool and paste them in your text field.


## Control emoji fallback search
You can prioritize searching the **Fallback Emoji Text Assets** for emojis. For example, if a font includes black and white emojis, you can choose whether to use emojis from the primary font or the **Fallback Emoji Text Assets** list.
  1. In UI Builder, select the text element in the **Hierarchy** panel.
  2. In the **Inspector** panel, in the **Attributes** section, enable or disable the **Emoji Fallback Support** option:
     * **Enabled** : The system searches the **Fallback Emoji Text Assets** list first for any emoji characters.
     * **Disabled** : The system searches the primary font asset assigned to the text element first.


## Limitations
The color emojis feature doesn’t support the following:
  * Some OpenType font features, such as chain context and single substitution.
  * Apple fonts that use the AAT format, which is a predecessor to OpenType.
  * SVG color glyphs.
  * COLR Table Format version 2 (COLR v2), such as Noto Color Emoji.


Dynamic OS font asset has limited support on some iOS devices. The `Apple Color Emoji` font file found on macOS and several iOS devices works correctly. However, the `Apple Color Emoji-160px` found on newer iOS devices isn’t supported. Its emojis are encoded in JPEG format, which isn’t supported by FreeType.
## Additional resources
  * [Unicode Emojis Standard](http://unicode.org/Public/emoji/latest/)
  * [Font assets](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-font-asset-landing.html)
  * [Include sprites in text](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-sprite.html)
  * [Text Setting Asset](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-text-setting-asset.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-color-gradient.html)
Color gradients
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-advanced-text-generator.html)
Advanced Text Generator
