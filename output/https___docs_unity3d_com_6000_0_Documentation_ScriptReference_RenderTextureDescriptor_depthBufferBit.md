* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTextureDescriptor-depthBufferBits.html

#  [RenderTextureDescriptor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTextureDescriptor.html).depthBufferBits
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
depthBufferBits; 
### Description
The precision of the render texture's depth buffer in bits (0, 16, 24 and 32 are supported).
The minimum number of bits used for depth in the Depth/Stencil buffer format.  
  
The actual format of the depth/stencil buffer that is selected based on the given number of bits can be different per platform or graphics API. Read more about the decision tree here Additional resources: [RenderTexture.depth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture-depth.html). Additional resources: [RenderTexture.depthStencilFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture-depthStencilFormat.html) returns the actual format that was selected.  
  
The property returns the actual number of bits for depth in the selected format. This can be different than the number of bits that was set if no format with that exact number of depth bits is available on the platform.
* * *
