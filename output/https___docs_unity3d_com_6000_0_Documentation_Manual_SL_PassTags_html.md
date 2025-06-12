* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/SL-PassTags.html

  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-and-shaders.html)
  * [Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)
  * [Shader languages reference](https://docs.unity3d.com/6000.0/Documentation/Manual/shaders-reference.html)
  * [ShaderLab language reference](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-Reference.html)
  * [Pass in ShaderLab reference](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-SubShader-pass.html)
  * Pass tags in ShaderLab reference


[](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-Name.html)
Name directive in ShaderLab reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-shaderlab-code-blocks.html)
Shader code blocks in ShaderLab reference
# Pass tags in ShaderLab reference
This page contains information on using a `Tags` block in your **ShaderLab** Unity’s language for defining the structure of Shader objects. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-Shader.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#ShaderLab) code to assign tags to a Pass. It also contains information on using the `LightMode` tag.
For information on how a **Shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) object works, and the relationship between **Shader objects** An instance of the Shader class, a Shader object is container for shader programs and GPU instructions, and information that tells Unity how to use them. Use them with materials to determine the appearance of your scene. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-objects.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shaderobject), SubShaders and Passes, see [Shader object fundamentals](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html).
## Render pipeline compatibility
**Feature name** | **Universal**Render Pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Renderpipeline) (URP)** | **High Definition Render Pipeline (HDRP)** | **Custom SRP** | **Built-in Render Pipeline**  
---|---|---|---|---  
**ShaderLab: Pass Tags block** | Yes | Yes | Yes | Yes  
**ShaderLab: LightMode Pass tag** | Yes | Yes | Yes | Yes  
## Syntax
**Signature** | **Function**  
---|---  
`Tags {"<name1>" = "<value1>" "<name2>" = "<value2>"}` | Applies the given tags to the Pass.  
  
You can define as many tags as you like.  
### LightMode tag
**Signature** | **Function**  
---|---  
“LightMode” = “[value]” | Sets the LightMode value for this Pass.  
Valid values for this tag depend on the render pipeline.
#### LightMode tag valid values
These are the valid values for the `LightMode` Pass tag in the Built-in Render Pipeline. For more information on the LightMode tag, see [ShaderLab: using Pass tags](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-PassTags.html).
**Value** | **Function**  
---|---  
`Always` | Always rendered; does not apply any lighting. This is the default value.  
`ForwardBase` | Used in **Forward rendering** A rendering path that renders each object in one or more passes, depending on lights that affect the object. Lights themselves are also treated differently by Forward Rendering, depending on their settings and intensity. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/RenderTech-ForwardRendering.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#ForwardRendering); applies ambient, main directional light, vertex/SH lights and **lightmaps** A pre-rendered texture that contains the effects of light sources on static objects in the scene. Lightmaps are overlaid on top of scene geometry to create the effect of lighting. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Lightmapping.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Lightmap).  
`ForwardAdd` | Used in Forward rendering; applies additive per-pixel lights, one Pass per light.  
`Deferred` | Used in **Deferred Shading** A rendering path in the Built-in Render Pipeline that places no limit on the number of Lights that can affect a GameObject. All Lights are evaluated per-pixel, which means that they all interact correctly with normal maps and so on. Additionally, all Lights can have cookies and shadows. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/RenderTech-DeferredShading.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Deferredshading); renders G-buffer.  
`ShadowCaster` | Renders object depth into the shadowmap or a depth texture.  
`MotionVectors` | Used to calculate per-object motion vectors.  
`Vertex` | Used in legacy Vertex Lit rendering when the object is not lightmapped; applies all vertex lights.  
`VertexLMRGBM` | Used in legacy Vertex Lit rendering when the object is lightmapped, and on platforms where the lightmap is RGBM encoded (PC & console).  
`VertexLM` | Used in legacy Vertex Lit rendering when the object is lightmapped, and on platforms where lightmap is double-LDR encoded (mobile platforms).  
`Meta` | This Pass is not used during regular rendering, only for lightmap baking or **Enlighten** A lighting system by Geomerics used in Unity for Enlighten Realtime Global Illumination. [More info](https://www.siliconstudio.co.jp/en/products-service/enlighten/)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Enlighten) Realtime **Global Illumination** A group of techniques that model both direct and indirect lighting to provide realistic lighting results.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#globalillumination). For more information, see [Lightmapping and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/MetaPass.html).  
### PassFlags tag
In the Built-in Render Pipeline, use the `PassFlags` Pass tag to specify what data Unity provides to the Pass.
**Value** | **Function**  
---|---  
OnlyDirectional | Valid only in the Built-in Render Pipeline, when the rendering path is set to Forward, in a Pass with a `LightMode` tag value of `ForwardBase`.  
  
Unity provides only the main directional light and ambient/light probe data to this Pass. This means that data of non-important lights is not passed into vertex-light or spherical harmonics shader variables. See [Forward rendering path](https://docs.unity3d.com/6000.0/Documentation/Manual/RenderTech-ForwardRendering.html) for details.  
#### Example
```
Shader "Examples/ExamplePassFlag"
{
    SubShader
    {
        Pass
        {    
              Tags { "LightMode" = "ForwardBase" "PassFlags" = "OnlyDirectional" }
            
              // The rest of the code that defines the Pass goes here.
        }
    }
}

```

### RequireOptions tag
In the Built-in Render Pipeline, the `RequireOptions` Pass tag enables or disables a Pass based on **project settings** A broad collection of settings which allow you to configure how Physics, Audio, Networking, Graphics, Input and many other areas of your project behave. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/comp-ManagerGroup.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#ProjectSettings).
**Value** | **Function**  
---|---  
`SoftVegetation` | Render this Pass only if [QualitySettings-softVegetation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings-softVegetation.html) is enabled.  
## Additional resources
  * [Configure if or when Unity uses a shader](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-tags.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-Name.html)
Name directive in ShaderLab reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-shaderlab-code-blocks.html)
Shader code blocks in ShaderLab reference
