* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/urp/customizing-urp.html

  * [Rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/rendering-and-post-processing.html)
  * [Render pipelines](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)
  * [Using the Universal Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/universal-render-pipeline.html)
  * Custom rendering and post-processing in URP


[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/anti-aliasing.html)
Add anti-aliasing in the Universal Render Pipeline
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/renderer-features/intro-to-scriptable-render-passes.html)
Introduction to Scriptable Render Passes in URP
# Custom rendering and post-processing in URP
Customize and extend the rendering process in the Universal **Render Pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Renderpipeline) (URP). Create a custom render pass in a C# script and inject it into the URP frame rendering loop.
Page | Description  
---|---  
[Introduction to Scriptable Render Passes](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/renderer-features/intro-to-scriptable-render-passes.html) | Learn about using Scriptable Render Passes to alter how Unity renders a **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) or the objects within a scene.  
[Adding pre-built effects with Renderer Features in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/urp-renderer-feature-landing.html) | Resources for adding pre-built render passes to URP, and configuring their behaviour.  
[Custom render pass workflow in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/renderer-features/custom-rendering-pass-workflow-in-urp.html) | Add and inject a custom render pass.  
[Blit](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/customize/blit-overview.html)A shorthand term for “bit block transfer”. A blit operation is the process of transferring blocks of data from one place in memory to another.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#blit) | Understand the different ways to perform a blit operation in URP and best practices to follow when writing custom render passes.  
[Render graph system](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/render-graph.html) | Resources and approaches for using the `RenderGraph` APIs to create a Scriptable Render Pass.  
[Adding a Scriptable Render Pass to the frame rendering loop](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/inject-a-render-pass.html) | Resources and techniques for injecting a custom render pass via a Scriptable Renderer Feature, or the `RenderPipelineManager` API.  
[Modify URP source code](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/customize/modify-urp-source-code.html) | Modify URP source code to implement advanced customizations.  
[Compatibility Mode](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/compatibility-mode.html) | Write a Scriptable Render Pass if you enable **Compatibility Mode (Render Graph Disabled)** in URP graphics settings. Unity no longer develops or improves this **rendering path** The technique that a render pipeline uses to render graphics. Choosing a different rendering path affects how lighting and shading are calculated. Some rendering paths are more suited to different platforms and hardware than others. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/RenderingPaths.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#RenderingPath).  
## Additional resources
  * [Rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/rendering-in-universalrp.html)
  * [Render pipeline concepts](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/urp-concepts.html)
  * [Pre-built effects (Renderer Features)](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/urp-renderer-feature.html)
  * [How to create a custom post-processing effect](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/post-processing/post-processing-custom-effect-low-code.html)
  * [Execute rendering commands in a custom render pipeline](https://docs.unity3d.com/Packages/com.unity.render-pipelines.core@17.0/manual/srp-using-scriptable-render-context.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/anti-aliasing.html)
Add anti-aliasing in the Universal Render Pipeline
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/renderer-features/intro-to-scriptable-render-passes.html)
Introduction to Scriptable Render Passes in URP
