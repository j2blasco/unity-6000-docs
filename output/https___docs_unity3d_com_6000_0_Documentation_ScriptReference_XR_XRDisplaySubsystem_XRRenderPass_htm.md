* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRDisplaySubsystem.XRRenderPass.html

# XRRenderPass
struct in UnityEngine.XR
/
Implemented in:[UnityEngine.XRModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.XRModule.html)
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
Contains configuration parameters about which view into the Scene the renderer should rasterize, and a render target (which can be a texture array) for the result of the rasterization.
An XRRenderPass can contain more than one [XRRenderParameter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRDisplaySubsystem.XRRenderParameter.html) (viewpoints that the render pipeline renders to the output texture as either different viewports or texture array slices). The render pipeline must query each child [XRRenderParameter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRDisplaySubsystem.XRRenderParameter.html) via [GetRenderParameter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRDisplaySubsystem.XRRenderPass.GetRenderParameter.html). The most optimal way to implement an XRRenderPass is to cull first, and then submit draw calls once for the resulting objects. You can also use techniques such as instanced rendering to optimize XRRenderPasses that contain more than one [XRRenderParameter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRDisplaySubsystem.XRRenderParameter.html).  
  
XRRenderPass is typically consumed by a scriptable rendering pipeline.
### Properties
Property | Description  
---|---  
[cullingPassIndex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRDisplaySubsystem.XRRenderPass-cullingPassIndex.html) | An index that a render pipeline can pass to XRDisplaySubsystem.GetCullingParameters to obtain culling information.  
[foveatedRenderingInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRDisplaySubsystem.XRRenderPass-foveatedRenderingInfo.html) | A pointer to a native struct containing platform-specific data for foveated rendering.  
[hasMotionVectorPass](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRDisplaySubsystem.XRRenderPass-hasMotionVectorPass.html) | A boolean indicating if this render pass contains a motion-vector generation pass.  
[motionVectorRenderTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRDisplaySubsystem.XRRenderPass-motionVectorRenderTarget.html) | The output render-texture target for the motion-vector generation render pass.  
[motionVectorRenderTargetDesc](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRDisplaySubsystem.XRRenderPass-motionVectorRenderTargetDesc.html) | The render texture description for the target texture for the motion-vector render pass.  
[renderPassIndex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRDisplaySubsystem.XRRenderPass-renderPassIndex.html) | The index of the render pass (originally passed in to XRDisplaySubsystem.GetRenderPass).  
[renderTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRDisplaySubsystem.XRRenderPass-renderTarget.html) | The output target for the render pass.  
[renderTargetDesc](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRDisplaySubsystem.XRRenderPass-renderTargetDesc.html) | Descriptor that can be passed to RenderTexture.GetTemporary to create temporary textures that match the XR Display render target.  
[shouldFillOutDepth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRDisplaySubsystem.XRRenderPass-shouldFillOutDepth.html) | When this is false an optimal renderer can avoid resolving the depth buffer.  
### Public Methods
Method | Description  
---|---  
[GetRenderParameter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRDisplaySubsystem.XRRenderPass.GetRenderParameter.html) | Gets an XRRenderParameter for a specific XRRenderPass.  
[GetRenderParameterCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRDisplaySubsystem.XRRenderPass.GetRenderParameterCount.html) | The number of XRRenderParameter entries for this XRRenderPass.  
* * *
