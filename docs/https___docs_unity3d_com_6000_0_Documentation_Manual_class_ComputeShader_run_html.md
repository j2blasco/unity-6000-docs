* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/class-ComputeShader-run.html

  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-and-shaders.html)
  * [Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)
  * [Writing custom shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-custom-shaders.html)
  * [Compute shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ComputeShader.html)
  * Run a compute shader


[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ComputeShader-hlsl-shaderlab.html)
Use HLSL and ShaderLab in a compute shader
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ComputeShader-crossplatform.html)
Writing compute shaders for multiple platforms
# Run a compute shader
In your script, define a variable of ComputeShader type and assign a reference to the Asset. This allows you to invoke them with [ComputeShader.Dispatch](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.Dispatch.html) function. See Unity documentation on [ComputeShader class](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.html) for more details.
Closely related to compute **shaders** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) is a [ComputeBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeBuffer.html) class, which defines arbitrary data buffer (“structured buffer” in DX11 lingo). [Render Textures](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.html)A special type of Texture that is created and updated at runtime. To use them, first create a new Render Texture and designate one of your Cameras to render into it. Then you can use the Render Texture in a Material just like a regular Texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-RenderTexture.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#RenderTexture) can also be written into from compute shaders, if they have “random access” flag set (“unordered access view” in DX11). See [RenderTexture.enableRandomWrite](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture-enableRandomWrite.html) to learn more about this.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ComputeShader-hlsl-shaderlab.html)
Use HLSL and ShaderLab in a compute shader
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ComputeShader-crossplatform.html)
Writing compute shaders for multiple platforms
