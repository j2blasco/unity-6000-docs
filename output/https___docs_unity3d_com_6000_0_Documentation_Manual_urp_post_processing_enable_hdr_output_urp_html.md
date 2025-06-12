* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/urp/post-processing/enable-hdr-output-urp.html

  * [Rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/rendering-and-post-processing.html)
  * [Color](https://docs.unity3d.com/6000.0/Documentation/Manual/graphics-color.html)
  * [High dynamic range (HDR)](https://docs.unity3d.com/6000.0/Documentation/Manual/hdr-landing.html)
  * [HDR](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/post-processing/hdr-in-urp.html)
  * Enable HDR Output in URP


[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/post-processing/hdr-output-debug-views-urp.html)
HDR Output debug views in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/post-processing/hdr-output-implement-custom-overlay.html)
Implement an HDR Output compatible custom overlay in URP
# Enable HDR Output in URP
HDR Output in URP requires you to enable multiple properties to work. These properties allow URP to render **scenes** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) correctly with **HDR** high dynamic range  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#HDR) Rendering and then output the HDR values to a display.
To activate HDR output, follow these steps.
  1. Locate the [URP Asset](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/universalrp-asset.html) in the Project window under **Assets** > **Settings**.
  2. Navigate to **Quality** > **HDR** and enable the checkbox to enable **HDR**.
  3. Navigate to **Edit** > **Project Settings** > **Player** > **Other Settings** and enable the following settings:
     * **Allow HDR Display Output**
     * **Use HDR Display Output**


**Note** : Only enable **Use HDR Display Output** if you need the main display to use HDR Output.
If you switch to a URP Asset that does not have HDR enabled, URP disables HDR Output until you change to a URP Asset with HDR enabled.
**Note** : When HDR Output is active the color grading mode is HDR by default, even if a different Color Grading Mode is active in the URP Asset.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/post-processing/hdr-output-debug-views-urp.html)
HDR Output debug views in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/post-processing/hdr-output-implement-custom-overlay.html)
Implement an HDR Output compatible custom overlay in URP
