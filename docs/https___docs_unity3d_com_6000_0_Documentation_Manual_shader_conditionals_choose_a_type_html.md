* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/shader-conditionals-choose-a-type.html

  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-and-shaders.html)
  * [Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)
  * [Writing custom shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-custom-shaders.html)
  * [Writing shaders in code](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-writing.html)
  * [Changing how shaders work using keywords](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-MultipleProgramVariants.html)
  * How Unity compiles branching shaders


[](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-keywords.html)
Shader keywords workflow
[](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-MultipleProgramVariants-declare.html)
Declare shader keywords
# How Unity compiles branching shaders
When you use a keyword, you can choose how Unity compiles the **shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) code. The options are:
  * Dynamic branching: Unity keeps branching code in one compiled shader program.
  * Shader variants: Unity compiles a separate shader program called a shader variant for each branch. This is a form of static branching, and can help minimize your shader code.


## Dynamic branching
To use dynamic branching, use `#pragma dynamic_branch` to declare keywords. For example:
```
#pragma dynamic_branch RED GREEN

...

if (RED)
{
    // Output red
}
else if (GREEN)
{
    // Output green
}

```

At compile time, Unity converts each keyword into a uniform integer variable in the compiled shader code, which can have a value of either `0` or `1`. At runtime, for each draw call, Unity sends the state of each keyword integer to the GPU.
You can use `dynamic_branch` if your shaders run on a fast GPU, and don’t have asymmetric code branches where one branch is longer or more complex than the other.
## Shader variants
To use shader variants, use `#pragma multi_compile` or `#pragma shader_feature` to declare keywords. For example:
```
#pragma multi_compile RED GREEN

if (RED)
{
    // Output red
}
else if (GREEN)
{
    // Output green
}

```

At compile time, Unity splits the previous code into 2 separate but similar shader files called shader variants. One file contains the code that outputs red, and the other contains the code that outputs green. Each draw call, Unity sends the GPU the correct shader variant.
### Choosing a shader variant type
If you only need a shader to branch based on material properties, use `shader_feature`. Unity compiles shader variants for keyword combinations that materials in your build use, and removes other shader variants. This keeps build times low and file sizes small. 
**Note:** At runtime, if you use a keyword combination you didn’t use at build time, Unity tries to find the shader variant that closely matches. You can [highlight missing shaders at runtime](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-how-many-variants.html#highlight-missing-shaders) instead, or include a [shader variant collection](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-variant-collections.html) in the list of [preloaded shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GraphicsSettings.html#shader-loading).
If you need to use a C# script to make the shader branch at runtime, use `multi_compile`. Unity compiles shader variants regardless of whether they’re used by materials in your build. For example, you can use `multi_compile` to give users dynamic control over whether fog appears in a game.
**Important** : If you use `multi_compile`, Unity might spend a long time compiling, because each combination of keywords becomes a shader variant. For example, if you have 8 keyword sets with 3 keywords each, Unity might compile over 6,000 shader variants. Use `shader_feature` instead, or use different ways to [strip shader variants](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-variant-stripping.html).
## Additional resources
  * [Shader keywords fundamentals](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-keywords.html)
  * [Prevent global keyword objects affecting shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-keywords-scripts.html#prevent-global-keyword-objects-affecting-shaders)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-keywords.html)
Shader keywords workflow
[](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-MultipleProgramVariants-declare.html)
Declare shader keywords
