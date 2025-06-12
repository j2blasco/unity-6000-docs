* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/urp/Post-Processing-Lens-Distortion.html

  * [Rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/rendering-and-post-processing.html)
  * [Post-processing and full-screen effects](https://docs.unity3d.com/6000.0/Documentation/Manual/post-processing-and-full-screen-effects.html)
  * [Post-processing and full-screen effects in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/post-processing-and-full-screen-effects-urp.html)
  * [Post-processing in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/post-processing-in-urp.html)
  * [Post-processing Volume Overrides reference for URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/EffectList.html)
  * Lens Distortion Volume Override reference for URP


[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/Post-Processing-Film-Grain.html)
Film Grain Volume Override reference for URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/Post-Processing-Lift-Gamma-Gain.html)
Lift Gamma Gain Volume Override reference for URP
# Lens Distortion Volume Override reference for URP
![Scene with Lens Distortion effect turned off.](https://docs.unity3d.com/6000.0/Documentation/uploads/urp/post-proc/lens-distortion-off.png) Scene with Lens Distortion effect turned off. ![Scene with Lens Distortion effect turned on.](https://docs.unity3d.com/6000.0/Documentation/uploads/urp/post-proc/lens-distortion.png) Scene with Lens Distortion effect turned on.
The **Lens Distortion** effect distorts the final rendered picture to simulate the shape of a real-world **camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera) lens.
## Properties
**Property** | **Description**  
---|---  
**Intensity** | Use the slider to set the overall strength of the **distortion effect** An audio effect that modifies the sound by squashing and clipping the waveform to produce a rough, harsh result. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioDistortionFilter.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#DistortionEffect).  
**X Multiplier** | Use the slider to set the distortion intensity on the x-axis. This value acts as a multiplier so you can set this value to 0 to disable distortion on this axis,  
**Y Multiplier** | Use the slider to set the distortion intensity on the y-axis. This value acts as a multiplier so you can set this value to 0 to disable distortion on this axis,  
**Center** | Set the center point of the distortion effect on the screen.  
**Scale** | Use the slider to set the value for global screen scaling. This zooms the render to hide the borders of the screen. When you use a high distortion, **pixels** The smallest unit in a computer image. Pixel size depends on your screen resolution. Pixel lighting is calculated at every screen pixel. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/ShadowPerformance.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#pixel) on the borders of the screen can break because they rely on information from pixels outside the screen boundaries that don’t exist. This property is useful for hiding these broken pixels around the screen border.  
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/Post-Processing-Film-Grain.html)
Film Grain Volume Override reference for URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/Post-Processing-Lift-Gamma-Gain.html)
Lift Gamma Gain Volume Override reference for URP
