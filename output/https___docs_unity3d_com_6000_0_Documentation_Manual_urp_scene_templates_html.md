* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/urp/scene-templates.html

  * [Rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/rendering-and-post-processing.html)
  * [Render pipelines](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)
  * [Using the Universal Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/universal-render-pipeline.html)
  * [Get started with URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/introduction-landing.html)
  * [Installing and upgrading URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/InstallingAndConfiguringURP.html)
  * [Creating a URP project](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/creating-a-urp-project.html)
  * Scene templates in URP


[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/creating-a-new-project-with-urp.html)
Create a new project that uses URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/package-samples.html)
Import a package sample in URP
# Scene templates in URP
You can use [Scene Templates](https://docs.unity3d.com/Manual/scene-templates.html) to quickly create scenes that include pre-configured URP-specific settings and **post-processing** A process that improves product visuals by applying filters and effects before the image appears on screen. You can use post-processing effects to simulate physical camera and film properties, for example Bloom and Depth of Field. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/PostProcessingOverview.html) post processing, postprocessing, postprocess  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#post-processing) effects. For information on how to create a new **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) from a Scene Template, refer to [Creating a new scene from the New Scene dialog](https://docs.unity3d.com/Manual/scenes-working-with.html#creating-a-new-scene-from-the-new-scene-dialog).
![The New Scene dialog displaying Scene Templates.](https://docs.unity3d.com/6000.0/Documentation/uploads/urp/scene-templates.png) The New Scene dialog displaying Scene Templates.
The following Scene Templates are available for URP:
  * **Basic (URP)** : A scene that contains a [Camera](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/camera-component-reference.md)A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera) and a [Light](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/light-component.md). This is the URP equivalent of Unity’s default scene.
  * **Standard (URP)** : A scene that contains a Camera, a Light, and a global [Volume](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/Volumes.md) with various post-processing effects. **Note** : If you create a scene using the Standard (URP) Scene Template, Unity creates a new [Volume Profile](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/Volume-Profile.md) to store the post-processing effects.


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/creating-a-new-project-with-urp.html)
Create a new project that uses URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/package-samples.html)
Import a package sample in URP
