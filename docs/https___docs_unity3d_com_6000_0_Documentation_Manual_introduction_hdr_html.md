* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/introduction-hdr.html

  * [Rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/rendering-and-post-processing.html)
  * [Color](https://docs.unity3d.com/6000.0/Documentation/Manual/graphics-color.html)
  * [High dynamic range (HDR)](https://docs.unity3d.com/6000.0/Documentation/Manual/hdr-landing.html)
  * Introduction to high dynamic range (HDR)


[](https://docs.unity3d.com/6000.0/Documentation/Manual/hdr-landing.html)
High dynamic range (HDR)
[](https://docs.unity3d.com/6000.0/Documentation/Manual/hdr-color-picker-reference.html)
HDR color picker reference
# Introduction to high dynamic range (HDR)
High dynamic range (HDR) is a technique that produces images with a greater dynamic range of luminosity than standard dynamic range (SDR) images, allowing for realistic depictions of color and brightness.
## How HDR works
In standard rendering, the red, green, and blue values of a **pixel** The smallest unit in a computer image. Pixel size depends on your screen resolution. Pixel lighting is calculated at every screen pixel. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/ShadowPerformance.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#pixel) are stored using an 8-bit value between 0 and 1, where 0 represents zero intensity and 1 represents the maximum intensity for the display device. This limited range of values doesn’t accurately reflect the way that we perceive light in real life and leads to unrealistic images when very bright or very dark elements are present.
In **HDR** high dynamic range  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#HDR) rendering, the pixel values are stored using floating point numbers. This allows for a much larger range of values that more accurately represents the way that the human eye perceives color and brightness.
## HDR in Unity
In Unity, you can use HDR images for internal rendering calculations. This feature is called HDR rendering. When HDR rendering is enabled, Unity renders the **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) to an HDR image buffer, and performs rendering operations, such as **post-processing** A process that improves product visuals by applying filters and effects before the image appears on screen. You can use post-processing effects to simulate physical camera and film properties, for example Bloom and Depth of Field. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/PostProcessingOverview.html) post processing, postprocessing, postprocess  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#post-processing) effects, using that HDR image. This means that the calculations are carried out using realistic values, which can lead to more realistic results.
On certain compatible platforms, Unity supports sending that HDR image to the display device. This feature is called HDR Output.
## Considerations for the use of HDR
HDR offers a variety of advantages and disadvantages which you should consider before you use HDR to ensure it is the correct choice.
### Advantages of using HDR
HDR offers the following advantages:
  * Colors are not lost in high intensity areas
  * Better bloom and glow support
  * Reduction of banding in low frequency lighting areas


### Disadvantages of using HDR
HDR offers the following disadvantages:
  * Increased VRAM usage
  * Additional computational cost of **tonemapping** The process of remapping HDR values of an image into a range suitable to be displayed on screen. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/PostProcessingOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Tonemapping), when used
  * Hardware anti-aliasing is not compatible with HDR rendering


## Render pipeline compatibility
For information on HDR Rendering and HDR Output in URP, see [HDR Output in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/post-processing/hdr-output.html).
For information on HDR Rendering and HDR Output in HDRP, see [HDR Output in HDRP](https://docs.unity3d.com/Packages/com.unity.render-pipelines.high-definition@15.0/manual/HDR-Output.html).
For any additional information about support for HDR Rendering and HDR Output in the Scriptable **Render Pipelines** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Renderpipeline) URP and HDRP, see the [Render pipeline feature comparison](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines-feature-comparison.html).
## Tonemapping
Tonemapping is the process of mapping color values from one range to another. When working with HDR, you must use tonemapping to convert the colors in the HDR image buffer so that the values are within a range that your display device can handle. If you do not use tonemapping, you can lose much of the detail and color information from the image, especially in very bright areas.
![An exceptionally bright scene rendered in HDR and output to SDR. Without tonemapping, most pixels appear out of range.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/WithoutTonemap.jpg) An exceptionally bright scene rendered in HDR and output to SDR. Without tonemapping, most pixels appear out of range. ![The same scene as above. But this time, tonemapping is bringing most intensities into a more plausible range. Note that adaptive tonemapping can even blend between above and this image thus simulating the adaptive nature of capturing media \(e.g. eyes, cameras\).](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/WithTonemap.jpg) The same scene as above. But this time, tonemapping is bringing most intensities into a more plausible range. Note that adaptive tonemapping can even blend between above and this image thus simulating the adaptive nature of capturing media (e.g. eyes, cameras).
When using HDR rendering with SDR output, you must use tonemapping to convert the HDR image buffer to an SDR image for display. Unity provides tonemapping post-processing effects that let you do this: the [Post-Processing Stack V2 package](https://docs.unity3d.com/Packages/com.unity.postprocessing@latest), the [URP integrated post-processing solution](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/integration-with-post-processing.html), and [HDRP integrated post-processing solution](https://docs.unity3d.com/Packages/com.unity.render-pipelines.high-definition@latest/index.html?subfolder=/manual/Post-Processing-Main.html) all contain tonemapping effects.
When using HDR rendering with HDR output, you can either:
  * Create your own tonemapping solution that converts the HDR image buffer directly to a compatible HDR format for display
  * Use Unity’s tonemapping post-processing effects to convert the HDR buffer to an SDR image (as above), and then use Unity’s automatic output tonemapping to convert that SDR image to a suitable output format. For more details of Unity’s automatic output tonemapping, see the documentation for [HDROutputSettings.automaticHDRTonemapping](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HDROutputSettings-automaticHDRTonemapping.html).
  * HDROutputSettings API added in [2020.1](https://docs.unity3d.com/2020.1/Documentation/Manual/30_search.html?q=newin20201) NewIn20201


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/hdr-landing.html)
High dynamic range (HDR)
[](https://docs.unity3d.com/6000.0/Documentation/Manual/hdr-color-picker-reference.html)
HDR color picker reference
