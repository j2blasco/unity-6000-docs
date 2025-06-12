* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-text-setting-asset.html

  * [UI systems](https://docs.unity3d.com/6000.0/Documentation/Manual/UIToolkits.html)
  * [UI Toolkit](https://docs.unity3d.com/6000.0/Documentation/Manual/UIElements.html)
  * [Work with text](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-work-with-text.html)
  * UITK Text Settings assets


[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-advanced-text-generator.html)
Advanced Text Generator
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-fallback-font.html)
Fallback font
# UITK Text Settings assets
UI Toolkit stores project-wide text settings in the UITK Text Settings asset. UI Toolkit uses a default UITK Text Settings asset for your text objects.
For runtime UI, you can create and assign a UITK Text Settings asset to the [Panel Setting](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-Runtime-Panel-Settings.html) asset, and edit the text setting properties:
  * To create a UITK Text Settings, select **Assets** > **Create** > **UI Toolkit** > **Text Settings**. This creates a UITK Text Settings asset with the default values.
  * To assign a UITK Text Settings to a Panel Setting, select the Panel Setting and drag the UITK Text Settings to the Text Settings field in the **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector) window.


**Note** : In the current release, you can’t change the default UITK Text Settings for Editor UI.
This section describes all the properties for the UITK Text Settings asset. The UITK Text Settings asset controls the default values for all text objects used within that Panel. 
You can edit the paths to store the font assets, **sprite** A 2D graphic objects. If you are used to working in 3D, Sprites are essentially just standard textures but there are special techniques for combining and managing sprite textures for efficiency and convenience during development. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/sprite-landing.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Sprite) assets, custom style sheets, and the color gradient presets. The paths must be a sub-folder of a `Resources` folder. Create a `Resources` folder if you don’t have one in your project.
## Default Font Asset
After you [create a font asset](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-font-asset.html) from a font file, you must place it in the path set to store all the font assets.
**Property** | **Description**  
---|---  
**Default Font Asset** | Default font to use when you create a new text object.  
**Path** | Path to store all the font assets.  
## Fallback Emoji Text Assets
Manage the global [fallback font assets](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-fallback-font.html) list for this font asset.
**Note** : The [local fallback set in the Font Asset Properties](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-font-asset-properties.html#fallback-font-assets) has precedence over the global fallback .
**Property** | **Description**  
---|---  
**Text Asset List** | Select **+** and **-** to add and remove font slots.   
Click the circle icon next to a font to open an Object Picker where you can choose a font asset.  
Drag the handles on the left side of any font asset to reorder the list.  
## Dynamic Font System Settings
Project-wide settings to handle missing glyphs.
**Property** | **Description**  
---|---  
**Missing Character Unicode** | Unicode of the character to use when a missing glyph isn’t in any of the fallback fonts.  
  
The default value of `0` produces the outline of a square.  
**Clear Dynamic Data on Build** | Clear all dynamic data and restore the font asset back to its default creation and empty state.  
**Disable Warnings** | Enable this if you don’t want to log a warning for every missing glyph.  
## Default Sprite Asset
After you [create a sprit asset](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-sprite.html), you must place it in the path set to store all the sprite assets. You can set a default sprite asset and reference the sprites in the default sprite asset by index or sprite name. 
**Property** | **Description**  
---|---  
**Default Sprite Asset** |  [Sprite asset](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-sprite.html) to use by default.  
**Missing Sprite Unicode** | Unicode of the sprite for a missing sprite.  
**Path** | Path to store all the sprite assets.  
## Sprite Asset Fallback
The fallback list set in the Panel Text Setting is called the global fallback. The [local fallback set in the Sprite Asset](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-sprite.html) has precedence over the global fallback list.
**Property** | **Description**  
---|---  
**Sprite Asset Fallback List** | Add or remove a sprite asset in the fallback list. You can also drag the handles on the left side of any sprit asset to reorder the list.  
## Default Style Sheet
After you create a custom style sheet, you must place it in the path set to store all the custom style sheet assets.
**Property** | **Description**  
---|---  
**Default Style Sheet** | Default [style sheet](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-style-sheet.html) to use by all text objects in the project.  
**Path** | Path to store all the custom style sheet assets.  
## Color Gradient Presets
Set the path to store all color gradients presets. 
**Property** | **Description**  
---|---  
**Path** | Path to store the Color Gradient presets.  
## Line Breaking for Asian Languages
To get correct line-breaking behavior for Asian languages, specify which characters behave as leading and following characters. 
**Property** | **Description**  
---|---  
**Leading Characters** | Specify the text file that contains the list of leading characters.  
**Following Characters** | Specify the text file that contains the list of following characters.  
**Korean Line Breaking Rules** | Enable this to use modern rules.  
## Additional resources
  * [Font assets](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-font-asset.html)
  * [Style sheets assets](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-style-sheet.html)
  * [Include sprites in text](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-sprite.html)
  * [Color gradients](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-color-gradient.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-advanced-text-generator.html)
Advanced Text Generator
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-fallback-font.html)
Fallback font
