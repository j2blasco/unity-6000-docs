* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/shader-introduction.html

  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-and-shaders.html)
  * [Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)
  * Introduction to shaders


[](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)
Shaders
[](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-built-in-landing.html)
Prebuilt shaders
# Introduction to shaders
A **shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) program, commonly referred to as a shader, is a program that runs on a GPU.
## Types of shader
In Unity, shaders are divided into three broad categories. You use each category for different things, and work with them differently.
  * Shaders that are part of the [graphics pipeline](https://en.wikipedia.org/wiki/Graphics_pipeline) are the most common type of shader. They perform calculations that determine the color of **pixels** The smallest unit in a computer image. Pixel size depends on your screen resolution. Pixel lighting is calculated at every screen pixel. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/ShadowPerformance.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#pixel) on the screen. In Unity, you usually work with this type of shader by using [Shader objects](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-objects.html)An instance of the Shader class, a Shader object is container for shader programs and GPU instructions, and information that tells Unity how to use them. Use them with materials to determine the appearance of your scene. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-objects.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shaderobject).
  * [Compute shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ComputeShader.html) perform calculations on the GPU, outside of the regular graphics pipeline.
  * **Ray tracing** The process of generating an image by tracing out rays from the Camera through each pixel and recording the color contribution at the hit point. This is an alternative to rasterization. raytracing  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Raytracing) shaders perform calculations related to ray tracing.


## Terminology
The terminology around shaders can be confusing; people commonly use the word “shader” to mean different things.
In this documentation, the terminology is as follows:
  * **shader** or **shader program** - a program that runs on a GPU. Unless otherwise specified, this means shader programs that are part of the graphics pipeline.
  * **Shader object** - an instance of the `Shader` class. A Shader object is a wrapper for shader programs and other information.
  * ****ShaderLab** Unity’s language for defining the structure of Shader objects. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-Shader.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#ShaderLab)** - a Unity-specific language for writing shaders.
  * **Shader Graph** - a tool for creating shaders without writing code.
  * **shader asset** - a file with the `.shader` extension in your Unity project. It defines a Shader object.
  * **Shader Graph asset** - a file in your Unity project. It defines a Shader object.


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)
Shaders
[](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-built-in-landing.html)
Prebuilt shaders
