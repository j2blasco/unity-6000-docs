* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/urp/urp-shaders/shader-keywords-macros.html

  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-and-shaders.html)
  * [Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)
  * [Shaders in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/shaders-in-universalrp.html)
  * [Writing custom shaders in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/writing-custom-shaders-urp.html)
  * Shader keywords and macros reference in URP


[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/shaders-in-universalrp-srp-batcher.html)
Make a URP shader compatible with the SRP Batcher
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/shaders-in-universalrp-reference.html)
Shader Material Inspector window reference for URP
# Shader keywords and macros reference in URP
Shader keywords and macros that enable or provide access to URP features in **shaders** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader).
**Element** | **Description**  
---|---  
`_FORWARD_PLUS` | Use this `multi_compile` keyword to make the shader compatible with the Forward+ **rendering path** The technique that a render pipeline uses to render graphics. Choosing a different rendering path affects how lighting and shading are calculated. Some rendering paths are more suited to different platforms and hardware than others. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/RenderingPaths.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#RenderingPath). For an implementation example, refer to [Render additional lights in a shader](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/use-built-in-shader-methods-additional-lights-fplus.html).  
`_ADDITIONAL_LIGHTS` | Use this keyword to define areas in shader code that Unity should execute if per-pixel additional lights are enabled in a **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) and URP Asset. If a renderer uses the Forward+ rendering path, Unity ignores this keyword and uses the `_FORWARD_PLUS` keyword instead. For an implementation example, refer to [Render additional lights in a shader](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/use-built-in-shader-methods-additional-lights-fplus.html).  
`LIGHT_LOOP_BEGIN` | Use this macro to iterate over the additional lights. In the Forward+ rendering path, the `LIGHT_LOOP_BEGIN` macro requires the following struct to be in its scope, both the type and the variable name must match this signature: `InputData inputData`. For an implementation example, refer to [Render additional lights in a shader](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/use-built-in-shader-methods-additional-lights-fplus.html).  
## Additional resources
  * [Changing how shaders work via branching and keywords](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-MultipleProgramVariants.html)
  * [Shader methods in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/use-built-in-shader-methods.html)
  * [Custom lighting in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/lighting/custom-lighting-landing.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/shaders-in-universalrp-srp-batcher.html)
Make a URP shader compatible with the SRP Batcher
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/shaders-in-universalrp-reference.html)
Shader Material Inspector window reference for URP
