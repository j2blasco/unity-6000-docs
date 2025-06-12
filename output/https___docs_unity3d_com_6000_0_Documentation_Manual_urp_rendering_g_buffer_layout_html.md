* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/urp/rendering/g-buffer-layout.html

  * [Rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/rendering-and-post-processing.html)
  * [Render pipelines](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)
  * [Using the Universal Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/universal-render-pipeline.html)
  * [Get started with URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/introduction-landing.html)
  * [Universal Render Pipeline fundamentals](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/urp-concepts.html)
  * [Rendering paths in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/rendering-paths-landing.html)
  * [Deferred rendering path in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/rendering/deferred-rendering-path-landing.html)
  * G-buffer layout in the Deferred rendering path in URP


[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/rendering/render-passes-deferred.html)
Render passes in the Deferred rendering path in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/rendering/accurate-g-buffer-normals.html)
Enable accurate G-buffer normals in the Deferred rendering path in URP
# G-buffer layout in the Deferred rendering path in URP
The following illustration shows the data structure for each **pixel** The smallest unit in a computer image. Pixel size depends on your screen resolution. Pixel lighting is calculated at every screen pixel. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/ShadowPerformance.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#pixel) of the render targets that Unity uses in the G-buffer in the Deferred **rendering path** The technique that a render pipeline uses to render graphics. Choosing a different rendering path affects how lighting and shading are calculated. Some rendering paths are more suited to different platforms and hardware than others. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/RenderingPaths.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#RenderingPath).
![Data structure of the render targets that Unity uses in the Deferred Rendering Path](https://docs.unity3d.com/6000.0/Documentation/uploads/urp/rendering-deferred/data-structure-render-targets-g-buffer.png) Data structure of the render targets that Unity uses in the Deferred Rendering Path
## Albedo (sRGB)
This field contains the albedo color in 24-bit sRGB format.
## MaterialFlags
This field is a bit field that contains material flags:
  * Bit 0, **ReceiveShadowsOff** : if set, the pixel does not receive dynamic shadows.
  * Bit 1, **SpecularHighlightsOff** : if set, the pixel does not receive specular highlights.
  * Bit 2, **SubtractiveMixedLighting** : if set, the pixel uses the Subtractive Lighting Mode.
  * Bit 3, **SpecularSetup** : if set, the material uses the specular workflow.


Bits 4 to 7 are reserved for future use.
## Specular
This field contains the following 24-bit values:
  * Simple Lit material: RGB **specular color** The color of a specular highlight.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#specularcolor) stored in 24 bits.
  * Lit material with metallic workflow: Reflectivity stored in 8 bits. The other 16 bits aren’t used.
  * Lit material with specular workflow: RGB specular color stored in 24 bits.


## Occlusion
This field contains the baked occlusion value from baked lighting. For realtime lighting, Unity calculates the **ambient occlusion** A method to approximate how much ambient light (light not coming from a specific direction) can hit a point on a surface.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Ambientocclusion) value by combining the baked occlusion value with the screen space ambient occlusion (SSAO) value.
## Normal
This field contains the world space normals encoded in 24 bits. For more information, refer to [Enable accurate G-buffer normals in the Deferred rendering path](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/rendering/accurate-g-buffer-normals.html).
## Smoothness
This field stores the smoothness value for the Simple Lit and Lit materials.
## Emissive/GI/Lighting
This render target contains the material emissive output and baked lighting. Unity fills this field during the G-buffer render pass. During the **deferred shading** A rendering path in the Built-in Render Pipeline that places no limit on the number of Lights that can affect a GameObject. All Lights are evaluated per-pixel, which means that they all interact correctly with normal maps and so on. Additionally, all Lights can have cookies and shadows. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/RenderTech-DeferredShading.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Deferredshading) pass, Unity stores lighting results in this render target.
The default format is `B10G11R11_UFloatPack32`.
Unity uses `R16G6B16A16_SFloat` if either of the following is true:
  * In the [URP Asset](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/universalrp-asset.html#quality), **Quality Settings** > **HDR** is enabled but the build platform doesn’t support HDR.
  * In the [Player settings window](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PlayerSettings.html), **PreserveFramebufferAlpha** is enabled.


If Unity can’t use `B10G11R11_UFloatPack32` or `R16G6B16A16_SFloat`, it uses the [default HDR format](https://docs.unity3d.com/ScriptReference/Experimental.Rendering.DefaultFormat.HDR.html). 
## ShadowMask
Unity adds this render target to the G-buffer layout when you set the [Lighting Mode](https://docs.unity3d.com/6000.0/Documentation/Manual/lighting-mode.html) to **Subtractive** or ****Shadowmask** A Texture that shares the same UV layout and resolution with its corresponding lightmap. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/lighting-mode.html#shadowmask)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shadowmask)**.
## Rendering Layer Mask
Unity adds this render target to the G-buffer layout when you enable [Rendering Layers](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/features/rendering-layers.html).
## Depth as Color
Unity adds this render target to the G-buffer layout when you enable Native Render Passes, and the platform supports them. Unity renders depth as a color into this render target. This render target has the following purpose:
  * Improves performance on Vulkan devices.
  * Lets Unity get the **depth buffer** A memory store that holds the z-value depth of each pixel in an image, where the z-value is the depth for each rendered pixel from the projection plane. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-RenderTexture.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#depthbuffer) on platforms that use the Metal graphics API, which doesn’t allow fetching the depth from the DepthStencil buffer within the same render pass.


The format of this render target is `GraphicsFormat.R32_SFloat`.
## DepthStencil
Unity reserves the four highest bits of this render target for the material type. For more information, refer to [URP ShaderLab Pass tags](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/urp-shaders/urp-shaderlab-pass-tags.html#universalmaterialtype).
The format of this render target is `D32F_S8` or `D24S8`, depending on the platform.
## Additional resources
  * [Render passes in the Deferred rendering path](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/rendering/render-passes-deferred.html)
  * [Rendering Layers performance](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/features/rendering-layers-introduction.html#performance)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/rendering/render-passes-deferred.html)
Render passes in the Deferred rendering path in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/rendering/accurate-g-buffer-normals.html)
Enable accurate G-buffer normals in the Deferred rendering path in URP
