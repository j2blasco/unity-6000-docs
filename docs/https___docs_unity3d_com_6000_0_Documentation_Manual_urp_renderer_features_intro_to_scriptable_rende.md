* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/urp/renderer-features/intro-to-scriptable-render-passes.html

  * [Rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/rendering-and-post-processing.html)
  * [Render pipelines](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)
  * [Using the Universal Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/universal-render-pipeline.html)
  * [Custom rendering and post-processing in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/customizing-urp.html)
  * Introduction to Scriptable Render Passes in URP


[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/customizing-urp.html)
Custom rendering and post-processing in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/urp-renderer-feature-landing.html)
Adding pre-built effects via Renderer Features in URP
# Introduction to Scriptable Render Passes in URP
Scriptable Render Passes are a way to alter how Unity renders a **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) or the objects within a scene. They allow you to fine tune how Unity renders each scene in your project on a scene-by-scene basis.
You inject a Scriptable Render Pass into the **render pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Renderpipeline) to achieve a custom visual effect. For more information, refer to [Adding a Scriptable Render Pass to the frame rendering loop](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/inject-a-render-pass.html).
A Scriptable Render Pass lets you to do the following:
  * Change the properties of materials in your scene.
  * Change the order that Unity renders **GameObjects** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) in.
  * Lets Unity read **camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera) buffers and use them in **shaders** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader).


For example, you can use a Scriptable Render Pass to blur a camera’s view when showing the in-game menu.
Unity injects Scriptable Render Passes at certain points during the URP render loop. These points are called injection points. You can change the injection point Unity inserts your pass at to control how the Scriptable Render Pass affects the appearance of your scene. For more information on injection points, refer to [Injection Points](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/customize/custom-pass-injection-points.html).
## Additional resources
  * [Adding pre-built effects with Renderer Features in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/urp-renderer-feature-landing.html)
  * [How to create a Custom Renderer Feature](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/renderer-features/create-custom-renderer-feature.html)
  * [Scriptable Renderer Feature Reference](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/renderer-features/scriptable-renderer-features/scriptable-renderer-feature-reference.html)
  * [How to inject a Custom Render Pass via scripting](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/customize/custom-pass-injection-points.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/customizing-urp.html)
Custom rendering and post-processing in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/urp-renderer-feature-landing.html)
Adding pre-built effects via Renderer Features in URP
