* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRDisplaySubsystem.AddGraphicsThreadMirrorViewBlit.html

#  [XRDisplaySubsystem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRDisplaySubsystem.html).AddGraphicsThreadMirrorViewBlit
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
**Obsolete** AddGraphicsThreadMirrorViewBlit(CommandBuffer, bool) is deprecated. Use AddGraphicsThreadMirrorViewBlit(CommandBuffer, bool, int) instead.
## Declaration
public bool AddGraphicsThreadMirrorViewBlit([Rendering.CommandBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.html) cmd, bool allowGraphicsStateInvalidate); 
## Declaration
public bool AddGraphicsThreadMirrorViewBlit([Rendering.CommandBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.html) cmd, bool allowGraphicsStateInvalidate, int mode); 
### Parameters
Parameter | Description  
---|---  
cmd | The target [CommandBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.html) that records the native blit event.  
allowGraphicsStateInvalidate | True causes the graphics device to invalidate internal states before and after calling into the provider's native blit. This ensures the GFX internal states' consistency with the cost of some runtime performance.  
mode | The [XRMirrorViewBlitMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRMirrorViewBlitMode.html) XR display should perform.  
### Returns
**bool** Returns true if native blit event is successfully recorded. Returns false otherwise. 
### Description
This function records the display subsystem's native blit event to the target command buffer. This function is typically called by a scriptable rendering pipeline.
* * *
