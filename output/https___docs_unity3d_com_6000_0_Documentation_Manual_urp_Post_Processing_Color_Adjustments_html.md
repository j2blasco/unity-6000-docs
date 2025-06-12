* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/urp/Post-Processing-Color-Adjustments.html

  * [Rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/rendering-and-post-processing.html)
  * [Post-processing and full-screen effects](https://docs.unity3d.com/6000.0/Documentation/Manual/post-processing-and-full-screen-effects.html)
  * [Post-processing and full-screen effects in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/post-processing-and-full-screen-effects-urp.html)
  * [Post-processing in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/post-processing-in-urp.html)
  * [Post-processing Volume Overrides reference for URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/EffectList.html)
  * Color Adjustments Volume Override reference for URP


[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/post-processing-chromatic-aberration.html)
Chromatic Aberration Volume Override reference for URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/Post-Processing-Color-Curves.html)
Color Curves Volume Override reference for URP
# Color Adjustments Volume Override reference for URP
Use this effect to tweak the overall tone, brightness, and contrast of the final rendered image.
![Scene without Color Adjustments effect.](https://docs.unity3d.com/6000.0/Documentation/uploads/urp/post-proc/color-adjustments-off.png) Scene without Color Adjustments effect. ![Scene with Color Adjustments effect.](https://docs.unity3d.com/6000.0/Documentation/uploads/urp/post-proc/color-adjustments.png) Scene with Color Adjustments effect.
## Properties
**Property** | **Description**  
---|---  
**Post Exposure** | Adjusts the overall exposure of the scene in EV (not EV100). URP applies this after the HDR effect and before tonemapping, which means that it does not affect previous effects in the chain.  
**Contrast** | Use the slider to expand or shrink the overall range of tonal values. Larger positive values expand the tonal range and lower negative values shrink the tonal range.  
**Color Filter** | Use the color picker to select which color the Color Adjustment effect should use to multiply the render and tint the result.  
**Hue Shift** | Use the slider to shift the hue of all colors.  
**Saturation** | Use the slider to push the intensity of all colors.  
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/post-processing-chromatic-aberration.html)
Chromatic Aberration Volume Override reference for URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/Post-Processing-Color-Curves.html)
Color Curves Volume Override reference for URP
