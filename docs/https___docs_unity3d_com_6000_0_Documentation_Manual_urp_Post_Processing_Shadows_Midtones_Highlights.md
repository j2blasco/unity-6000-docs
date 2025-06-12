* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/urp/Post-Processing-Shadows-Midtones-Highlights.html

  * [Rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/rendering-and-post-processing.html)
  * [Post-processing and full-screen effects](https://docs.unity3d.com/6000.0/Documentation/Manual/post-processing-and-full-screen-effects.html)
  * [Post-processing and full-screen effects in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/post-processing-and-full-screen-effects-urp.html)
  * [Post-processing in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/post-processing-in-urp.html)
  * [Post-processing Volume Overrides reference for URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/EffectList.html)
  * Shadows Midtones Highlights Volume Override reference for URP


[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/shared/lens-flare/post-processing-screen-space-lens-flare.html)
Add screen space lens flares in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/Post-Processing-Split-Toning.html)
Split Toning Volume Override reference for URP
# Shadows Midtones Highlights Volume Override reference for URP
The **Shadows Midtones Highlights** effect separately controls the shadows, midtones, and highlights of the render. Unlike [Lift, Gamma, Gain](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/Post-Processing-Lift-Gamma-Gain.html), you can use this effect to precisely define the tonal range for shadows, midtones, and highlights.
## Properties
**Property** | **Description**  
---|---  
**Shadows** | Use this to control the shadows.Use the trackball to select the color URP should shift the hue of the shadows to.Use the slider to offset the color lightness of the trackball color.  
**Midtones** | Use this to control the midtones.Use the trackball to select the color URP should shift the hue of the midtones to.Use the slider to offset the color lightness of the trackball color.  
**Highlights** | Use this to control the highlights.Use the trackball to select the color URP should shift the hue of the highlights to.Use the slider to offset the color lightness of the trackball color.  
### Graph view
This graph shows the overall contribution of the **Shadows** (blue), **Midtones** (green), and **Highlights** (yellow). This is useful to visualize the transitions between the tonal regions.
### Shadow Limits
**Property** | **Description**  
---|---  
**Start** | Set the start point of the transition between the shadows and the midtones of the render.  
**End** | Set the end point of the transition between the shadows and the midtones of the render.  
### Highlight Limits
**Property** | **Description**  
---|---  
**Start** | Set the start point of the transition between the midtones and the highlights of the render.  
**End** | Set the end point of the transition between the midtones and the highlights of the render.  
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/shared/lens-flare/post-processing-screen-space-lens-flare.html)
Add screen space lens flares in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/Post-Processing-Split-Toning.html)
Split Toning Volume Override reference for URP
