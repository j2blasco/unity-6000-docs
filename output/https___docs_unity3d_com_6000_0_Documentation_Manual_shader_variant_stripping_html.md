* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/shader-variant-stripping.html

  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-and-shaders.html)
  * [Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)
  * [Troubleshooting shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-troubleshooting.html)
  * [Reducing the size or number of shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-reducing.html)
  * [Reducing shader variants](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-variants-landing.html)
  * Strip shader variants


[](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-how-many-variants.html)
Check how many shader variants you have
[](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-keywords-default.html)
Default shader keywords
# Strip shader variants
You can prevent [shader variants](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-variants.html)A verion of a shader program that Unity generates according to a specific combination of shader keywords and their status. A Shader object can contain multiple shader variants. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-variants.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shadervariant) from being compiled. This is called **stripping**. Stripping unneeded variants can greatly reduce build times, file size, **shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) loading times, and runtime memory usage. In larger projects, or projects with complex shaders, this is a very important consideration.
If you strip a shader variant that a Material needs at runtime, Unity tries to choose a similar shader variant that’s available. To avoid this, use the following approaches:
  * If you use a `shader_feature` keyword, don’t use the keyword to change which code branch executes at runtime.
  * [Check what shader variants you have](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-how-many-variants.html) to help you see which shader variants and keyword combinations Materials need at runtime.
  * Add shaders to the **Always Included Shaders** list in [Graphics settings](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GraphicsSettings.html).


## Limit shader variants when you declare shader keywords
The way that you declare shader keywords can limit the number of variants that they produce:
  * Use `shader_feature` instead of `multi_compile` where possible - see [How Unity compiles branching shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-conditionals-choose-a-type.html).
  * Ensure that you don’t define unused keywords with `multi_compile`.


For information on declaring keywords in hand-coded shaders, see [Declaring and using shader keywords in HLSL](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-MultipleProgramVariants.html). For information on declaring keywords in Shader Graph, see [Shader Graph: Blackboard](https://docs.unity3d.com/Packages/com.unity.shadergraph@latest?subfolder=/manual/Blackboard.html).
### Indicate which shader keywords affect which shader stage
When you [declare a keyword](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-MultipleProgramVariants-declare.html), Unity assumes all stages of the shader contain conditional code for that keyword.
You can add the following suffixes to indicate that only certain stages contain conditional code for a keyword, so that Unity doesn’t generate unneeded shader variants.
  * `_vertex`
  * `_fragment`
  * `_hull`
  * `_domain`
  * `_geometry`


For example, use `#pragma shader_feature_fragment RED GREEN BLUE` to indicate that you use the 3 keywords to create conditional code in the fragment stage only.
You can’t add these suffixes to `#pragma dynamic_branch` because `dynamic_branch` doesn’t create variants.
These suffixes might behave differently or have no effect, depending on the [graphics API](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsDeviceType.html). For example:
  * The suffixes have no effect on OpenGL, OpenGL ES or Vulkan.
  * The `_geometry` and `_raytracing` suffixes have no effect on Metal. Metal treats `_vertex`, `_hull` and `_domain` as a single stage.


### Use preprocessor macros to limit variants by platform
In Unity 2021.3 and above, you can create conditional shader code using a [target platform preprocessor macro](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-branching-built-in-macros.html), so you can limit variants on platforms with limited memory.
The code sample does the following:
  * If you build for a [`SHADER_API_DESKTOP` platform](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-branching-built-in-macros.html), Unity builds variants for every possible keyword combination.
  * If you build for another platform, Unity builds only variants for keyword combinations the Materials in your build use.

```
#ifdef SHADER_API_DESKTOP
   #pragma multi_compile _ RED GREEN BLUE WHITE
#else
   #pragma shader_feature RED GREEN BLUE WHITE
#endif

```

You can use target platform preprocessor macros to select between `shader_feature`, `multi_compile` and `dynamic_branch`. For more information on when to use each type of conditional, see [Shader Conditionals](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-conditionals-choose-a-type.html).
### Create user-controlled quality settings
When you build for console and mobile platforms that have limited memory, you can limit shader variants by only allowing users to switch between a small number of quality settings.
For example, if you use the keywords `DYNAMIC_LIGHTING`, `SOFT_SHADOWS` and `HIGH_QUALITY_LIGHTMAPS`, you can create the following:
  * A ‘low quality’ setting that turns on `DYNAMIC_LIGHTING`.
  * A ‘high quality’ setting that turns on `DYNAMIC_LIGHTING`, `SOFT_SHADOWS` and `HIGH_QUALITY_LIGHTMAPS`.


This means Unity won’t create shader variants for `DYNAMIC_LIGHTING` when it’s off, or the many different combinations of the 3 keywords being on and off.
You can use [target platform preprocessor macros](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-branching-built-in-macros.html) to conditionally create fewer quality settings and fewer variants on platforms with limited memory. For example the following code sample will allow users to switch between 8 permutations of settings on `SHADER_API_DESKTOP` platforms, but only 2 on `SHADER_API_MOBILE` platforms.
```
#if SHADER_API_DESKTOP
   #pragma multi_compile SHADOWS_LOW SHADOWS_HIGH
   #pragma multi_compile REFLECTIONS_LOW REFLECTIONS_HIGH
   #pragma multi_compile CAUSTICS_LOW CAUSTICS_HIGH
#elif SHADER_API_MOBILE
   #pragma multi_compile QUALITY_LOW QUALITY_HIGH
   #pragma shader_feature CAUSTICS // Uses shader_feature, so Unity strips variants that use CAUSTICS if there are no Materials that use the keyword at build time.
#endif

```

## Strip shader variants in the Editor UI
There are several places in the Unity Editor UI where you can configure shader stripping:
  * In the [Graphics Settings window](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GraphicsSettings.html#stripping), configure the settings in the **Shader stripping** section:
  * Ensure that no unneeded shaders are included in the **Always-included shaders** setting.
  * Strip variants relating to GPU instancing, lightmapping, and fog.
  * In the Built-in **Render Pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Renderpipeline), if it is not important that your Tier settings are different, ensure that they are identical to each other. For more information, see [Graphics tiers](https://docs.unity3d.com/6000.0/Documentation/Manual/graphics-tiers.html).
  * In the Universal Render Pipeline (URP), disable unused features in the URP Asset. For more information, see [Shader stripping](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/shader-stripping.html).


If you use the Universal Render Pipeline you can also do the following:
  * In the [Universal Render Pipeline Asset](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/universalrp-asset.html), disable rendering any features your project doesn’t use.
  * Enable [shader stripping](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/shader-stripping.html).


If you use the High Definition Render Pipeline you can also do the following:
  * In the [High Definition Render Pipeline Asset](https://docs.unity3d.com/Packages/com.unity.render-pipelines.high-definition@17.0/manual/HDRP-Asset.html), disable any rendering features your project doesn’t use.
  * In the [Miscellaneous section of the HDRP Global Settings Window](https://docs.unity3d.com/Packages/com.unity.render-pipelines.high-definition@17.0/manual/Default-Settings-Window.html#miscellaneous), disable **Runtime Debug Shaders**.


## Strip shader variants using Editor scripts
For shader variants that you can’t strip in other ways, you can use the following APIs in an Editor script to perform build-time stripping:
  * [IPreprocessShaders.OnProcessShader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.IPreprocessShaders.OnProcessShader.html): receive a callback before Unity compiles a graphics shader Pass into a build.
  * [IPreprocessComputeShaders.OnProcessComputeShader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.IPreprocessComputeShaders.OnProcessComputeShader.html): receive a callback before Unity compiles a compute shader into a build.


For more information on this subject, refer to [Stripping scriptable shader variants](https://unity.com/blog/engine-platform/stripping-scriptable-shader-variants)
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-how-many-variants.html)
Check how many shader variants you have
[](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-keywords-default.html)
Default shader keywords
