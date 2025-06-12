* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/UsingDX11GL3Features.html

  * [Platform development ](https://docs.unity3d.com/6000.0/Documentation/Manual/PlatformSpecific.html)
  * [Cross-platform features and considerations](https://docs.unity3d.com/6000.0/Documentation/Manual/cross-platform-features.html)
  * [Graphics API support](https://docs.unity3d.com/6000.0/Documentation/Manual/GraphicsAPIs.html)
  * DirectX


[](https://docs.unity3d.com/6000.0/Documentation/Manual/configure-graphicsAPIs.html)
Configure graphics APIs
[](https://docs.unity3d.com/6000.0/Documentation/Manual/Metal.html)
Metal
# DirectX
Unity supports the DirectX graphics API including both DirectX 11 and DirectX 12. However, not all features are available in DirectX 11. For more information, refer to [Feature comparison of DirectX 11 and DirectX 12 in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingDX11GL3Features.html#comparison-of-directx11-and-directx12-in-unity). 
## Set your default graphics API to DirectX
You can choose to set DirectX 11 (DX11) or DirectX 12 (DX12) as your default Graphics API in the Editor or Standalone Player:
  1. Open the [Player settings](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PlayerSettings.html)Settings that let you set various player-specific options for the final game built by Unity. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PlayerSettings.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#PlayerSettings) (menu: **Edit** > **Project Settings** > **Player**).
  2. In the **Other Settings** > **Rendering** section, disable the **Auto Graphics API for a platform (Windows/Mac/Linux)** option. 
  3. Select the **Add** (**+**) button, then select **Direct3D11** or **Direct3D12** from the list of the supported Graphics APIs.


## Feature comparison of DirectX 11 and DirectX 12 in Unity
The following lists include the features introduced with the DirectX 12 graphics API, which are unavailable in DirectX 11. 
**APIs** | **DirectX 11** | **DirectX 12**  
---|---|---  
[Dynamic resolution](https://docs.unity3d.com/6000.0/Documentation/Manual/DynamicResolution-introduction.html)A Camera setting that allows you to dynamically scale individual render targets to reduce workload on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/DynamicResolution-landing.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#dynamicresolution) | Unsupported | Supported  
[Asynchronous compute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.ExecuteCommandBufferAsync.html) | Unsupported | Supported  
[Native render pass](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ScriptableRenderContext.BeginRenderPass.html) | Unsupported | Supported  
[Ray tracing acceleration](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RayTracingAccelerationStructure.html) | Unsupported | Supported  
[Graphics state collection](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.Rendering.GraphicsStateCollection.html) | Unsupported | Supported  
[XR foveated rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/xr-foveated-rendering.html) | Unsupported | Supported  
**Render Threading Mode** | **DirectX 11** | **DirectX 12**  
---|---|---  
[Direct](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderingThreadingMode.Direct.html) | Supported | Supported  
[Single threaded](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderingThreadingMode.SingleThreaded.html) | Supported | Supported  
[Main + render thread](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderingThreadingMode.MultiThreaded.html) | Supported | Supported  
[Legacy jobified](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderingThreadingMode.LegacyJobified.html) | Supported | Supported  
[Native graphics jobs](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderingThreadingMode.NativeGraphicsJobs.html) | Unsupported | Supported  
[Split graphics jobs](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderingThreadingMode.NativeGraphicsJobsSplitThreading.html) | Unsupported | Supported  
****Shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) features** | **DirectX 11** | **DirectX 12**  
---|---|---  
[Ray tracing shader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RayTracingShader.html) | Unsupported | Supported  
[Inline ray tracing](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.SetRayTracingAccelerationStructure.html) (`#pragma multi_compile _ UNITY_DEVICE_SUPPORTS_INLINE_RAY_TRACING`) | Unsupported | Supported  
[Native 16-bit](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-ShaderCompileTargets.html) (`#pragma multi_compile _ UNITY_DEVICE_SUPPORTS_NATIVE_16BIT`) | Unsupported | Supported  
[Wave function](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-ShaderCompileTargets.html) (`#pragma multi_compile _ UNITY_DEVICE_SUPPORTS_WAVE_ANY`) | Unsupported | Supported  
**Universal**Render Pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Renderpipeline)** | **DirectX 11** | **DirectX 12**  
---|---|---  
[Raster pass merging](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/render-graph-introduction.html) | Unsupported | Supported (Windows on ARM)  
[Native RenderPass](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/urp-universal-renderer.html#native-renderpass) | Unsupported | Supported (Windows on ARM)  
[Framebuffer fetch](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/render-graph-framebuffer-fetch.html) | Unsupported | Supported (Windows on ARM)  
**High Definition Render Pipeline** | **DirectX 11** | **DirectX 12**  
---|---|---  
[Hardware dynamic resolution](https://docs.unity3d.com/Packages/com.unity.render-pipelines.high-definition@latest/index.html?subfolder=/manual/Dynamic-Resolution.html) | Unsupported | Supported  
[Asynchronous Compute Shaders](https://docs.unity3d.com/Packages/com.unity.render-pipelines.high-definition@latest/index.html?subfolder=/manual/frame-settings-reference.html#asynchronous-compute-shaders) | Unsupported | Supported  
[Ray traced ambient occlusion](https://docs.unity3d.com/Packages/com.unity.render-pipelines.high-definition@latest/index.html?subfolder=/manual/Ray-Traced-Ambient-Occlusion.html) | Unsupported | Supported  
[Ray traced contact shadows](https://docs.unity3d.com/Packages/com.unity.render-pipelines.high-definition@latest/index.html?subfolder=/manual/Ray-Traced-Contact-Shadows.html) | Unsupported | Supported  
[Ray traced global illumination](https://docs.unity3d.com/Packages/com.unity.render-pipelines.high-definition@latest/index.html?subfolder=/manual/Ray-Traced-Global-Illumination.html) | Unsupported | Supported  
[Ray traced reflections](https://docs.unity3d.com/Packages/com.unity.render-pipelines.high-definition@latest/index.html?subfolder=/manual/Ray-Traced-Reflections.html) | Unsupported | Supported  
[Ray traced shadows](https://docs.unity3d.com/Packages/com.unity.render-pipelines.high-definition@latest/index.html?subfolder=/manual/Ray-Traced-Shadows.html) | Unsupported | Supported  
[Ray traced recursion](https://docs.unity3d.com/Packages/com.unity.render-pipelines.high-definition@latest/index.html?subfolder=/manual/Ray-Tracing-Recursive-Rendering.html) | Unsupported | Supported  
[Ray traced subsurface scattering](https://docs.unity3d.com/Packages/com.unity.render-pipelines.high-definition@latest/index.html?subfolder=/manual/Ray-Traced-Subsurface-Scattering.html) | Unsupported | Supported  
## Additional resources
  * [Configure graphics APIs](https://docs.unity3d.com/6000.0/Documentation/Manual/configure-graphicsAPIs.html)
  * [Surface Shaders with DX11 / OpenGL Core Tessellation](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-SurfaceShaderTessellation.html)
  * [Surface shaders and DirectX 11 HLSL syntax](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-SurfaceShaders.html#surface-shaders-directX)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/configure-graphicsAPIs.html)
Configure graphics APIs
[](https://docs.unity3d.com/6000.0/Documentation/Manual/Metal.html)
Metal
