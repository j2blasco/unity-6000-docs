* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/dots-instancing-shaders-support.html

  * [Rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/rendering-and-post-processing.html)
  * [Graphics performance and profiling](https://docs.unity3d.com/6000.0/Documentation/Manual/graphics-performance-profiling.html)
  * [Graphics performance and profiling in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/graphics-performance-and-profiling-in-urp.html)
  * [Optimizing draw calls in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/reduce-draw-calls-landing-urp.html)
  * [BatchRendererGroup API in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/batch-renderer-group.html)
  * [Writing custom shaders for the BatchRendererGroup API](https://docs.unity3d.com/6000.0/Documentation/Manual/batch-renderer-group-writing-shaders.html)
  * Support DOTS Instancing in a a custom shader in URP


[](https://docs.unity3d.com/6000.0/Documentation/Manual/dots-instancing-shaders.html)
DOTS Instancing shaders in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/dots-instancing-shaders-declare.html)
Declare DOTS Instancing properties in a custom shader in URP
# Support DOTS Instancing in a a custom shader in URP
To support DOTS Instancing, a **shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) needs to do the following:
  * Use shader model 4.5 or newer. Specify `#pragma target 4.5` or higher.
  * Support the `DOTS_INSTANCING_ON` keyword. Declare this with `#pragma multi_compile _ DOTS_INSTANCING_ON`.
  * Declare at least one block of DOTS Instanced properties each of which has least one property. For more information, see [Declaring DOTS Instanced properties](https://docs.unity3d.com/6000.0/Documentation/Manual/dots-instancing-shaders-unity-dots-instanced-prop.html).


**Note** : Shader Graphs and shaders that Unity provides in URP and HDRP support DOTS Instancing.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/dots-instancing-shaders.html)
DOTS Instancing shaders in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/dots-instancing-shaders-declare.html)
Declare DOTS Instancing properties in a custom shader in URP
