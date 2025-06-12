* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/shader-variants.html

  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-and-shaders.html)
  * [Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)
  * [Troubleshooting shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-troubleshooting.html)
  * [Reducing the size or number of shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-reducing.html)
  * [Reducing shader variants](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-variants-landing.html)
  * Introduction to shader variants


[](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-variants-landing.html)
Reducing shader variants
[](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-how-many-variants.html)
Check how many shader variants you have
# Introduction to shader variants
Shader variants, also sometimes called **shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) permutations, are one way of introducing conditional behavior into shader code.
Unity compiles shader source files into shader programs. Each compiled shader program has one or more **variants** : different versions of the shader program for different conditions. At runtime, Unity uses the variant that matches the current requirements. You configure variants using [shader keywords](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-keywords.html).
For a general overview of conditionals in shader code and when to use which technique, see [Conditionals in shader code](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-conditionals-choose-a-type.html). For more information on how Unity loads shader variants, see [Shader loading](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-loading.html).
Shaders with a large number of variants are called “mega shaders” or “uber shaders”. Unity’s Standard Shader is an example of such a shader.
## Advantages and disadvantages of shader variants
The main advantage of shader variants is that they allow you to use runtime conditionals in your shader programs, without the GPU performance impact of [dynamic branching](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-conditionals-choose-a-type.html). The main disadvantage of shader variants is that a large number of them can lead to longer build times, high shader memory usage, and shader compilation stutters.
When Unity creates shader variants, it uses static branching to create multiple small, specialized shader programs. At runtime, Unity uses the shader program that matches the conditions. This means that you can use shader variants for code that would likely result in reduced GPU performance in a dynamic branch, without suffering a GPU performance penalty.
However, a large number of variants can result in increased build times, file sizes, runtime memory usage, and loading times. It also leads to greater complexity when manually preloading (“prewarming”) shaders. When a project contains a very large number of shader variants, these issues can lead to significant problems with performance and workflow.
**Warning:** It is easy to inadvertently create an excessively large number of shader variants, which can lead to significant performance problems. It is therefore very important to understand [how Unity determines the number of shader variants](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-variants.html#number-shader-variants), [how to exclude (“strip”) unneeded variants from compilation](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-variant-stripping.html), and [when to use other types of conditionals in shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-conditionals-choose-a-type.html).
## Number of shader variants
At build time, Unity compiles one set of shader variants for each graphics API for the current build target. The number of variants for each combination of graphics API and build target depends on your shader source files, and your use of shader keywords.
You can [check how many shader variants you have](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-how-many-variants.html).
### Graphics APIs
Unity compiles one set of shader variants for each graphics API in the list for the current build target. The shaders differ for each combination of build target and graphics API; for example, Unity compiles different shaders for Metal on iOS than for Metal on macOS.
Some shader programs or keywords might only target a given graphics API or a given build target, so the total number of variants for each combination of graphics API and build target can differ; however, the process for compiling these variants is the same.
To view and edit the list of graphics APIs for your current build target, use the [Player Settings](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PlayerSettings.html)Settings that let you set various player-specific options for the final game built by Unity. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PlayerSettings.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#PlayerSettings) window, or the [PlayerSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.html) API.
### Number of shader programs
Unity must determine how many shader programs to compile for the current combination of build target and graphics API.
For each shader source file that is included in your build, Unity determines how many unique shader programs it defines:
  * A compute shader asset defines a single shader program.
  * In a hand-coded shader, the number of shader programs depends on your code. The total comprises: 
    * All shader stages in all Passes in the source file itself. For example, each vertex stage defines one shader program; each fragment stage defines one shader program; and so on.
    * All shader stages in all Passes in dependencies of the source file. This comprises all [fallback shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-Fallback.html), and all Passes that are included using the [UsePass command](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-UsePass.html).
  * In a Shader Graph shader, the number of shader programs depends on the code that Unity generates from your graph. To see the shader code that Unity generates, context-click the Shader Graph asset and select **See generated code**. You can then determine the total number of shader programs in the same way that you would for a hand-coded shader.


**Note:** A shader source file is included in a build if it is referenced in a **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) in that build, referenced by something in the **Resources** folder, or included in the **Always-included shaders** section of the [Graphics Settings](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GraphicsSettings.html) window.
### Keywords that affect a shader program
When Unity has determined how many shader programs it must compile for the current build target and graphics API, it then determines how many shader variants it must compile for each shader program.
For each shader program, Unity determines the combination of shader keywords that result in different variants. This comprises:
  * The sets of shader variant keywords that are declared in the source file for that shader. For more information, see [Declaring shader keywords](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-keywords.html#declaring-keywords).
  * The sets of shader keywords that Unity adds automatically. For more information, see [Unity’s predefined shader keywords](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-keywords-default.html).


The number of shader variants that Unity compiles for a shader program is the product of the keyword sets; that is to say, Unity compiles one variant for every combination that includes one element from each set. 
For example, this set contains three shader variant keywords:
  * COLOR_RED
  * COLOR_GREEN
  * COLOR_BLUE


This set contains four shader variant keywords:
  * QUALITY_LOW
  * QUALITY_MEDIUM
  * QUALITY_HIGH
  * QUALITY_ULTRA


A shader program affected by those shader variant keywords will result in the following twelve variants:
  * COLOR_RED and QUALITY_LOW
  * COLOR_RED and QUALITY_MEDIUM
  * COLOR_RED and QUALITY_HIGH
  * COLOR_RED and QUALITY_ULTRA
  * COLOR_GREEN and QUALITY_LOW
  * COLOR_GREEN and QUALITY_MEDIUM
  * COLOR_GREEN and QUALITY_HIGH
  * COLOR_GREEN and QUALITY_ULTRA
  * COLOR_BLUE and QUALITY_LOW
  * COLOR_BLUE and QUALITY_MEDIUM
  * COLOR_BLUE and QUALITY_HIGH
  * COLOR_BLUE and QUALITY_ULTRA


The number of variants that Unity compiles can grow very rapidly as you add more sets of shader variant keywords. The term for this very rapid growth is combinatorial explosion.
For example, consider a fairly typical use case, where a shader has a number of sets of shader variant keywords that contain two keywords each (`<feature name>_ON` and `<feature name>_OFF`). If the shader has two such sets of keywords, this results in four variants. If the shader has ten such sets of keywords, this results in 1024 variants.
### Deduplication of shader variants
After compilation, Unity automatically identifies identical variants within the same Pass, and ensures that these identical variants point to the same bytecode. This is called **deduplication**.
Deduplication prevents identical variants in the same Pass from increasing file size; however, identical variants still result in wasted work during compilation, and increased memory usage and shader loading times at runtime. With this in mind, it is always best to [strip unneeded variants](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-variant-stripping.html).
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-variants-landing.html)
Reducing shader variants
[](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-how-many-variants.html)
Check how many shader variants you have
