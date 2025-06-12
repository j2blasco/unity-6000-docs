* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.SetRenderTarget.html

#  [Graphics](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.html).SetRenderTarget
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
## Declaration
public static void SetRenderTarget([RenderTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.html) rt, int mipLevel = 0, [CubemapFace](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CubemapFace.html) face = CubemapFace.Unknown, int depthSlice = 0); 
## Declaration
public static void SetRenderTarget([Rendering.GraphicsTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsTexture.html) rt, int mipLevel = 0, [CubemapFace](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CubemapFace.html) face = CubemapFace.Unknown, int depthSlice = 0); 
## Declaration
public static void SetRenderTarget(RenderBuffer[] colorBuffers, [RenderBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderBuffer.html) depthBuffer); 
## Declaration
public static void SetRenderTarget([RenderBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderBuffer.html) colorBuffer, [RenderBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderBuffer.html) depthBuffer, int mipLevel = 0, [CubemapFace](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CubemapFace.html) face = CubemapFace.Unknown, int depthSlice = 0); 
## Declaration
public static void SetRenderTarget([RenderTargetSetup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTargetSetup.html) setup); 
### Parameters
Parameter | Description  
---|---  
rt |  [RenderTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.html) or [GraphicsTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsTexture.html) to set as active render target.  
mipLevel | Mipmap level to render into (use 0 if not mipmapped).  
face | Cubemap face to render into (use Unknown if not a cubemap).  
depthSlice | Depth slice to render into (use 0 if not a 3D or 2DArray render target).  
colorBuffer | Color buffer to render into.  
depthBuffer | Depth buffer to render into.  
colorBuffers | Color buffers to render into (for multiple render target effects).  
setup | Full render target setup information.  
### Description
Sets current render target.
This function sets which [RenderTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.html), [GraphicsTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsTexture.html), or a [RenderBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderBuffer.html) combination will be rendered into next. Use it when implementing custom rendering algorithms, where you need to render something into a render target texture manually.  
  
Variants with mipLevel and face arguments enable rendering into a specific mipmap level of a texture, or specific cubemap face of a cubemap RenderTexture/GraphicsTexture. Variants with depthSlice allow rendering into a specific slice of a 3D or 2DArray render texture.  
  
The function call with colorBuffers array enables techniques that use Multiple Render Targets (MRT), where fragment shader can output more than one final color.  
  
Calling SetRenderTarget with just a RenderTexture or GraphicsTexture argument is the same as setting the [RenderTexture.active](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture-active.html) and [GraphicsTexture.active](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsTexture-active.html) property. To set a GraphicsTexture as the render target, it must have GraphicsTextureDescFlags.RenderTarget enabled in GraphicsTexture.descriptor.flags.  
  
Note that in Linear color space, it is important to have the correct sRGB<->Linear color conversion state set. Depending on what was rendered previously, the current state might not be the one you expect. You should consider setting [GL.sRGBWrite](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL-sRGBWrite.html) as you need it before doing SetRenderTarget or any other manual rendering.  
  
Additional resources: [RenderTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.html), [GraphicsTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsTexture.html), [Graphics.activeColorBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics-activeColorBuffer.html), [Graphics.activeDepthBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics-activeDepthBuffer.html), [SystemInfo.supportedRenderTargetCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-supportedRenderTargetCount.html).
* * *
