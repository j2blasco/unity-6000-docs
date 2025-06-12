* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/urp/depth-of-field-volume-override.html

  * [Rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/rendering-and-post-processing.html)
  * [Post-processing and full-screen effects](https://docs.unity3d.com/6000.0/Documentation/Manual/post-processing-and-full-screen-effects.html)
  * [Post-processing and full-screen effects in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/post-processing-and-full-screen-effects-urp.html)
  * [Post-processing in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/post-processing-in-urp.html)
  * [Post-processing Volume Overrides reference for URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/EffectList.html)
  * [Depth of Field in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/depth-of-field-urp.html)
  * Depth of Field Volume Override in URP


[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/depth-of-field-urp.html)
Depth of Field in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/depth-of-field-volume-override-reference.html)
Depth of Field Volume Override reference for URP
# Depth of Field Volume Override in URP
The **Depth Of Field** A post-processing effect that simulates the focus properties of a camera lens. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/PostProcessingOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#DepthofField) component applies a depth of field effect, which simulates the focus properties of a **camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera) lens. In real life, a camera can only focus sharply on an object at a specific distance. Objects nearer or farther from the camera are out of focus. The blurring gives a visual cue about an object’s distance, and introduces “bokeh”, which refers to visual artifacts that appear around bright areas of the image as they fall out of focus. To read more about bokeh, refer to the [Wikipedia article on Bokeh](https://en.wikipedia.org/wiki/Bokeh).
The Universal **Render Pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Renderpipeline) (URP) has two depth of field modes:
  * **Gaussian** : this mode approximates camera-like effects, but doesn’t imitate them completely. It has a limited blur radius and only does far-field blurring. This mode is the fastest, and is the best mode for lower-end platforms.  
![Gaussian Depth Of Field](https://docs.unity3d.com/6000.0/Documentation/uploads/urp/post-proc/dof-gaussian.png)
  * **Bokeh** : a slower but higher quality mode that closely imitates the effects of a real-life camera. It can do both near & far-field blurring, and generates bokeh on areas with high luminosity intensity, also known as hot spots.  
![Gaussian Depth Of Field](https://docs.unity3d.com/6000.0/Documentation/uploads/urp/post-proc/dof-bokeh.png)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/depth-of-field-urp.html)
Depth of Field in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/depth-of-field-volume-override-reference.html)
Depth of Field Volume Override reference for URP
