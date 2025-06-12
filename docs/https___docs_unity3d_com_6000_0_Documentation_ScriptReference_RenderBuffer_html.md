* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderBuffer.html

# RenderBuffer
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
Color or depth buffer part of a [RenderTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.html).
A single [RenderTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.html) object represents both color and depth buffers, but many complex rendering algorithms require using the same depth buffer with multiple color buffers or vice versa.  
  
This class represents either a color or a depth buffer part of a RenderTexture.  
  
Additional resources: [RenderTexture.colorBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture-colorBuffer.html), [RenderTexture.depthBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture-depthBuffer.html), [Graphics.activeColorBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics-activeColorBuffer.html), [Graphics.activeDepthBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics-activeDepthBuffer.html), [Graphics.SetRenderTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.SetRenderTarget.html).
### Public Methods
Method | Description  
---|---  
[GetNativeRenderBufferPtr](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderBuffer.GetNativeRenderBufferPtr.html) | Returns native RenderBuffer. Be warned this is not native Texture, but rather pointer to unity struct that can be used with native unity API. Currently such API exists only on iOS.  
* * *
