* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderTargetBinding-ctor.html

# RenderTargetBinding Constructor
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
public RenderTargetBinding([Rendering.RenderTargetIdentifier](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderTargetIdentifier.html) colorRenderTarget, [Rendering.RenderBufferLoadAction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderBufferLoadAction.html) colorLoadAction, [Rendering.RenderBufferStoreAction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderBufferStoreAction.html) colorStoreAction, [Rendering.RenderTargetIdentifier](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderTargetIdentifier.html) depthRenderTarget, [Rendering.RenderBufferLoadAction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderBufferLoadAction.html) depthLoadAction, [Rendering.RenderBufferStoreAction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderBufferStoreAction.html) depthStoreAction); 
## Declaration
public RenderTargetBinding(RenderTargetIdentifier[] colorRenderTargets, RenderBufferLoadAction[] colorLoadActions, RenderBufferStoreAction[] colorStoreActions, [Rendering.RenderTargetIdentifier](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderTargetIdentifier.html) depthRenderTarget, [Rendering.RenderBufferLoadAction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderBufferLoadAction.html) depthLoadAction, [Rendering.RenderBufferStoreAction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderBufferStoreAction.html) depthStoreAction); 
## Declaration
public RenderTargetBinding([RenderTargetSetup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTargetSetup.html) setup); 
### Parameters
Parameter | Description  
---|---  
color | Color buffers to use as render targets.  
depth | Depth buffer to use as render target.  
colorLoadAction | Load actions for color buffers.  
colorStoreAction | Store actions for color buffers.  
depthLoadAction | Load action for the depth/stencil buffer.  
depthStoreAction | Store action for the depth/stencil buffer.  
### Description
Constructs RenderTargetBinding.
* * *
