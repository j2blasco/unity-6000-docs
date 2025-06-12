* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/shader-prewarm.html

  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-and-shaders.html)
  * [Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)
  * [Troubleshooting shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-troubleshooting.html)
  * [Fixing hitches or stalls](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-reduce-stalling.html)
  * Prewarm shaders


[](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-loading.html)
Shader loading
[](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-variant-collections.html)
Create a shader variant collection
# Prewarm shaders
When Unity uses a **shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) variant for the first time in your built application, the **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) might stutter. This is because Unity and the graphics driver need to compile the shader variant, and create a pipeline state object (PSO) with the compiled shader code and its related GPU state.
To reduce stuttering, compile shaders and create PSOs before they’re first needed, so that the graphics driver caches them to disk. This is called warming up, prewarming, or precooking. You usually warm up during a loading screen, either when your application starts or while loading a scene. 
**Note** : Some of the APIs are experimental and not ready for production use. The APIs and documentation might be changed or removed in the future.
## Warm up shaders with DirectX 12, Metal or Vulkan
To warm up shaders on DirectX 12, Metal or Vulkan, use the experimental `GraphicsStateCollection` API. This API collects the specific GPU states your project uses at runtime, which modern graphics APIs need to create and cache accurate PSOs.
Follow these steps:
  1. In a test run of your built application, use the `GraphicsStateCollection.BeginTrace` and `GraphicsStateCollection.EndTrace` methods to record the shader variants and GPU states your application uses.
  2. To save the recorded information as a `.graphicsState` file, use the `GraphicsStateCollection.SendToEditor` API.
  3. In your final project, load the `.graphicsstate` file, then use the `WarmUp` or `WarmUpProgressively` APIs to warm up the shader variants. Both APIs return `JobHandle` objects you can use to warm up the shader variants asynchronously.


You should create a different `.graphicsstate` file for each graphics API you use.
For more information, refer to [`GraphicsStateCollection`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.Rendering.GraphicsStateCollection.html).
## Warm up shaders with other graphics APIs
Warm up in the following ways:
  * To warm up a **Shader object** An instance of the Shader class, a Shader object is container for shader programs and GPU instructions, and information that tells Unity how to use them. Use them with materials to determine the appearance of your scene. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-objects.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shaderobject), use the [Experimental.Rendering.ShaderWarmup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.Rendering.ShaderWarmup.html) API.
  * To warm up all variants of all Shader objects currently in memory, use the [Shader.WarmupAllShaders](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.WarmupAllShaders.html) API.


To warm up a shader variant collection, do any of the following:
  * Use the [Experimental.Rendering.ShaderWarmup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.Rendering.ShaderWarmup.html) API.
  * Use the [ShaderVariantCollection.WarmUp](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderVariantCollection.WarmUp.html) API.
  * Add the shader variant collection to the [Preloaded shaders section of the Graphics Settings window](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GraphicsSettings.html#shader-loading). Unity then uses the `ShaderVariantCollection.WarmUp` to warm up the shader variants when your built application starts.


## Check if shaders are warmed up
To check when Unity and the graphics driver compile shaders and create PSOs, search for the following **profiler markers** Placed in code to describe a CPU or GPU event that is then displayed in the Unity Profiler window. Added to Unity code by default, or you can use [ProfilerMarker API](https://docs.unity3d.com/Packages/com.unity.profiling.core@latest/index.html?subfolder=/manual/profilermarker-guide.html) to add your own custom markers. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-markers.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Profilermarker) in the [Profiler](https://docs.unity3d.com/6000.0/Documentation/Manual/Profiler.html)A window that helps you to optimize your game. It shows how much time is spent in the various areas of your game. For example, it can report the percentage of time spent rendering, animating, or in your game logic. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Profiler.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Profiler):
  * `Shader.CreateGPUProgram` for Unity creating a GPU-specific version of a shader variant.
  * `CreateGraphicsGraphicsPipelineImpl` for Unity creating a PSO.


## Additional resources
  * [How Unity loads and uses shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-loading.html)
  * [Optimizing shader runtime performance](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-ShaderPerformance.html)
  * [GraphicsStateCollection Tracing and Warmup in Unity 6](https://forum.unity.com/threads/graphicsstatecollection-tracing-and-warmup-in-unity-6.1606386/) on the Unity Forums.


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-loading.html)
Shader loading
[](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-variant-collections.html)
Create a shader variant collection
