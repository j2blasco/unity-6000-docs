* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/urp/Post-Processing-Motion-Blur.html

  * [Rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/rendering-and-post-processing.html)
  * [Post-processing and full-screen effects](https://docs.unity3d.com/6000.0/Documentation/Manual/post-processing-and-full-screen-effects.html)
  * [Post-processing and full-screen effects in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/post-processing-and-full-screen-effects-urp.html)
  * [Post-processing in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/post-processing-in-urp.html)
  * [Post-processing Volume Overrides reference for URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/EffectList.html)
  * Motion Blur Volume Override reference for URP


[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/Post-Processing-Lift-Gamma-Gain.html)
Lift Gamma Gain Volume Override reference for URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/Post-Processing-Panini-Projection.html)
Panini Projection Volume Override reference for URP
# Motion Blur Volume Override reference for URP
![Scene with Motion Blur effect turned off.](https://docs.unity3d.com/6000.0/Documentation/uploads/urp/post-proc/motion-blur-off.png) Scene with Motion Blur effect turned off. ![Scene with Motion Blur effect turned on.](https://docs.unity3d.com/6000.0/Documentation/uploads/urp/post-proc/motion-blur.png) Scene with Motion Blur effect turned on.
The Motion Blur effect simulates the blur that occurs in an image when a real-world **camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera) films objects moving faster than the camera’s exposure time. This is usually due to rapidly moving objects, or a long exposure time.
Universal **Render Pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Renderpipeline) (URP) only blurs camera motions.
## Properties
**Property** | **Description**  
---|---  
**Mode** | Select the motion blur technique.  
Options:
  * **Camera Only** : use only the motion of the camera to blur the objects. This technique does not use the motion vectors. This technique has better performance than **Camera and Objects**.
  * **Camera and Objects** : use the motion of both the camera and the GameObjects. GameObject motion vectors overwrite the camera motion vectors.

  
**Quality** | Set the quality of the effect. Lower presets give better performance, but at a lower visual quality and a higher risk of visual artifacts.  
**Intensity** | Set the strength of the motion blur filter to a value from 0 to 1. Higher values give a stronger blur effect, but can cause lower performance, depending on the **Clamp** parameter.  
**Clamp** | Set the maximum length that the velocity resulting from Camera rotation can have. This limits the blur at high velocity, to avoid excessive performance costs. The value is measured as a fraction of the screen’s full resolution. The value range is 0 to 0.2. A lower value uses less resources and results in better performance.  
  
The default value is 0.05.  
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/Post-Processing-Lift-Gamma-Gain.html)
Lift Gamma Gain Volume Override reference for URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/Post-Processing-Panini-Projection.html)
Panini Projection Volume Override reference for URP
