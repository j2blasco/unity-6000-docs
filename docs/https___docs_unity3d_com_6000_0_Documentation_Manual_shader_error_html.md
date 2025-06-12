* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/shader-error.html

  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-and-shaders.html)
  * [Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)
  * [Troubleshooting shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-troubleshooting.html)
  * Error and loading shaders


[](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-troubleshooting.html)
Troubleshooting shaders
[](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-reduce-stalling.html)
Fixing hitches or stalls
# Error and loading shaders
Sometimes, Unity can’t render objects with regular **shaders** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader). When this happens, Unity renders the objects with special shaders:
  * [The default error shader](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-error.html#default-error-shader)
  * [The loading shader](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-error.html#loading-shader)
  * [The Streaming Virtual Texturing error material](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-error.html#svt-error-material)


The special shader that Unity uses depends on the reason that Unity can’t use the original shader.
## The default error shader
Unity renders an object with the default error shader when there’s a problem with that object’s material or shader; for example, if no material is assigned, if the shader doesn’t compile, or if the shader isn’t supported.
Unity uses the default error shader in the Unity Editor, and in builds.
The default error shader is magenta (bright pink).
![The magenta error shader.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/shader-error.png) The magenta error shader.
When you use the [BatchRendererGroup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchRendererGroup.html) API, Unity doesn’t display the default error shader. Use [BatchRendererGroup.SetErrorMaterial](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchRendererGroup.SetErrorMaterial.html) to set a material to use instead.
If your project uses the Universal Rendering Pipeline (URP), Unity might render an object using the default error shader if the object uses a shader from the Built-In **Render Pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Renderpipeline). Refer to [Converting your shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/upgrading-your-shaders.html) for more information.
## The loading shader
Unity renders an object with the loading shader to indicate that Unity is compiling the [shader variant](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-variants.html)A verion of a shader program that Unity generates according to a specific combination of shader keywords and their status. A Shader object can contain multiple shader variants. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-variants.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shadervariant) needed to display that object.
Unity shows the loading shader in the Unity Editor when [asynchronous shader compilation](https://docs.unity3d.com/6000.0/Documentation/Manual/AsynchronousShaderCompilation.html) is enabled, or in a **development build** A development build includes debug symbols and enables the Profiler. [More info](https://docs.unity.com/devops/en/manual/build-target-configurations#Build_target_advanced_settings_overview)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#DevelopmentBuild) when [Shader Live Link support](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildOptions.ShaderLivelinkSupport.html) is enabled.
The loading shader is cyan (bright blue).
![The cyan loading shader.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/shader-loading.png) The cyan loading shader.
When you use the [BatchRendererGroup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchRendererGroup.html) API, Unity doesn’t display the loading shader. Use [BatchRendererGroup.SetLoadingMaterial](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchRendererGroup.SetLoadingMaterial.html) to set a material to use instead.
## The Virtual Texturing error material
If your project uses [Streaming Virtual Texturing ](https://docs.unity3d.com/6000.0/Documentation/Manual/svt-streaming-virtual-texturing.html) (SVT), Unity uses a special material to indicate problems in your SVT setup. For more information, see [Virtual Texturing error material](https://docs.unity3d.com/6000.0/Documentation/Manual/svt-error-material.html).
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-troubleshooting.html)
Troubleshooting shaders
[](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-reduce-stalling.html)
Fixing hitches or stalls
