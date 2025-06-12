* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/SL-SurfaceShaders-output.html

  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-and-shaders.html)
  * [Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)
  * [Shaders in the Built-In Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-built-in-birp-landing.html)
  * [Writing custom shaders in the Built-In Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shaders-birp.html)
  * [Writing Surface Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-surface-shaders.html)
  * Surface Shader output structures in the Built-In Render Pipeline


[](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-SurfaceShaders.html)
Introduction to surface shaders in the Built-In Render Pipeline
[](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-RenderPipeline.html)
Surface Shaders and rendering paths in the Built-In Render Pipeline
# Surface Shader output structures in the Built-In Render Pipeline
Standard output structure of surface **shaders** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) is this:
```
struct SurfaceOutput
{
    fixed3 Albedo;  // diffuse color
    fixed3 Normal;  // tangent space normal, if written
    fixed3 Emission;
    half Specular;  // specular power in 0..1 range
    fixed Gloss;    // specular intensity
    fixed Alpha;    // alpha for transparencies
};

```

In Unity 5, **surface shaders** A streamlined way of writing shaders for the Built-in Render Pipeline. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-SurfaceShaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#SurfaceShader) can also use physically based lighting models. Built-in Standard and StandardSpecular lighting models (see below) use these output structures respectively:
```
struct SurfaceOutputStandard
{
    fixed3 Albedo;      // base (diffuse or specular) color
    fixed3 Normal;      // tangent space normal, if written
    half3 Emission;
    half Metallic;      // 0=non-metal, 1=metal
    half Smoothness;    // 0=rough, 1=smooth
    half Occlusion;     // occlusion (default 1)
    fixed Alpha;        // alpha for transparencies
};
struct SurfaceOutputStandardSpecular
{
    fixed3 Albedo;      // diffuse color
    fixed3 Specular;    // specular color
    fixed3 Normal;      // tangent space normal, if written
    half3 Emission;
    half Smoothness;    // 0=rough, 1=smooth
    half Occlusion;     // occlusion (default 1)
    fixed Alpha;        // alpha for transparencies
};

```

* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-SurfaceShaders.html)
Introduction to surface shaders in the Built-In Render Pipeline
[](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-RenderPipeline.html)
Surface Shaders and rendering paths in the Built-In Render Pipeline
