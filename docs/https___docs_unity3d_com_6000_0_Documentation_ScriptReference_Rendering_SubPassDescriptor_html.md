* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.SubPassDescriptor.html

# SubPassDescriptor
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
Structure discribing a single native subpass.
### Properties
Property | Description  
---|---  
[colorOutputs](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.SubPassDescriptor-colorOutputs.html) | Array of attachment indices to be used as the color render targets in this sub pass. These are specificed as indices into the attachment array passed to CommandBuffer.BeginRenderPass.  
[flags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.SubPassDescriptor-flags.html) | Flags controlling specific reading behaviour of depth and stencil attachments.  
[inputs](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.SubPassDescriptor-inputs.html) | Array of attachment indices to be used as input attachments in this sub pass. These are specificed as indices into the attachment array passed to CommandBuffer.BeginRenderPass.  
* * *
