* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-set-stencil.html

  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-and-shaders.html)
  * [Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)
  * [Writing custom shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-custom-shaders.html)
  * [Writing shaders in code](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-writing.html)
  * [Writing a custom shader in ShaderLab and HLSL](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-landing.html)
  * [Setting the render state on the GPU](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-render-state-commands.html)
  * Check or write to the stencil buffer in a shader


[](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-set-zwrite.html)
Disable writing to the depth buffer in a shader
[](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-blending-modes.html)
Set the blending mode in a shader
# Check or write to the stencil buffer in a shader
The **stencil buffer** A memory store that holds an 8-bit per-pixel value. In Unity, you can use a stencil buffer to flag pixels, and then only render to pixels that pass the stencil operation. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-RenderTexture.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#stencilbuffer) stores an 8-bit integer value for each **pixel** The smallest unit in a computer image. Pixel size depends on your screen resolution. Pixel lighting is calculated at every screen pixel. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/ShadowPerformance.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#pixel) in the frame buffer. Before executing the fragment **shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) for a given pixel, the GPU can compare the current value in the stencil buffer against a given reference value. This is called a stencil test. If the stencil test passes, the GPU performs the depth test. If the stencil test fails, the GPU skips the rest of the processing for that pixel. This means that you can use the stencil buffer as a mask to tell the GPU which pixels to draw, and which pixels to discard.
You would typically use the stencil buffer for special effects such as portals or mirrors. Additionally, the stencil buffer is sometimes used when rendering hard shadows, or [constructive solid geometry (CSG)](https://en.wikipedia.org/wiki/Constructive_solid_geometry).
You can use the `Stencil` command to do two different things: to configure the stencil test, and to configure what the GPU writes to the stencil buffer. You can do both of these things in the same command, but the most common use case is to create one **Shader object** An instance of the Shader class, a Shader object is container for shader programs and GPU instructions, and information that tells Unity how to use them. Use them with materials to determine the appearance of your scene. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-objects.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shaderobject) that masks out areas of the screen that other Shader objects cannot draw to. To do this, you need to configure the first Shader object to always pass the stencil test and write to the stencil buffer, and configure the others to perform a stencil test and not write to the stencil buffer.
Use the `Ref`, `ReadMask`, and `Comp` parameters to configure the stencil test. Use the `Ref`, `WriteMask`, `Pass`, `Fail`, and `ZFail` parameters to configure the stencil write operation.
This command makes a change to the render state. Use it in a `Pass` block to set the render state for that Pass, or use it in a `SubShader` block to set the render state for all Passes in that SubShader.
The stencil test equation is:
```
(ref & readMask) comparisonFunction (stencilBufferValue & readMask)

```

## Examples
```
Shader "Examples/CommandExample"
{
    SubShader
    {
         // The rest of the code that defines the SubShader goes here.

        Pass
        {    
             // All pixels in this Pass will pass the stencil test and write a value of 2 to the stencil buffer
             // You would typically do this if you wanted to prevent subsequent shaders from drawing to this area of the render target or restrict them to render to this area only
             Stencil
             {
                 Ref 2
                 Comp Always
                 Pass Replace
             }            

             // The rest of the code that defines the Pass goes here.
        }
    }
}

```

This example code demonstrates the syntax for using this command in a SubShader block.
```
Shader "Examples/CommandExample"
{
    SubShader
    {
             // All pixels in this SubShader pass the stencil test only if the current value of the stencil buffer is less than 2
             // You would typically do this if you wanted to only draw to areas of the render target that were not "masked out"
             Stencil
             {
                 Ref 2
                 Comp Less
             }  

         // The rest of the code that defines the SubShader goes here.        

        Pass
        {    
              // The rest of the code that defines the Pass goes here.
        }
    }
}

```

## Additional resources
  * [Stencil command in ShaderLab reference](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-Stencil.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-set-zwrite.html)
Disable writing to the depth buffer in a shader
[](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-blending-modes.html)
Set the blending mode in a shader
