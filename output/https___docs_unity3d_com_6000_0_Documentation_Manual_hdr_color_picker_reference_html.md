* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/hdr-color-picker-reference.html

  * [Rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/rendering-and-post-processing.html)
  * [Color](https://docs.unity3d.com/6000.0/Documentation/Manual/graphics-color.html)
  * [High dynamic range (HDR)](https://docs.unity3d.com/6000.0/Documentation/Manual/hdr-landing.html)
  * HDR color picker reference


[](https://docs.unity3d.com/6000.0/Documentation/Manual/introduction-hdr.html)
Introduction to high dynamic range (HDR)
[](https://docs.unity3d.com/6000.0/Documentation/Manual/hdr-birp-landing.html)
Color space and HDR in the Built-in Render Pipeline
# HDR color picker reference
The **HDR** high dynamic range  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#HDR) Color picker looks similar to the ordinary color picker, but it contains additional controls for adjusting the color’s exposure.
**Property:** | **Function:**  
---|---  
Mode | When using **HSV** or **RGB 0–255** mode, the color picker treats exposure adjustments independently from color channel data. However, the color channel data displayed in **RBG (0–1.0)** mode reflects the results of your exposure adjustment on the color data.  
  
Unlike the ordinary color picker, you can directly enter float values greater than 1.0 when editing color channels in **RGB 0–1.0** mode. In this case, the color picker derives the **Intensity** value automatically from the value you set.  
  
The default setting for this property is **RGB 0–255**.  
**RGBA** | Use the slider or text box to define a RGBA value. If the color picker has a **Hexadecimal** property, the hex value automatically updates to reflect the RGBA values.  
**Intensity** | Use the **Intensity** slider to overexpose or underexpose the color. Each positive step along the slider provides twice as much light as the previous slider position, and each negative step provides half as much light.  
  
Use the exposure swatches under the **Intensity** slider to preview what the current color value looks like within a range of two steps in either direction. To quickly adjust the color’s exposure, click a preview swatch.  
**Swatches** | Use the **Swatches** section to save colors to a [swatch library](https://docs.unity3d.com/6000.0/Documentation/Manual/EditingValueProperties#swatch-libraries). You can reuse, save, and share colors, gradients, and **animation curves** Allows you to add data to an imported clip so you can animate the timings of other items based on the state of an animator. For example, for a game set in icy conditions, you could use an extra animation curve to control the emission rate of a particle system to show the player’s condensing breath in the cold air. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimationCurvesOnImportedClips.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#AnimationCurves).  
**Note** : Whenever you close the HDR Color window and reopen it, the window derives the color channel and intensity values from the color you are editing. Because of this, you might see slightly different values for the color channels in **HSV** and **RGB 0–255** mode or for the **Intensity** slider, even though the color channel values in **RGB 0–1.0** mode are the same as the last time you edited the color.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/introduction-hdr.html)
Introduction to high dynamic range (HDR)
[](https://docs.unity3d.com/6000.0/Documentation/Manual/hdr-birp-landing.html)
Color space and HDR in the Built-in Render Pipeline
