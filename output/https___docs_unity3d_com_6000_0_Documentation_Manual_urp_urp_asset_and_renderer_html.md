* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/urp/urp-asset-and-renderer.html

  * [Rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/rendering-and-post-processing.html)
  * [Render pipelines](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)
  * [Using the Universal Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/universal-render-pipeline.html)
  * [Graphics quality settings in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/urp-quality-settings-landing.html)
  * Universal Render Pipeline asset


[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/urp-quality-settings-landing.html)
Graphics quality settings in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/urp-asset-additional-settings.html)
Display advanced properties in a URP Asset
# Universal Render Pipeline asset
Any Unity project that uses the Universal **Render Pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Renderpipeline) (URP) must have a URP Asset to configure the settings. When you create a project using the URP template, Unity creates the URP Assets in the **Settings** project folder and assigns them in **Project Settings** A broad collection of settings which allow you to configure how Physics, Audio, Networking, Graphics, Input and many other areas of your project behave. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/comp-ManagerGroup.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#ProjectSettings). If you are migrating an existing project to URP, you need to [create a URP Asset and assign the asset in the Graphics settings](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/InstallURPIntoAProject.html).
The URP Asset controls several graphical features and quality settings for the Universal Render Pipeline. It is a scriptable object that inherits from ‘RenderPipelineAsset’. When you assign the asset in the Graphics settings, Unity switches from the built-in render pipeline to the URP. You can then adjust the corresponding settings directly in the URP, instead of looking for them elsewhere.
You can have multiple URP assets and switch between them. For example, you can have one with Shadows on and one with Shadows off. If you switch between the assets to understand the effects, you don’t have to manually toggle the corresponding settings for shadows every time. You cannot, however, switch between HDRP/SRP and URP assets, as the render pipelines are incompatible.
## Additional resources
  * [URP Asset reference](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/universalrp-asset.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/urp-quality-settings-landing.html)
Graphics quality settings in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/urp-asset-additional-settings.html)
Display advanced properties in a URP Asset
