* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/urp/depth-of-field-volume-override-reference.html

  * [Rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/rendering-and-post-processing.html)
  * [Post-processing and full-screen effects](https://docs.unity3d.com/6000.0/Documentation/Manual/post-processing-and-full-screen-effects.html)
  * [Post-processing and full-screen effects in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/post-processing-and-full-screen-effects-urp.html)
  * [Post-processing in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/post-processing-in-urp.html)
  * [Post-processing Volume Overrides reference for URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/EffectList.html)
  * [Depth of Field in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/depth-of-field-urp.html)
  * Depth of Field Volume Override reference for URP


[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/depth-of-field-volume-override.html)
Depth of Field Volume Override in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/Post-Processing-Film-Grain.html)
Film Grain Volume Override reference for URP
# Depth of Field Volume Override reference for URP
The **Depth of Field** A post-processing effect that simulates the focus properties of a camera lens. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/PostProcessingOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#DepthofField) Volume Override has multiple propeties that can alter the way Depth of Field appears. These properties vary depending on which Depth of Field mode is selected.
## Properties
**Property** | **Description**  
---|---  
**Mode** | Select the mode that URP uses to set the focus for the depth of field effect:
  * **Off** : Select this option to disable depth of field.
  * **Gaussian** : Select this option to use the faster but more limited depth of field mode.
  * **Bokeh** : Select this option to use the Bokeh-based depth of field mode.

  
### Gaussian Depth of Field
**Property** | **Description**  
---|---  
**Start** | Set the distance from the **Camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera) at which the far field starts blurring.  
**End** | Set the distance from the Camera at which the far field blur reaches its maximum blur radius.  
**Max Radius** | Set the maximum radius the far blur can reach. The default value is 1.   
**Note** : Values above 1 can cause visual under-sampling artifacts to appear in your scene. If your blur effects are not smooth or appear to have static noise in them, try decreasing the value back to 1 or lower.  
**High Quality Sampling** | Use higher quality sampling to reduce flickering and improve the overall blur smoothness. This can cause some performance cost.  
### Bokeh Depth of Field
The **Bokeh** Depth of Field mode closely imitates the effect of a real-life camera. For this reason, the settings are based on real-life camera settings, and offer a number of properties to adjust the diaphragm blades on the Camera. For an introduction to diaphragm blades and how they affect the visual quality of your Camera output, refer to Improve Photography’s guide [Aperture Blades: How many is best?](https://improvephotography.com/29529/aperture-blades-many-best/).
**Property** | **Description**  
---|---  
**Focus Distance** | Set the distance from the Camera to the focus point.  
**Focal Length** | Set the distance, in millimeters, between the Camera sensor and the Camera lens. The larger the value is, the shallower the depth of field.  
**Aperture** | Set the ratio of aperture (known as f-stop or f-number). The smaller the value is, the shallower the depth of field is.  
**Blade Count** | Use the slider to set the number of diaphragm blades the Camera uses to form the aperture. The more blades you use, the rounder the bokeh appears.  
**Blade Curvature** | Use the slider to set the curvature of diaphragm blades the Camera uses to form the aperture. The smaller the value is, the more visible aperture blades are. A value of 1 makes the bokeh perfectly circular.*  
**Blade Rotation** | Use the slider to set the rotation of diaphragm blades in degrees.  
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/depth-of-field-volume-override.html)
Depth of Field Volume Override in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/Post-Processing-Film-Grain.html)
Film Grain Volume Override reference for URP
