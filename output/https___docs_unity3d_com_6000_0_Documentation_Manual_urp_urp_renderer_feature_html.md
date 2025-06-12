* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/urp/urp-renderer-feature.html

  * [Rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/rendering-and-post-processing.html)
  * [Render pipelines](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)
  * [Using the Universal Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/universal-render-pipeline.html)
  * [Custom rendering and post-processing in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/customizing-urp.html)
  * [Adding pre-built effects via Renderer Features in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/urp-renderer-feature-landing.html)
  * Add a Renderer Feature to a URP Renderer


[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/urp-renderer-feature-landing.html)
Adding pre-built effects via Renderer Features in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/renderer-features/how-to-custom-effect-render-objects.html)
Example of creating a custom rendering effect via the Render Objects Renderer Feature in URP
# Add a Renderer Feature to a URP Renderer
URP draws objects in the **DrawOpaqueObjects** and **DrawTransparentObjects** passes. You might need to draw objects at a different point in the frame rendering, or interpret and write rendering data (like depth and stencil) in alternate ways. The Render Objects Renderer Feature lets you do such customizations by letting you draw objects on a certain layer, at a certain time, with specific overrides.
For examples of how to use Renderer Features, refer to the [Renderer Features samples in URP Package Samples](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/package-sample-urp-package-samples.html#renderer-features).
To add a Renderer Feature to a Renderer:
  1. In the **Project** window, select a Renderer.
![Select a Renderer.](https://docs.unity3d.com/6000.0/Documentation/uploads/urp/add-renderer-feature/renderer-feature-select-renderer.png) Select a Renderer.
The **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector) window shows the Renderer properties.
![Inspector window shows the Renderer properties.](https://docs.unity3d.com/6000.0/Documentation/uploads/urp/add-renderer-feature/renderer-feature-inspector-no-rend-features.png) Inspector window shows the Renderer properties.
  2. In the Inspector window, select **Add Renderer Feature**. In the list, select a Renderer Feature.
![Select Add Renderer Feature, then select a Renderer Feature.](https://docs.unity3d.com/6000.0/Documentation/uploads/urp/add-renderer-feature/renderer-feature-select-renderer-feature.png) Select **Add Renderer Feature** , then select a Renderer Feature.
Unity adds the selected Renderer Feature to the Renderer.
![New Renderer Feature added.](https://docs.unity3d.com/6000.0/Documentation/uploads/urp/add-renderer-feature/renderer-feature-created.png) New Renderer Feature added.


Unity shows Renderer Features as child items of the Renderer in the **Project Window** A window that shows the contents of your `Assets` folder (Project tab) [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/ProjectView.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Projectwindow):
![Renderer Feature as child item of the Renderer in the Project Window](https://docs.unity3d.com/6000.0/Documentation/uploads/urp/add-renderer-feature/renderer-feature-project-window.png) Renderer Feature as child item of the Renderer in the Project Window
## Additional resources
  * [Drawing objects with a Render Objects Renderer Feature](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/renderer-features/how-to-custom-effect-render-objects.html)
  * [Decal Renderer Feature](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/renderer-feature-decal-landing.html)
  * [Screen Space Ambient Occlusion (SSAO) Renderer Feature](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/post-processing-ssao.html)
  * [Screen Space Shadows Renderer Feature](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/renderer-feature-screen-space-shadows.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/urp-renderer-feature-landing.html)
Adding pre-built effects via Renderer Features in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/renderer-features/how-to-custom-effect-render-objects.html)
Example of creating a custom rendering effect via the Render Objects Renderer Feature in URP
