* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/metal-requirements-and-compatibility.html

  * [Platform development ](https://docs.unity3d.com/6000.0/Documentation/Manual/PlatformSpecific.html)
  * [Cross-platform features and considerations](https://docs.unity3d.com/6000.0/Documentation/Manual/cross-platform-features.html)
  * [Graphics API support](https://docs.unity3d.com/6000.0/Documentation/Manual/GraphicsAPIs.html)
  * [Metal](https://docs.unity3d.com/6000.0/Documentation/Manual/Metal.html)
  * Metal requirements and compatibility


[](https://docs.unity3d.com/6000.0/Documentation/Manual/Metal.html)
Metal
[](https://docs.unity3d.com/6000.0/Documentation/Manual/metal-debug.html)
Debug Metal graphics
# Metal requirements and compatibility
This page lists the requirements for using Metal as well as the features that Metal is compatible with.
## Platform compatibility
Unity supports Metal for the Unity Player on iOS, tvOS, and macOS. Unity also supports Metal for the Unity Editor on macOS.
## Hardware compatibility
Unity supports Metal for all Apple devices that Unity supports.
## Render pipeline compatibility
**Feature** | **Built-in**Render Pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Renderpipeline)** | **Universal Render Pipeline (URP)** | **High Definition Render Pipeline (HDRP)** | **Custom Scriptable Render Pipeline (SRP)**  
---|---|---|---|---  
**Metal** | Yes | Yes | Yes (macOS only) | Yes  
## Shader compatibility
  * Metal supports **shaders** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) that have a minimum [shader compilation target](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-ShaderCompileTargets.html) of 3.5.
  * Metal doesn’t support geometry shaders.


## Additional resources
  * [Use 16-bit precision in shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-Use16BitPrecisionInShaders.html)
  * [Writing shaders for different graphics APIs](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-PlatformDifferences.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/Metal.html)
Metal
[](https://docs.unity3d.com/6000.0/Documentation/Manual/metal-debug.html)
Debug Metal graphics
