* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture-depthStencilFormat.html

#  [RenderTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.html).depthStencilFormat
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-RenderTexture.html "Go to RenderTexture Component in the Manual")
[Experimental.Rendering.GraphicsFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.Rendering.GraphicsFormat.html) depthStencilFormat; 
### Description
The format of the depth/stencil buffer.
The returned format is the actual format that is used when [RenderTexture.Create](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.Create.html) is called. This format can be different than the depth/stencil format that was set on the RenderTexture if that format is not supported on the current platform or graphics API. RenderTexture will automatically try to use a compatible format with more bits. If the format is not supported and when no compatible format is found on this platform then the original format will be returned. This fallback to a compatible format can be disabled on a RenderTexture asset in the inspector.  
  
Additional resources: [RenderTexture.depth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture-depth.html), [RenderTextureDescriptor.depthStencilFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTextureDescriptor-depthStencilFormat.html), [GraphicsFormatUtility.GetDepthStencilFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.Rendering.GraphicsFormatUtility.GetDepthStencilFormat.html), [GraphicsFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.Rendering.GraphicsFormat.html). 
* * *
