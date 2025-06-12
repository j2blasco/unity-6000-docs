* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTextureDescriptor.html

# RenderTextureDescriptor
struct in UnityEngine
/
Implemented in:[UnityEngine.CoreModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.CoreModule.html)
Leave feedback
Suggest a change
## Success!
Thank you for helping us improve the quality of Unity Documentation. Although we cannot accept all submissions, we do read each suggested change from our users and will make updates where applicable.
Close
## Submission failed
For some reason your suggested change could not be submitted. Please <a>try again</a> in a few minutes. And thank you for taking the time to help us improve the quality of Unity Documentation.
Close
Your name Your email Suggestion* Submit suggestion
Cancel
### Description
This struct contains all the information required to create a RenderTexture. It can be copied, cached, and reused to easily create RenderTextures that all share the same properties. Avoid using the default constructor as it does not initialize some flags with the recommended values.
### Properties
Property | Description  
---|---  
[autoGenerateMips](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTextureDescriptor-autoGenerateMips.html) | Mipmap levels are generated automatically when this flag is set.  
[bindMS](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTextureDescriptor-bindMS.html) | If true and msaaSamples is greater than 1, the render texture will not be resolved by default. Use this if the render texture needs to be bound as a multisampled texture in a shader.  
[colorFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTextureDescriptor-colorFormat.html) | The format of the RenderTarget is expressed as a RenderTextureFormat. Internally, this format is stored as a GraphicsFormat compatible with the current system (see SystemInfo.GetCompatibleFormat). Therefore, if you set a format and immediately get it again, it may return a different result from the one just set.  
[depthBufferBits](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTextureDescriptor-depthBufferBits.html) | The precision of the render texture's depth buffer in bits (0, 16, 24 and 32 are supported).  
[depthStencilFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTextureDescriptor-depthStencilFormat.html) | The desired format of the depth/stencil buffer.  
[dimension](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTextureDescriptor-dimension.html) | Dimensionality (type) of the render texture.Additional resources: RenderTexture.dimension.  
[enableRandomWrite](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTextureDescriptor-enableRandomWrite.html) | Enable random access write into this render texture on Shader Model 5.0 level shaders.Additional resources: RenderTexture.enableRandomWrite.  
[flags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTextureDescriptor-flags.html) | A set of RenderTextureCreationFlags that control how the texture is created.  
[graphicsFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTextureDescriptor-graphicsFormat.html) | The color format for the RenderTexture. You can set this format to None to achieve depth-only rendering.  
[height](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTextureDescriptor-height.html) | The height of the render texture in pixels.  
[memoryless](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTextureDescriptor-memoryless.html) | The render texture memoryless mode property.  
[mipCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTextureDescriptor-mipCount.html) | User-defined mipmap count.  
[msaaSamples](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTextureDescriptor-msaaSamples.html) | The multisample antialiasing level for the RenderTexture.Additional resources: RenderTexture.antiAliasing.  
[shadowSamplingMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTextureDescriptor-shadowSamplingMode.html) | Determines how the RenderTexture is sampled if it is used as a shadow map.Additional resources: ShadowSamplingMode for more details.  
[sRGB](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTextureDescriptor-sRGB.html) | This flag causes the render texture uses sRGB read/write conversions.  
[stencilFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTextureDescriptor-stencilFormat.html) | The format of the stencil data that you can encapsulate within a RenderTexture.Specifying this property creates a stencil element for the RenderTexture and sets its format. This allows for stencil data to be bound as a Texture to all shader types for the platforms that support it. This property does not specify the format of the stencil buffer, which is constrained by the depth buffer format specified in RenderTexture.depth.Currently, most platforms only support R8_UInt (DirectX11, DirectX12).  
[useDynamicScale](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTextureDescriptor-useDynamicScale.html) | Set to true to enable dynamic resolution scaling on this render texture. Mutually exclusive with RenderTextureDescriptor.useDynamicScaleExplicitAdditional resources: RenderTexture.useDynamicScale.  
[useDynamicScaleExplicit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTextureDescriptor-useDynamicScaleExplicit.html) | Set to true to enable dynamic resolution scaling on this render texture and control when this scaling happens. Mutually exclusive with RenderTextureDescriptor.useDynamicScaleAdditional resources: RenderTexture.useDynamicScaleExplicit.  
[useMipMap](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTextureDescriptor-useMipMap.html) | Render texture has mipmaps when this flag is set.Additional resources: RenderTexture.useMipMap.  
[volumeDepth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTextureDescriptor-volumeDepth.html) | Volume extent of a 3D render texture.  
[vrUsage](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTextureDescriptor-vrUsage.html) | If this RenderTexture is a VR eye texture used in stereoscopic rendering, this property decides what special rendering occurs, if any. Instead of setting this manually, use the value returned by eyeTextureDesc or other VR functions returning a RenderTextureDescriptor.  
[width](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTextureDescriptor-width.html) | The width of the render texture in pixels.  
### Constructors
Constructor | Description  
---|---  
[RenderTextureDescriptor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTextureDescriptor-ctor.html) | Create a RenderTextureDescriptor with default values, or a certain width, height, and format.  
* * *
