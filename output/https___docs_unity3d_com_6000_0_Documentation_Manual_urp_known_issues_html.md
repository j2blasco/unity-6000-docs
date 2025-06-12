* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/urp/known-issues.html

  * [Rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/rendering-and-post-processing.html)
  * [Render pipelines](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)
  * [Using the Universal Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/universal-render-pipeline.html)
  * [Get started with URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/introduction-landing.html)
  * [Installing and upgrading URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/InstallingAndConfiguringURP.html)
  * Known issues in URP


[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/upgrade-lwrp-to-urp.html)
Upgrade from the Lightweight Render Pipeline to the Universal Render Pipeline
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/configure-for-better-performance.html)
Configure for better performance in URP
# Known issues in URP
This page contains information on known issues you may encounter when using URP.
## Long build times when using the Forward+ Rendering Path
Due to the wide variety of use cases, target platforms, renderers, and features used in projects, certain URP configurations can result in a large number of **shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) variants. That can lead to long compilation times.
Long shader compilation time affects both player build time and the time for a **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) to render in the Editor.
The per-camera visible light limit value affects the compilation time for each **Lit** and **Complex Lit** shader variant. In the Forward+ **Rendering Path** The technique that a render pipeline uses to render graphics. Choosing a different rendering path affects how lighting and shading are calculated. Some rendering paths are more suited to different platforms and hardware than others. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/RenderingPaths.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#RenderingPath), on desktop platforms, that limit is 256.
Refer to the following page to learn how to reduce the build time in the Forward+ Rendering Path by reducing the maximum number of visible lights:
  * [Reduce build time in Forward+ Rendering Path](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/rendering/forward-plus-rendering-path-limitations.html)


## When importing the URP package samples, Unity does not set the necessary URP asset in Quality > Render Pipeline Asset
When importing the URP package samples, Unity does not set the necessary URP asset in **Quality** > **Render Pipeline Asset** , and certain sample rendering effects do not work.
To fix this issue:
In **Project Settings** > **Quality** > **Render Pipeline Asset** , select `SamplesPipelineAsset`.
![In Project Settings > Quality > Render Pipeline Asset, select SamplesPipelineAsset](https://docs.unity3d.com/6000.0/Documentation/uploads/urp/known-issues/urp-12-package-samples.png) In Project Settings > Quality > Render Pipeline Asset, select SamplesPipelineAsset
## Renaming a URP Renderer asset to a name matching one of the Renderer Feature names causes erroneous behavior
If a URP Renderer asset has any Renderer Features assigned, renaming the Renderer asset to a name matching one of the Renderer Feature names causes erroneous behavior: the URP Renderer and the Renderer Feature switch places.
The following scenario shows how the error occurs:
  * Let’s assume that the URP Renderer in your project is called `UniversalRenderer`.
  * The Renderer has a Renderer Feature called `NewRenderObjects` assigned.
![UniversalRenderer with Renderer Feature assigned to it.](https://docs.unity3d.com/6000.0/Documentation/uploads/urp/known-issues/urp-10-renaming-renderer.png) UniversalRenderer with Renderer Feature assigned to it.
  * Renaming `UniversalRenderer` to `NewRenderObjects` causes erroneous behavior:  
The Renderer switches places with the Renderer Feature and does not behave correctly.


To avoid the issue, do not give the URP Renderer asset the same name as the Renderer Feature asset.
To find updates on this issue, refer to the [Unity Issue Tracker](https://issuetracker.unity3d.com/issues/parent-and-child-nested-scriptable-object-assets-switch-places-when-parent-scriptable-object-asset-is-renamed).
## Warning about _AdditionalLights property when upgrading the URP package
In certain cases, you might receive the following warning when upgrading the URP package to a newer version:
```
Property (_AdditionalLights<...>) exceeds previous array size (256 vs 16). Cap to previous size.

```

This warning does not cause issues with the project, the warning disappears if you restart the Editor.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/upgrade-lwrp-to-urp.html)
Upgrade from the Lightweight Render Pipeline to the Universal Render Pipeline
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/configure-for-better-performance.html)
Configure for better performance in URP
