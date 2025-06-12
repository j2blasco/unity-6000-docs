* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/urp/render-graph-frame-data-reference.html

  * [Rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/rendering-and-post-processing.html)
  * [Render pipelines](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)
  * [Using the Universal Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/universal-render-pipeline.html)
  * [Custom rendering and post-processing in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/customizing-urp.html)
  * [Render graph system in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/render-graph.html)
  * [Frame data in the render graph system in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/render-graph-frame-data.html)
  * Frame data textures reference for URP


[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/render-graph-framebuffer-fetch.html)
Get the current framebuffer from GPU memory in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/render-graph-draw-objects-in-a-pass.html)
Draw objects in the render graph system in URP
# Frame data textures reference for URP
You can fetch the following textures from the frame data.
## Color data
**Property** | **Texture** | **URP**shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) pass that writes to the texture**  
---|---|---  
`activeColorTexture` | The color texture the **camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera) currently targets. | Any pass, depending on your settings  
`afterPostProcessColor` | The main color texture after URP’s post processing passes. | `UberPost`  
`backBufferColor ` | The color texture of the screen back buffer. If you use [post-processing](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/integration-with-post-processing.html)A process that improves product visuals by applying filters and effects before the image appears on screen. You can use post-processing effects to simulate physical camera and film properties, for example Bloom and Depth of Field. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/PostProcessingOverview.html) post processing, postprocessing, postprocess  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#post-processing), URP writes to this texture at the end of rendering, unless you enable [HDR Debug Views](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/post-processing/hdr-output-debug-views-urp.html). Refer to `debugScreenTexture` for more information. | Any pass, depending on your settings  
`cameraColor` | The main color texture for the camera. You can store multiple samples in this texture if you enable [Multisample Anti-aliasing (MSAA)](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/anti-aliasing.html#msaa). | Any pass, depending on your settings  
`cameraOpaqueTexture` | A texture with the opaque objects in the **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene), if you enable **Opaque Texture** in the [URP Asset](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/universalrp-asset.html). | `CopyColor`  
`debugScreenTexture` | If you enable [HDR Debug Views](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/post-processing/hdr-output-debug-views-urp.html), URP writes the output of [post-processing](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/integration-with-post-processing.html) to this texture instead of `backBufferColor`. |  `uberPost` and `finalPost`  
## Depth data
**Property** | **Texture** | **URP shader pass that writes to the texture**  
---|---|---  
`activeDepthTexture` | The **depth buffer** A memory store that holds the z-value depth of each pixel in an image, where the z-value is the depth for each rendered pixel from the projection plane. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-RenderTexture.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#depthbuffer) the GPU currently renders to. This is either `backBufferDepth` or `cameraDepth`. | Any pass, depending on your settings  
`backBufferDepth ` | The depth buffer of the screen back buffer. If you target `backBufferDepth`, any changes you make are overwritten when URP **blits** A shorthand term for “bit block transfer”. A blit operation is the process of transferring blocks of data from one place in memory to another.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#blit) `cameraDepth` to the back buffer near the end of a frame. | Any pass, depending on your settings  
`cameraDepth` | The depth buffer from the **render texture** A special type of Texture that is created and updated at runtime. To use them, first create a new Render Texture and designate one of your Cameras to render into it. Then you can use the Render Texture in a Material just like a regular Texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-RenderTexture.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#RenderTexture) the camera currently renders to. Avoid targeting `cameraDepth`, because URP uses this buffer for most of its own rendering. | Any pass, depending on your settings  
`cameraDepthTexture` | A depth texture copy of the depth buffer, if you enable **Depth Priming Mode** in the [renderer](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/urp-universal-renderer.html) or **Depth Texture** in the active [URP Asset](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/universalrp-asset.html). If you use the [Deferred render path](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/rendering/deferred-rendering-path-landing.html), `cameraDepthTexture` is a color format instead of a depth format. |  `CopyDepth` or `DepthPrepass`  
`cameraNormalsTexture` | The scene normals texture. Contains the scene depth for objects with shaders that have a `DepthNormals` pass. |  `DepthNormals` prepass  
## Shadow data
**Property** | **Texture** | **URP shader pass that writes to the texture**  
---|---|---  
`additionalShadowsTexture ` | The additional shadow map. | `ShadowCaster`  
`mainShadowsTexture ` | The main shadow map. | `ShadowCaster`  
## Decal data
**Property** | **Texture** | **URP shader pass that writes to the texture**  
---|---|---  
`dBuffer` | The Decals texture. For more information about the decals texture, refer to [DBuffer](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/renderer-feature-decal-reference.html#dbuffer). | `Decals`  
`dBufferDepth` | The Decals depth texture. Refer to [DBuffer](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/renderer-feature-decal-reference.html#dbuffer). | `Decals`  
## Motion vector data
**Property** | **Texture** | **URP shader pass that writes to the texture**  
---|---|---  
**Property** | **Texture** | **URP shader pass that writes to the texture**  
`motionVectorColor` | The motion vectors color texture. Refer to [motion vectors](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/features/motion-vectors.html). |  `Camera Motion Vectors` and `MotionVectors`  
`motionVectorDepth` | The motion vectors depth texture. Refer to [motion vectors](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/features/motion-vectors.html). |  `Camera Motion Vectors` and `MotionVectors`  
## Other data
**Property** | **Texture** | **URP shader pass that writes to the texture**  
---|---|---  
`gBuffer` | The G-buffer textures. Refer to [G-buffer](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/rendering/g-buffer-layout.html). | `GBuffer`  
`internalColorLut` | The internal look-up textures (LUT) texture. | `InternalLut`  
`overlayUITexture` | The overlay UI texture. | `DrawScreenSpaceUI`  
`renderingLayersTexture` | The Rendering Layers texture. Refer to [Rendering layers](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/features/rendering-layers.html) |  `DrawOpaques` or the `DepthNormals` prepass, depending on your settings.  
`ssaoTexture` | The Screen Space Ambient Occlusion (SSAO) texture. Refer to [Ambient occlusion](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/post-processing-ssao.html)A method to approximate how much ambient light (light not coming from a specific direction) can hit a point on a surface.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Ambientocclusion). | `SSAO`  
## Additional resources
  * [Using frame data in the render graph system](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/render-graph-frame-data.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/render-graph-framebuffer-fetch.html)
Get the current framebuffer from GPU memory in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/render-graph-draw-objects-in-a-pass.html)
Draw objects in the render graph system in URP
