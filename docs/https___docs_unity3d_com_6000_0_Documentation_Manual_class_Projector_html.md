* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/class-Projector.html

  * [Visual effects](https://docs.unity3d.com/6000.0/Documentation/Manual/visual-effects.html)
  * [Decals and projectors](https://docs.unity3d.com/6000.0/Documentation/Manual/visual-effects-decals.html)
  * [Decals in the Built-In Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/decals-birp.html)
  * Projector component reference for the Built-In Render Pipeline


[](https://docs.unity3d.com/6000.0/Documentation/Manual/prepare-materials-projection.html)
Prepare materials for projection in the Built-In Render Pipeline
[](https://docs.unity3d.com/6000.0/Documentation/Manual/visual-effects-lens-flares.html)
Lens flares
# Projector component reference for the Built-In Render Pipeline
[Switch to Scripting](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Projector.html "Go to Projector page in the Scripting Reference")
Explore the properties in the Projector component to configure a material’s projection onto a surface.
**_Property:_** | **_Function:_**  
---|---  
**Near Clip Plane** | Objects in front of the near clip plane will not be projected upon.  
**Far Clip Plane** | Objects beyond this distance will not be projected upon.  
**Field Of View** | The field of view in degrees. This is only used if the Projector is not Orthographic.  
**Aspect Ratio** The relationship of an image’s proportional dimensions, such as its width and height.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#AspectRatio) | This allows you to tune the height and width of the Projector.  
**Orthographic** | If enabled, the Projector will be Orthographic instead of perspective.  
**Orthographic Size** | The Orthographic size of the Projection. This is only used if Orthographic is enabled.  
**Material** An asset that defines how a surface should be rendered. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Material.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Material) | The Material that will be projected.  
**Ignore Layers** | Objects in Layers that you specify here will not be projected upon. The default value is None.  
Projector
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/prepare-materials-projection.html)
Prepare materials for projection in the Built-In Render Pipeline
[](https://docs.unity3d.com/6000.0/Documentation/Manual/visual-effects-lens-flares.html)
Lens flares
