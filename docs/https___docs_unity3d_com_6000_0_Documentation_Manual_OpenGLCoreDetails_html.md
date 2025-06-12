* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/OpenGLCoreDetails.html

  * [Platform development ](https://docs.unity3d.com/6000.0/Documentation/Manual/PlatformSpecific.html)
  * [Cross-platform features and considerations](https://docs.unity3d.com/6000.0/Documentation/Manual/cross-platform-features.html)
  * [Graphics API support](https://docs.unity3d.com/6000.0/Documentation/Manual/GraphicsAPIs.html)
  * OpenGL Core


[](https://docs.unity3d.com/6000.0/Documentation/Manual/metal-optimize.html)
Optimize Metal graphics
[](https://docs.unity3d.com/6000.0/Documentation/Manual/ReducingFilesize.html)
Reducing the file size of your build
# OpenGL Core
OpenGL Core is a back end capable of supporting the latest OpenGL features on Windows, macOS, and Linux. This scales from OpenGL 3.2 to OpenGL 4.5, depending on the OpenGL driver support.
For information about how to enable OpenGL Core as your default Graphics API in the Editor or Standalone Player, refer to [Override default graphics APIs](https://docs.unity3d.com/6000.0/Documentation/Manual/configure-graphicsAPIs.html#override-default-gfxapi).
## OpenGL requirements
OpenGL Core has the following minimum requirements:
  * macOS 10.8 (OpenGL 3.2), macOS 10.9 (OpenGL 3.2 to 4.1)
  * Windows with NVIDIA since 2006 (GeForce 8), AMD since 2006 (Radeon HD 2000), Intel since 2012 (HD 4000 / IvyBridge) (OpenGL 3.2 to OpenGL 4.5)
  * Linux (OpenGL 3.2 to OpenGL 4.5)


## macOS OpenGL driver limitations
The macOS OpenGL backend for the Editor and Standalone supports OpenGL 3.x and 4.x features such as tessellation and geometry **shaders** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader). 
However, as Apple restricts the OpenGL version on OS X desktop to 4.1 at most, it does not support all DirectX 11 features (such as Unordered Access Views or Compute Shaders). This means that all shaders that are configured to target Shader Level 5.0 (with `#pragma target 50`) will fail to load on OS X.
Therefore a new shader target level is introduced: `#pragma target gl4.1`. This target level requires at least OpenGL 4.1 or DirectX 11.0 Shader Level 5 on desktop, or OpenGL ES 3.1 + Android Extension Pack on mobiles.
## OpenGL Core features
The new OpenGL back end introduces many new features (previously mostly DX11/GLES3 only):
  * Compute shaders (as well as ComputeBuffers and “random write” render textures)
  * Tessellation and Geometry shaders
  * Indirect draw ([Graphics.DrawProcedural](scriptRef:Graphics.DrawProcedural) and [Graphics.DrawProceduralIndirect](scriptRef:Graphics.DrawProceduralIndirect))
  * Advanced blend modes


## Additional resources
  * [Surface Shaders with DX11 / OpenGL Core Tessellation](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-SurfaceShaderTessellation.html)
  * [Graphics API arguments](https://docs.unity3d.com/6000.0/Documentation/Manual/EditorCommandLineArguments.html#gfx-api-arguments)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/metal-optimize.html)
Optimize Metal graphics
[](https://docs.unity3d.com/6000.0/Documentation/Manual/ReducingFilesize.html)
Reducing the file size of your build
