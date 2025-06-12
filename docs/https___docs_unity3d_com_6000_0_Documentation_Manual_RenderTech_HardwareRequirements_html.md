* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/RenderTech-HardwareRequirements.html

  * [Rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/rendering-and-post-processing.html)
  * [Render pipelines](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)
  * [Using the Built-In Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/built-in-render-pipeline.html)
  * Hardware requirements for the Built-in Render Pipeline


[](https://docs.unity3d.com/6000.0/Documentation/Manual/built-in-render-pipeline.html)
Using the Built-In Render Pipeline
[](https://docs.unity3d.com/6000.0/Documentation/Manual/built-in-graphics-quality-settings.html)
Graphics quality settings in the Built-In Render Pipeline
# Hardware requirements for the Built-in Render Pipeline
## Summary
|  |  |  |   
---|---|---|---|---  
| Win/Mac/Linux | iOS/Android | Consoles  
**Forward rendering** A rendering path that renders each object in one or more passes, depending on lights that affect the object. Lights themselves are also treated differently by Forward Rendering, depending on their settings and intensity. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/RenderTech-ForwardRendering.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#ForwardRendering) | Yes | Yes | Yes  
Vertex Lit rendering | Yes | Yes | -  
Realtime Shadows | GPU support | GPU support | Yes  
Image Effects | Yes | Yes | Yes  
Programmable **Shaders** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) | Yes | Yes | Yes  
Fixed Function Shaders | Yes | Yes | -  
## Realtime Shadows
Realtime Shadows work on most PC, console & mobile platforms. On Windows (Direct3D), the GPU also needs to support shadow mapping features; most discrete GPUs support that since 2003 and most integrated GPUs support that since 2007. Technically, on Direct3D 10, the GPU should support [D16/D24X8 or DF16/DF24](http://aras-p.info/texts/D3D9GPUHacks.html) **texture formats** A file format for handling textures during real-time rendering by 3D graphics hardware, such as a graphics card or mobile device. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextureImporterOverride)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#TextureFormat); and on OpenGL it should support the `GL_ARB_depth_texture` extension.
## Post-processing Effects
[Post-processing effects](https://docs.unity3d.com/6000.0/Documentation/Manual/PostProcessingOverview.html) require render-to-texture functionality, which is generally supported on anything made in this millenium.
## Shaders
You can write programmable or fixed function shaders. Programmable shaders are supported everywhere, and default to Shader Model 2.0 (desktop) and OpenGL ES 3.0. (mobile). You can target higher shader models if you want to add more functionality. Fixed function is supported everywhere except consoles.
## Additional resources
  * [Render pipeline feature comparison reference](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines-feature-comparison.html)
  * [Hardware requirements for the Univeral Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/requirements.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/built-in-render-pipeline.html)
Using the Built-In Render Pipeline
[](https://docs.unity3d.com/6000.0/Documentation/Manual/built-in-graphics-quality-settings.html)
Graphics quality settings in the Built-In Render Pipeline
