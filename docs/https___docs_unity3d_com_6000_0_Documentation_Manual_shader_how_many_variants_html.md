* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/shader-how-many-variants.html

  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-and-shaders.html)
  * [Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)
  * [Troubleshooting shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-troubleshooting.html)
  * [Reducing the size or number of shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-reducing.html)
  * [Reducing shader variants](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-variants-landing.html)
  * Check how many shader variants you have


[](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-variants.html)
Introduction to shader variants
[](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-variant-stripping.html)
Strip shader variants
# Check how many shader variants you have
You can use logging and profiling tools to check how many **shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) variants Unity compiles, and identify ways you can remove ([strip](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-variant-stripping.html)) variants to improve build times and reduce memory usage. You can do the following:
  * [Get a list of shader variants the Editor uses](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-how-many-variants.html#get-shader-variants-editor-uses)
  * [Get a list of shader variants Unity creates at build time](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-how-many-variants.html#get-shader-variants-unity-creates)
  * [Get a list of shader variants Unity compiles at runtime](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-how-many-variants.html#get-shader-variants-unity-compiles)
  * [Check how much memory shaders use at runtime](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-how-many-variants.html#check-memory-shaders-use-runtime)
  * [Highlight missing shaders at runtime](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-how-many-variants.html#highlight-missing-shaders)


## Get a list of shader variants the Editor uses
You can generate a list of shader variants that the Editor uses in the **Scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) view and the Game view. To do this:
  1. Go to **Edit > Project Settings > Graphics**.
  2. Under **Shader Loading** , you can see how many shaders and shader variants you have next to **Currently tracked:**.
  3. Select **Save to asset…** to create a [shader variant collection asset](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-variant-collections.html).


## Get a list of shader variants Unity creates at build time
After you build your project, open the `Editor.log` log file and search for `Compiling shader` to see which variants Unity compiles and strips. For example:
```
Compiling shader "Sprites/Default" pass "" (vp)
    Full variant space:         8
    After settings filtering:   8
    After built-in stripping:   4
    After scriptable stripping: 4
    Processed in 0.00 seconds
    starting compilation...
    finished in 0.03 seconds. Local cache hits 0 (0.00s CPU time), remote cache hits 0 (0.00s CPU time), compiled 4 variants (0.09s CPU time), skipped 0 variants
    Prepared data for serialisation in 0.00s

```

If you use the Universal **Render Pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Renderpipeline) (URP) or the High Definition Render Pipeline (HDRP), refer to the following:
  * [Shader Stripping](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/shader-stripping.html) in URP
  * [Reduce shader variants](https://docs.unity3d.com/Packages/com.unity.render-pipelines.high-definition@17.0/manual/reduce-shader-variants.html) in HDRP


## Get a list of shader variants Unity compiles at runtime
  1. Go to **Edit > Project Settings > Graphics**.
  2. Under **Shader Loading** , enable **Log Shader Compilation**.
  3. When you build your project, enable ****Development Build** A development build includes debug symbols and enables the Profiler. [More info](https://docs.unity.com/devops/en/manual/build-target-configurations#Build_target_advanced_settings_overview)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#DevelopmentBuild)** in the [build settings](https://docs.unity3d.com/6000.0/Documentation/Manual/BuildSettings.html).
  4. In the [Console Window](https://docs.unity3d.com/6000.0/Documentation/Manual/Console.html)A Unity Editor window that shows errors, warnings and other messages generated by Unity, or your own scripts. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Console.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Consolewindow), select **Editor** and enable **Full Log [Developer Mode Only]**.
  5. Start the application you built.


Unity prints a `Compiled shader` message in the Console Window when it compiles a shader for the GPU.
## Check how much memory shaders use at runtime
Use the [Memory Profiler module](https://docs.unity3d.com/6000.0/Documentation/Manual/ProfilerMemory.html) or the [Memory Profiler package](https://docs.unity3d.com/Packages/com.unity.memoryprofiler@1.0/manual/index.html) to check how much memory shaders are using at runtime. If a shader uses a lot of memory, you can experiment with stripping its variants.
## Highlight missing shaders at runtime
In Unity 2022.2 and above, you can force Unity to show a pink error shader during runtime, when a Material tries to use a missing shader variant.
  1. Go to **Edit > Project Settings > Player**.
  2. Under **Other Settings** , in the **Shader Settings** section, select **Strict shader variant matching**.


You can also enable this in C# **scripts** A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/creating-scripts.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scripts) using [`strictShaderVariantMatching`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings-strictShaderVariantMatching.html).
When you do this, Unity shows a warning in the console with the missing variant and its keywords. You can use this during [stripping](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-variant-stripping.html) to check you don’t remove shader variants your project needs.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-variants.html)
Introduction to shader variants
[](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-variant-stripping.html)
Strip shader variants
