* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/urp/post-processing/hdr-output-debug-views-urp.html

  * [Rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/rendering-and-post-processing.html)
  * [Color](https://docs.unity3d.com/6000.0/Documentation/Manual/graphics-color.html)
  * [High dynamic range (HDR)](https://docs.unity3d.com/6000.0/Documentation/Manual/hdr-landing.html)
  * [HDR](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/post-processing/hdr-in-urp.html)
  * HDR Output debug views in URP


[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/post-processing/hdr-output.html)
HDR Output in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/post-processing/enable-hdr-output-urp.html)
Enable HDR Output in URP
# HDR Output debug views in URP
URP offers three debug views for **HDR** high dynamic range  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#HDR) rendering.
These views are:
  * [Gamut View](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/post-processing/hdr-output-debug-views-urp.html#gamut-view)
  * [Gamut Clip](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/post-processing/hdr-output-debug-views-urp.html#gamut-clip)
  * [Values exceeding Paper White](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/post-processing/hdr-output-debug-views-urp.html#values-exceeding-paper-white)


To access them, navigate to **Window** > **Analysis** > **Render Pipeline Debugger** > **Lighting** > **HDR Debug Mode**.
## Gamut View
![Gamut Debug View](https://docs.unity3d.com/6000.0/Documentation/uploads/urp/post-proc/hdr/HDR-Output-GamutView.png) Gamut Debug View
The triangles in this debug view indicate which parts of three specific color gamuts this **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) covers. The small triangle displays the [Rec709](https://en.wikipedia.org/wiki/Rec._709) gamut values, the medium triangle displays the [P3-D65](https://en.wikipedia.org/wiki/DCI-P3) gamut values, and the large triangle displays the [Rec2020](https://en.wikipedia.org/wiki/Rec._2020) gamut values. This enables you to check color plot changes while color grading. It can also help you ensure that you benefit from the wider color gamut available in HDR.
## Gamut Clip
![Gamut Clip Debug View](https://docs.unity3d.com/6000.0/Documentation/uploads/urp/post-proc/hdr/HDR-Output-GamutClip.png) Gamut Clip Debug View
This debug view indicates the relationship between scene values and specific color gamuts. Areas of the screen with values within the Rec709 gamut are green, areas outside of the Rec709 gamut but inside the P3-D65 gamut are blue, and areas outside of both are red.
## Values exceeding Paper White
![Values Exceeding Paper White Debug View](https://docs.unity3d.com/6000.0/Documentation/uploads/urp/post-proc/hdr/HDR-Output-OverPaperWhite.png) Values Exceeding Paper White Debug View
This debug view uses a color coded gradient to indicate parts of the Scene that exceed the Paper White value and Max Nits. The gradient ranges from yellow to red and blue. Yellow corresponds to **Paper White** +1, red corresponds to **Max Nits** , and blue corresponds to **Max Nits** +1.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/post-processing/hdr-output.html)
HDR Output in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/post-processing/enable-hdr-output-urp.html)
Enable HDR Output in URP
