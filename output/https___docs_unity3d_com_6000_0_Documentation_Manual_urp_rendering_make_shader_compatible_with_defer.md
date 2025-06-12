* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/urp/rendering/make-shader-compatible-with-deferred.html

  * [Rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/rendering-and-post-processing.html)
  * [Render pipelines](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)
  * [Using the Universal Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/universal-render-pipeline.html)
  * [Get started with URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/introduction-landing.html)
  * [Universal Render Pipeline fundamentals](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/urp-concepts.html)
  * [Rendering paths in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/rendering-paths-landing.html)
  * [Deferred rendering path in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/rendering/deferred-rendering-path-landing.html)
  * Make a shader compatible with the Deferred rendering path in URP


[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/rendering/accurate-g-buffer-normals.html)
Enable accurate G-buffer normals in the Deferred rendering path in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/rendering/forward-plus-rendering-path-limitations.html)
Troubleshooting the Forward+ rendering path in URP
# Make a shader compatible with the Deferred rendering path in URP
## Use a shader in the Deferred rendering path
To use a **shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) in the Deferred **rendering path** The technique that a render pipeline uses to render graphics. Choosing a different rendering path affects how lighting and shading are calculated. Some rendering paths are more suited to different platforms and hardware than others. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/RenderingPaths.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#RenderingPath), add the `UniversalGBuffer` tag to the Pass in your **ShaderLab** Unity’s language for defining the structure of Shader objects. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-Shader.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#ShaderLab) code. Unity executes the shader during the G-buffer render pass.
For example:
```
Shader "Examples/ExamplePassFlag"
{
    SubShader
    {
        Pass
        {    
              Tags
              { 
                "RenderPipeline" = "UniversalPipeline"
                "LightMode" = "UniversalGBuffer"
              }
            
              // The rest of the code that defines the Pass goes here.
        }
    }
}

```

## Use a shader in the forward pass of the Deferred rendering path
To use a shader in the Deferred rendering path, add the `UniversalForwardOnly` and `DepthNormalsOnly` tags to the Pass in your ShaderLab code. Unity executes the shader during the G-buffer render pass.
For example:
```
Shader "Examples/ExamplePassFlag"
{
    SubShader
    {
        Pass
        {    
              Tags { 
                "RenderPipeline" = "UniversalPipeline"
                "LightMode" = "UniversalForwardOnly"
                "LightMode" = "DepthNormalsOnly"
              }
            
              // The rest of the code that defines the Pass goes here.
        }
    }
}

```

## Specify the shader lighting model
To specify the shader lighting model as Lit or Simple Lit, use the `UniversalMaterialType` tag. For example:
```
Shader "Examples/ExamplePassFlag"
{
    SubShader
    {
        Pass
        {    
              Tags
              { 
                "RenderPipeline" = "UniversalPipeline"
                "LightMode" = "UniversalGBuffer"
                "UniversalMaterialType" = "Lit" 
              }
            
              // The rest of the code that defines the Pass goes here.
        }
    }
}

```

## Additional resources
  * [ShaderLab Pass tags in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/urp-shaders/urp-shaderlab-pass-tags.html)
  * [Pass tags in ShaderLab reference](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-PassTags.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/rendering/accurate-g-buffer-normals.html)
Enable accurate G-buffer normals in the Deferred rendering path in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/rendering/forward-plus-rendering-path-limitations.html)
Troubleshooting the Forward+ rendering path in URP
