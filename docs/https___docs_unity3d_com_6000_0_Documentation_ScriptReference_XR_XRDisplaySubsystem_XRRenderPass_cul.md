* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRDisplaySubsystem.XRRenderPass-cullingPassIndex.html

#  [XRDisplaySubsystem.XRRenderPass](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRDisplaySubsystem.XRRenderPass.html).cullingPassIndex
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
cullingPassIndex; 
### Description
An index that a render pipeline can pass to [XRDisplaySubsystem.GetCullingParameters](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRDisplaySubsystem.GetCullingParameters.html) to obtain culling information.
Multiple [render passes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRDisplaySubsystem.XRRenderPass.html) can share the same index. This means that the renderer only needs to cull once, and can reuse the result of the culling for all render passes that use the same index.
* * *
