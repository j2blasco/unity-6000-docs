* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/DynamicResolution-enable-disable.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [Cameras](https://docs.unity3d.com/6000.0/Documentation/Manual/Cameras.html)
  * [Changing resolution scale](https://docs.unity3d.com/6000.0/Documentation/Manual/resolution-scale.html)
  * [Dynamic Resolution](https://docs.unity3d.com/6000.0/Documentation/Manual/DynamicResolution-landing.html)
  * Enable or disable Dynamic Resolution for render targets


[](https://docs.unity3d.com/6000.0/Documentation/Manual/DynamicResolution-control-when-occurs.html)
Control when Dynamic Scaling happens
[](https://docs.unity3d.com/6000.0/Documentation/Manual/OcclusionCulling-landing.html)
Excluding hidden objects with occlusion culling
# Enable or disable Dynamic Resolution for render targets
With **dynamic resolution** A Camera setting that allows you to dynamically scale individual render targets to reduce workload on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/DynamicResolution-landing.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#dynamicresolution), render targets have the [DynamicallyScalable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTextureCreationFlags.DynamicallyScalable.html) flag. You can set this to state whether Unity should scale this **render texture** A special type of Texture that is created and updated at runtime. To use them, first create a new Render Texture and designate one of your Cameras to render into it. Then you can use the Render Texture in a Material just like a regular Texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-RenderTexture.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#RenderTexture) as part of the dynamic resolution process or not. **Cameras** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera) also have the [allowDynamicResolution](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-allowDynamicResolution.html) flag, which you can use to set up dynamic resolution so that there is no need to override the render target if you just want to apply dynamic resolution to a less complex **Scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene).
## MRT buffers
When you enable **Allow Dynamic Resolution** on the Camera, Unity scales all of that Camera’s targets.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/DynamicResolution-control-when-occurs.html)
Control when Dynamic Scaling happens
[](https://docs.unity3d.com/6000.0/Documentation/Manual/OcclusionCulling-landing.html)
Excluding hidden objects with occlusion culling
