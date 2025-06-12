* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-tags.html

  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-and-shaders.html)
  * [Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)
  * [Writing custom shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-custom-shaders.html)
  * [Writing shaders in code](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-writing.html)
  * Configure when and if Unity uses a shader


[](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-branching-pass.html)
Branch based on shader pass or shader stage
[](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-tags-introduction.html)
Introduction to shader tags
# Configure when and if Unity uses a shader
Resources for using tags and blocks in a **shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) to configure if and when Unity uses the shader.
**Page** | **Description**  
---|---  
[Introduction to shader tags](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-tags-introduction.html) | Understand creating tags, accessing their values in **scripts** A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/creating-scripts.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scripts), and how tags vary by pipeline.  
[Add a shader tag to a SubShader or Pass](https://docs.unity3d.com/6000.0/Documentation/Manual/add-shader-tag.html) | Assign tags to a subshader or a shader pass by placing a `Tags` block.  
[Set a shader to require URP or HDRP](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-tags-pipeline.html) | Use a `RenderPipeline` tag to require the Universal **Render Pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Renderpipeline) or the High Definition Render Pipeline.  
[Set a shader to require a graphics API or platform](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-ShaderCompilationAPIs.html) | Use a `#pragma` directive to target a graphics API or platform.  
[Set a shader to require a shader model or GPU feature](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-ShaderCompileTargets.html) | Use a `#pragma` directive to target a shader model or GPU feature.  
[set a shader to require a package](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-tags-require-package.html) | Use a `PackageRequirements` block to add package requirements to a SubShader or Pass.  
[Set the render queue of a shader](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-tags-set-render-queue.html) | Use a `Queue` tag to set when Unity runs a shader.  
[Set when Unity runs a shader pass via a LightMode tag](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-tags-set-pass.html) | Use a `LightMode` tag to set when Unity runs a shader.  
[Prioritize lower quality shaders with the LOD command](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-prioritize-lower-quality-shaders.html) | Use a `LOD` command to fine-tune shader performance on different hardware.  
[Disable dynamic batching of a shader](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-tags-disable-dynamic-batching.html) | Use a `DisableBatching` tag to prevent Unity from applying **dynamic batching** An automatic Unity process which attempts to render multiple meshes as if they were a single mesh for optimized graphics performance. The technique transforms all of the GameObject vertices on the CPU and groups many similar vertices together. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/DrawCallBatching.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#DynamicBatching) to geometry.  
[Get tag values in C#](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-tags-get-tag-value.html) | Use APIs to get the value of tags in a subshader or a shader pass  
[Troubleshooting package requirement definitions](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-tags-require-package-troubleshooting.html) | Solve common issues with the `PackageRequirements` block, such as incorrect version values.  
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-branching-pass.html)
Branch based on shader pass or shader stage
[](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-tags-introduction.html)
Introduction to shader tags
