* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/graphics-tiers-customize.html

  * [Rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/rendering-and-post-processing.html)
  * [Render pipelines](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)
  * [Using the Built-In Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/built-in-render-pipeline.html)
  * [Graphics quality settings in the Built-In Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/built-in-graphics-quality-settings.html)
  * Configure graphics tiers in the Built-In Render Pipeline


[](https://docs.unity3d.com/6000.0/Documentation/Manual/graphics-tiers.html)
Graphics tiers in the Built-In Render Pipeline
[](https://docs.unity3d.com/6000.0/Documentation/Manual/built-in-rendering-paths.html)
Rendering paths in the Built-In Render Pipeline
# Configure graphics tiers in the Built-In Render Pipeline
## Using graphics tiers with C# scripts
Unity stores the value of the current graphics tier in [Graphics.activeTier](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics-activeTier.html), represented by a [GraphicsTier](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsTier.html) enum. To add custom behavior based on the current graphics tier, you can test against this value.
To override the value of `Graphics.activeTier`, set it directly. Note that you must do this before Unity loads any **shaders** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) that vary based on graphics tier. A good place to set this value is in a pre-loading **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene), before you load your main scene.
## Tier settings
In the Unity Editor, you can configure **tier settings**. Tier settings allow you to enable or disable graphics features for each tier.
Tier settings work by changing `#define` preprocessor directives in Unity’s internal shader code. These changes automatically affect prebuilt shaders for the Built-in **Render Pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Renderpipeline) (such as the [Standard Shader](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-StandardShader.html)), and the internal shader library code for [Surface Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-SurfaceShaders.html)A streamlined way of writing shaders for the Built-in Render Pipeline. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-SurfaceShaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#SurfaceShader). You can also add code to your own hand-coded shaders that changes their behavior based on tier settings. For more information, see [Graphics tiers and shader variants](https://docs.unity3d.com/6000.0/Documentation/Manual/graphics-tiers.html#shader-variants).
The default tier settings are suitable for most use cases. You should only change them if you are experiencing performance issues, or if you want to enable features on lower-end devices that are not enabled by default.
You can configure different tier settings for each graphics tier of a given build target. You can change tier settings in the following ways:
  * Use the [Graphics Settings](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GraphicsSettings.html) window, in the **Tier Settings** section.
  * Use these APIs in an Editor script: 
    * [EditorGraphicsSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.EditorGraphicsSettings.html)
    * [TierSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.TierSettings.html)


You can test tier settings in the Editor. To do this, navigate to **Edit > Graphics Tier** and choose the tier that you want the Unity Editor to use.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/graphics-tiers.html)
Graphics tiers in the Built-In Render Pipeline
[](https://docs.unity3d.com/6000.0/Documentation/Manual/built-in-rendering-paths.html)
Rendering paths in the Built-In Render Pipeline
