* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderTargetBinding.html

# RenderTargetBinding
struct in UnityEngine.Rendering
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
Describes a render target with one or more color buffers, a depth/stencil buffer and the associated load/store-actions that are applied when the render target is active.
This data structure is similiar to [RenderTargetSetup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTargetSetup.html), but relies on a [RenderTargetIdentifier](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderTargetIdentifier.html) to ensure compatability with [CommandBuffer.SetRenderTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.SetRenderTarget.html).  
  
To render to a specific mipmap level, cubemap face or depth slice the [RenderTargetIdentifier](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderTargetIdentifier.html) should be created accordingly.  
  
Note: the number of load- and store-actions specified for color buffers must be equal to the number of color buffers.  
  
Additional resources: [CommandBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.html).
### Properties
Property | Description  
---|---  
[colorLoadActions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderTargetBinding-colorLoadActions.html) | Load actions for color buffers.  
[colorRenderTargets](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderTargetBinding-colorRenderTargets.html) | Color buffers to use as render targets.  
[colorStoreActions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderTargetBinding-colorStoreActions.html) | Store actions for color buffers.  
[depthLoadAction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderTargetBinding-depthLoadAction.html) | Load action for the depth/stencil buffer.  
[depthRenderTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderTargetBinding-depthRenderTarget.html) | Depth/stencil buffer to use as render target.  
[depthStoreAction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderTargetBinding-depthStoreAction.html) | Store action for the depth/stencil buffer.  
[flags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderTargetBinding-flags.html) | Optional flags.  
### Constructors
Constructor | Description  
---|---  
[RenderTargetBinding](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderTargetBinding-ctor.html) | Constructs RenderTargetBinding.  
* * *
