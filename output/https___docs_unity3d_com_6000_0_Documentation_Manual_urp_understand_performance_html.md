* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/urp/understand-performance.html

  * [Rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/rendering-and-post-processing.html)
  * [Graphics performance and profiling](https://docs.unity3d.com/6000.0/Documentation/Manual/graphics-performance-profiling.html)
  * [Graphics performance and profiling in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/graphics-performance-and-profiling-in-urp.html)
  * Understand performance in URP


[](https://docs.unity3d.com/6000.0/Documentation/Manual/graphics-performance-and-profiling-in-urp.html)
Graphics performance and profiling in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/analyze-your-project.html)
Analyze your project in URP
# Understand performance in URP
The performance of your project depends on the Universal **Render Pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Renderpipeline) (URP) features you use or enable, what your **scenes** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) contain, and which platforms you target. 
You can use the [Unity Profiler](https://docs.unity3d.com/Manual/Profiler.html) or a GPU **profiler** A window that helps you to optimize your game. It shows how much time is spent in the various areas of your game. For example, it can report the percentage of time spent rendering, animating, or in your game logic. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Profiler.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Profiler) such as [RenderDoc](https://docs.unity3d.com/Manual/RenderDocIntegration.html) or [Xcode](https://docs.unity3d.com/Manual/XcodeFrameDebuggerIntegration.html) to check how much URP uses memory, the CPU and the GPU in your project. You can then use the information to enable or disable the features and settings that have the largest performance impact.
URP usually performs better if you change settings that reduce the following:
  * How much URP uses the CPU. For example, you can disable URP updating volumes every frame.
  * How much memory URP uses to store textures. For example, you can disable High Dynamic Range (HDR) if you don’t need it, to reduce the size of the color buffer. 
  * How many **render textures** A special type of Texture that is created and updated at runtime. To use them, first create a new Render Texture and designate one of your Cameras to render into it. Then you can use the Render Texture in a Material just like a regular Texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-RenderTexture.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#RenderTexture) URP copies to and from memory, which has a large impact on mobile platforms. For example, you can disable URP creating a depth texture if you don’t need it.
  * The number of passes in the render pipeline. For example, you can disable the opaque texture if you don’t need it, or disable additional lights casting shadows.
  * The number of draw calls URP sends to the GPU. For example, you can enable the SRP Batcher.
  * The number of **pixels** The smallest unit in a computer image. Pixel size depends on your screen resolution. Pixel lighting is calculated at every screen pixel. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/ShadowPerformance.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#pixel) URP renders to the screen, which has a big effect on mobile platforms where the GPU is less powerful. For example, you can reduce the render scale.


Refer to the following for more information about which settings to disable or change to improve performance:
  * [Configure for better performance](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/configure-for-better-performance.html)
  * [Optimize for better performance](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/optimize-for-better-performance.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/graphics-performance-and-profiling-in-urp.html)
Graphics performance and profiling in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/analyze-your-project.html)
Analyze your project in URP
