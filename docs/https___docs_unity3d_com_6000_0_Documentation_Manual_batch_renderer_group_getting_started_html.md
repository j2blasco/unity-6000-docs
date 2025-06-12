* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/batch-renderer-group-getting-started.html

  * [Rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/rendering-and-post-processing.html)
  * [Graphics performance and profiling](https://docs.unity3d.com/6000.0/Documentation/Manual/graphics-performance-profiling.html)
  * [Graphics performance and profiling in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/graphics-performance-and-profiling-in-urp.html)
  * [Optimizing draw calls in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/reduce-draw-calls-landing-urp.html)
  * [BatchRendererGroup API in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/batch-renderer-group.html)
  * Set up your project for the BatchRendererGroup API in URP


[](https://docs.unity3d.com/6000.0/Documentation/Manual/batch-renderer-group-how.html)
Introduction to the BatchRendererGroup API in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/batch-renderer-group-creating-a-renderer.html)
Creating a renderer with the BatchRendererGroup API in URP
# Set up your project for the BatchRendererGroup API in URP
Before you use BRG, your project must support it. BRG requires your project to:
  * Use the SRP Batcher. To enable the SRP Batcher, see [Using the SRP Batcher](https://docs.unity3d.com/6000.0/Documentation/Manual/SRPBatcher-Enable.html).
  * Keep BRG [shader variants](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-variants.html)A verion of a shader program that Unity generates according to a specific combination of shader keywords and their status. A Shader object can contain multiple shader variants. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-variants.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shadervariant). To do this, select **Edit** > **Project Settings** > **Graphics** , and set **BatchRendererGroup variants** to **Keep all**.
  * If your project uses URP, it’s best practice to disable the **Strip Unused Variants** [Global Setting](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/urp-global-settings.html). This helps to avoid problems with Unity stripping necessary DOTS Instancing variants. For more information, see [DOTS Instancing shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/dots-instancing-shaders.html). To find this setting, select **Edit** > **Project Settings** > **URP Global Settings**.
  * Allow [unsafe code](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/unsafe-code). To do this, enable the **Allow ‘unsafe’ Code** [Player Setting](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PlayerSettings.html).


**Note:** The BatchRendererGroup uses [DOTS Instancing shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/dots-instancing-shaders.html), but it doesn’t require any DOTS packages. The name reflects the new data-oriented way to load instance data, and also helps with backward compatibility with existing Hybrid Renderer compatible **shaders** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader).
For information on how to use BRG to create a basic renderer, see [Creating a renderer with BatchRendererGroup](https://docs.unity3d.com/6000.0/Documentation/Manual/batch-renderer-group-creating-a-renderer.html).
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/batch-renderer-group-how.html)
Introduction to the BatchRendererGroup API in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/batch-renderer-group-creating-a-renderer.html)
Creating a renderer with the BatchRendererGroup API in URP
