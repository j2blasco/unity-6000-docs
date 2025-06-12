* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-conservative-rasterization.html

  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-and-shaders.html)
  * [Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)
  * [Writing custom shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-custom-shaders.html)
  * [Writing shaders in code](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-writing.html)
  * [Writing a custom shader in ShaderLab and HLSL](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-landing.html)
  * [Setting the render state on the GPU](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-render-state-commands.html)
  * Enable conservative rasterization in a shader


[](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-render-state-commands.html)
Setting the render state on the GPU
[](https://docs.unity3d.com/6000.0/Documentation/Manual/set-culling-mode.html)
Set the culling mode in a shader
# Enable conservative rasterization in a shader
Rasterization is a rendering technique that converts vector data (triangle projections) to **pixel** The smallest unit in a computer image. Pixel size depends on your screen resolution. Pixel lighting is calculated at every screen pixel. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/ShadowPerformance.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#pixel) data (render target) by determining which pixels are covered by triangles. Normally, a GPU determines whether or not to rasterize a pixel by sampling points within the pixel to determine whether they are covered by the triangle; if the coverage is sufficient, then the GPU determines that the pixel is covered. Conservative **rasterization** The process of generating an image by calculating pixels for each polygon or triangle in the geometry. This is an alternative to ray tracing.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Rasterization) means that the GPU rasterizes a pixel that is partially covered by a triangle, regardless of coverage. This is useful when certainty is required, such as when performing **occlusion culling** A process that disables rendering GameObjects that are hidden (occluded) from the view of the camera. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/OcclusionCulling.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Occlusionculling), **collision** A collision occurs when the physics engine detects that the colliders of two GameObjects make contact or overlap, when at least one has a Rigidbody component and is in motion. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CollidersOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Collision) detection on the GPU, or visibility detection.
Conservative rasterization means that the GPU generates more fragments on triangle edges; this leads to more fragment **shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) invocations, which can lead to increased GPU frame times.
Check for hardware support using the [SystemInfo.supportsConservativeRaster](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.SystemInfo-supportsConservativeRaster.html) API. On hardware that does not support this command, it is ignored.
## Example
```
Shader "Examples/CommandExample"
{
    SubShader
    {
         // The rest of the code that defines the SubShader goes here.

        Pass
        {    
              // Enable conservative rasterization for this Pass.
              Conservative True
            
              // The rest of the code that defines the Pass goes here.
        }
    }
}

```

## Additional resources
  * [Conservative command in ShaderLab reference](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-Conservative.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-render-state-commands.html)
Setting the render state on the GPU
[](https://docs.unity3d.com/6000.0/Documentation/Manual/set-culling-mode.html)
Set the culling mode in a shader
