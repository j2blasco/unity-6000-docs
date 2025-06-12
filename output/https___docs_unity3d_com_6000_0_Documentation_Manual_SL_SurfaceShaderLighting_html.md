* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/SL-SurfaceShaderLighting.html

  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-and-shaders.html)
  * [Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)
  * [Shaders in the Built-In Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-built-in-birp-landing.html)
  * [Writing custom shaders in the Built-In Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shaders-birp.html)
  * [Writing Surface Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-surface-shaders.html)
  * Set the lighting model in a Surface Shader in the Built-In Render Pipeline


[](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-SurfaceShader-create.html)
Create a surface shader in the Built-In Render Pipeline
[](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-SurfaceShaderOptimize.html)
Optimize Surface Shaders
# Set the lighting model in a Surface Shader in the Built-In Render Pipeline
In the Built-in **Render Pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Renderpipeline), when writing [Surface Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-SurfaceShaders.html)A streamlined way of writing shaders for the Built-in Render Pipeline. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-SurfaceShaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#SurfaceShader), you describe the properties of a surface (such as albedo color and normal), and a **Lighting Model** computes the lighting interaction. 
There are two built-in lighting models: `Lambert` for diffuse lighting, and `BlinnPhong` for specular lighting. The _Lighting.cginc_ file inside Unity defines these models (Windows: _< unity install path>/Data/CGIncludes/Lighting.cginc_; macOS: _/Applications/Unity/Unity.app/Contents/CGIncludes/Lighting.cginc_).
Sometimes you might want to use a custom lighting model. You can do this with Surface **Shaders** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader). A lighting model is simply a couple of Cg/HLSL functions that match some conventions. 
## Render pipeline compatibility
**Feature name** | **Universal Render Pipeline (URP)** | **High Definition Render Pipeline (HDRP)** | **Custom SRP** | **Built-in Render Pipeline**  
---|---|---|---|---  
**Surface Shaders** | No  
  
For a streamlined way of creating Shader objects in URP, see [Shader Graph](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-graph.html). | No  
  
For a streamlined way of creating Shader objects in HDRP, see [Shader Graph](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-graph.html). | No | Yes  
## Declaring lighting models
A lighting model consists of regular functions with names that begin `Lighting`. You can declare them anywhere in your shader file, or one of the included files. The functions are:
  1. `half4 Lighting<Name> (SurfaceOutput s, UnityGI gi);` Use this in forward **rendering paths** The technique that a render pipeline uses to render graphics. Choosing a different rendering path affects how lighting and shading are calculated. Some rendering paths are more suited to different platforms and hardware than others. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/RenderingPaths.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#RenderingPath) for light models that are _not_ dependent on the view direction.
  2. `half4 Lighting<Name> (SurfaceOutput s, half3 viewDir, UnityGI gi);` Use this in **forward rendering** A rendering path that renders each object in one or more passes, depending on lights that affect the object. Lights themselves are also treated differently by Forward Rendering, depending on their settings and intensity. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/RenderTech-ForwardRendering.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#ForwardRendering) paths for light models that _are_ dependent on the view direction.
  3. `half4 Lighting<Name>_Deferred (SurfaceOutput s, UnityGI gi, out half4 outDiffuseOcclusion, out half4 outSpecSmoothness, out half4 outNormal);` Use this in **deferred shading** A rendering path in the Built-in Render Pipeline that places no limit on the number of Lights that can affect a GameObject. All Lights are evaluated per-pixel, which means that they all interact correctly with normal maps and so on. Additionally, all Lights can have cookies and shadows. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/RenderTech-DeferredShading.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Deferredshading) paths.


Note that you don’t need to declare all functions. A lighting model either uses view direction or it does not. Similarly, if the lighting model only works in forward rendering, do not declare the `_Deferred` function. This ensures that Shaders that use it only compile to forward rendering.
## Custom GI
Declare the following function to customize the decoding **lightmap** A pre-rendered texture that contains the effects of light sources on static objects in the scene. Lightmaps are overlaid on top of scene geometry to create the effect of lighting. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Lightmapping.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Lightmap) data and probes:
  1. `void Lighting<Name>_GI (SurfaceOutput s, UnityGIInput data, inout UnityGI gi);`


Note that to decode standard Unity lightmaps and SH probes, you can use the built-in `DecodeLightmap` and `ShadeSHPerPixel` functions, as seen in `UnityGI_Base` in the _UnityGlobalIllumination.cginc_ file inside Unity (Windows: _< unity install path>/Data/CGIncludes/UnityGlobalIllumination.cginc_; macOS: _/Applications/Unity/Unity.app/Contents/CGIncludes/UnityGlobalIllumination.cginc_ _).
## Example
The following is an example of a shader that uses the built-in Lambert lighting model:
```
  Shader "Example/Diffuse Texture" {
    Properties {
      _MainTex ("Texture", 2D) = "white" {}
    }
    SubShader {
      Tags { "RenderType" = "Opaque" }
      CGPROGRAM
      #pragma surface surf Lambert
      
      struct Input {
          float2 uv_MainTex;
      };
      
      sampler2D _MainTex;
      
      void surf (Input IN, inout SurfaceOutput o) {
          o.Albedo = tex2D (_MainTex, IN.uv_MainTex).rgb;
      }
      ENDCG
    }
    Fallback "Diffuse"
  }

```

Here’s how it looks like with a Texture and without a Texture, with one directional Light in the **Scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene): 
![Shader using a diffuse texture.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/SurfaceShaderDiffuseTexture.jpg) ![Shader without a diffuse texture.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/SurfaceShaderDiffuseNoTex.png)
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-SurfaceShader-create.html)
Create a surface shader in the Built-In Render Pipeline
[](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-SurfaceShaderOptimize.html)
Optimize Surface Shaders
