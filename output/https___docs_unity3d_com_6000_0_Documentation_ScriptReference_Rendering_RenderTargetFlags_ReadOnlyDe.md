* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderTargetFlags.ReadOnlyDepthStencil.html

#  [RenderTargetFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderTargetFlags.html).ReadOnlyDepthStencil
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
Both depth and stencil buffers bound for rendering may be bound as samplable textures to the graphics pipeline: some platforms require the depth and stencil buffers to be set to read-only mode in such cases (D3D11, Vulkan). This flag can be used for both packed depth-stencil as well as separate depth-stencil formats. This flag is a bitwise combination of [RenderTargetFlags.ReadOnlyDepth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderTargetFlags.ReadOnlyDepth.html) and [RenderTargetFlags.ReadOnlyStencil](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderTargetFlags.ReadOnlyStencil.html).
* * *
