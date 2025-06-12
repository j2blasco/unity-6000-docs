* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/urp/Post-Processing-Panini-Projection.html

  * [Rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/rendering-and-post-processing.html)
  * [Post-processing and full-screen effects](https://docs.unity3d.com/6000.0/Documentation/Manual/post-processing-and-full-screen-effects.html)
  * [Post-processing and full-screen effects in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/post-processing-and-full-screen-effects-urp.html)
  * [Post-processing in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/post-processing-in-urp.html)
  * [Post-processing Volume Overrides reference for URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/EffectList.html)
  * Panini Projection Volume Override reference for URP


[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/Post-Processing-Motion-Blur.html)
Motion Blur Volume Override reference for URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/shared/lens-flare/post-processing-screen-space-lens-flare.html)
Add screen space lens flares in URP
# Panini Projection Volume Override reference for URP
![Scene with Panini Projection effect turned off.](https://docs.unity3d.com/6000.0/Documentation/uploads/urp/post-proc/panini-off.png) Scene with Panini Projection effect turned off. ![Scene with Panini Projection effect turned on.](https://docs.unity3d.com/6000.0/Documentation/uploads/urp/post-proc/panini.png) Scene with Panini Projection effect turned on.
This effect helps you to render perspective views in **scenes** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) with a very large field of view. Panini projection is a cylindrical projection, which means that it keeps vertical straight lines straight and vertical. Unlike other cylindrical projections, panini projection keeps radial lines through the center of the image straight too.
For more information about panini projection, refer to PanoTools’ wiki documentation on [General Panini Projection](https://wiki.panotools.org/The_General_Panini_Projection).
## Properties
**Property** | **Description**  
---|---  
**Distance** | Use the slider to set the strength of the distortion.  
**Crop to Fit** | Use the slider to crop the distortion to fit the screen. A value of 1 crops the distortion to the edge of the screen, but results in a loss of precision in the center if you set **Distance** to a high value.  
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/Post-Processing-Motion-Blur.html)
Motion Blur Volume Override reference for URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/shared/lens-flare/post-processing-screen-space-lens-flare.html)
Add screen space lens flares in URP
