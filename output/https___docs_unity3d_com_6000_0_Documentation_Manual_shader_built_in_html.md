* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/shader-built-in.html

  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-and-shaders.html)
  * [Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)
  * [Prebuilt shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-built-in-landing.html)
  * Prebuilt shaders render pipeline compatibility reference


[](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-built-in-landing.html)
Prebuilt shaders
[](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-built-in-configure-properties.html)
Configuring material properties in prebuilt shaders
# Prebuilt shaders render pipeline compatibility reference
****Shaders** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader)** | **Universal**Render Pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Renderpipeline) (URP)** | **High Definition Render Pipeline (HDRP)** | **Custom SRP** | **Built-in Render Pipeline**  
---|---|---|---|---  
[**URP shaders**](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/shaders-in-universalrp.html) | Yes | No | No | No  
[**HDRP shaders**](https://docs.unity3d.com/Packages/com.unity.render-pipelines.high-definition@17.0/manual/materials-and-surfaces.html) | No | Yes | No | No  
[**Standard Shader**](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-StandardShader-landing.html) | No  
  
Can convert Standard Shader to equivalent on import | No  
  
Can convert Standard Shader to equivalent on import | No | Yes  
[**Standard Particle Shaders**](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-StandardParticleShadersLanding.html) | No | No | No | Yes  
[**Legacy shaders**](https://docs.unity3d.com/6000.0/Documentation/Manual/Built-inShaderGuide.html) | Yes  
  
Simple unlit Legacy shaders will likely render fine, but they might not be SRP Batcher compatible. | Yes  
  
Simple unlit Legacy shaders will likely render fine, but they might not be SRP Batcher compatible. They also do not support any HDRP features. For an unlit shader that supports HDRP features, use the HDRP/Unlit shader. | Yes  
  
Simple unlit Legacy shaders will likely render fine, but they might not be SRP Batcher compatible. | Yes  
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-built-in-landing.html)
Prebuilt shaders
[](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-built-in-configure-properties.html)
Configuring material properties in prebuilt shaders
