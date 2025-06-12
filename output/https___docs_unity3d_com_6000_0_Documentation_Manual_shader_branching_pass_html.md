* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/shader-branching-pass.html

  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-and-shaders.html)
  * [Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)
  * [Writing custom shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-custom-shaders.html)
  * [Writing shaders in code](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-writing.html)
  * [Branch in a shader via built-in macros](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-branching-built-in-macros.html)
  * Branch based on shader pass or shader stage


[](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-branching-unity-version.html)
Branch based on Unity version
[](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-tags.html)
Configure when and if Unity uses a shader
# Branch based on shader pass or shader stage
## Shader stage being compiled
Preprocessor macros `SHADER_STAGE_VERTEX`, `SHADER_STAGE_FRAGMENT`, `SHADER_STAGE_DOMAIN`, `SHADER_STAGE_HULL`, `SHADER_STAGE_GEOMETRY`, `SHADER_STAGE_COMPUTE` are defined when compiling each **Shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) stage. Typically they are useful when sharing Shader code between **pixel** The smallest unit in a computer image. Pixel size depends on your screen resolution. Pixel lighting is calculated at every screen pixel. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/ShadowPerformance.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#pixel) Shaders and compute Shaders, to handle cases where some things have to be done slightly differently.
## Surface Shader pass
When [Surface Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-SurfaceShaders.html)A streamlined way of writing shaders for the Built-in Render Pipeline. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-SurfaceShaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#SurfaceShader) are compiled, they generate a lot of code for various passes to do lighting. When compiling each pass, one of the following macros is defined:
**Macro:** | **Use:**  
---|---  
`UNITY_PASS_FORWARDBASE` |  **Forward rendering** A rendering path that renders each object in one or more passes, depending on lights that affect the object. Lights themselves are also treated differently by Forward Rendering, depending on their settings and intensity. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/RenderTech-ForwardRendering.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#ForwardRendering) base pass (main directional light, lightmaps, SH).  
`UNITY_PASS_FORWARDADD` | Forward rendering additive pass (one light per pass).  
`UNITY_PASS_DEFERRED` |  **Deferred shading** A rendering path in the Built-in Render Pipeline that places no limit on the number of Lights that can affect a GameObject. All Lights are evaluated per-pixel, which means that they all interact correctly with normal maps and so on. Additionally, all Lights can have cookies and shadows. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/RenderTech-DeferredShading.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Deferredshading) pass (renders G-buffer).  
`UNITY_PASS_SHADOWCASTER` | Shadow caster and depth Texture rendering pass.  
## Additional resources
  * [HLSL pragma directives reference](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-PragmaDirectives.html)
  * [HLSL pragma target command reference](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-Pragma-target.html)
  * [HLSL pragma require command reference](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-Pragma-require.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-branching-unity-version.html)
Branch based on Unity version
[](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-tags.html)
Configure when and if Unity uses a shader
