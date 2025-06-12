* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderBufferLoadAction.html

# RenderBufferLoadAction
enumeration
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
This enum describes what should be done on the render target when it is activated (loaded).
When the GPU starts rendering into a render target, this setting specifies the action that should be performed on the existing contents of the surface. Tile-based GPUs may get performance advantage if the load action is Clear or DontCare. The user should avoid using RenderBufferLoadAction.Load whenever possible.  
  
Please note that not all platforms have load/store actions, so this setting might be ignored at runtime. Generally mobile-oriented graphics APIs (OpenGL ES, Metal) take advantage of these settings.  
  
If you use `RenderBufferLoadAction.DontCare`, rendering might fail or produce artefacts because undefined pixels in the [depth texture](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-CameraDepthTexture.html) cause depth testing to fail. You can use [LoadStoreActionDebugModeSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.LoadStoreActionDebugModeSettings.html) to highlight undefined pixels. 
### Properties
Property | Description  
---|---  
[Load](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderBufferLoadAction.Load.html) | When this RenderBuffer is activated, preserve the existing contents of it. This setting is expensive on tile-based GPUs and should be avoided whenever possible.  
[Clear](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderBufferLoadAction.Clear.html) | Upon activating the render buffer, clear its contents. Currently only works together with the RenderPass API.  
[DontCare](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderBufferLoadAction.DontCare.html) | When this RenderBuffer is activated, the GPU is instructed not to care about the existing contents of that RenderBuffer. On tile-based GPUs this means that the RenderBuffer contents do not need to be loaded into the tile memory, providing a performance boost.  
* * *
