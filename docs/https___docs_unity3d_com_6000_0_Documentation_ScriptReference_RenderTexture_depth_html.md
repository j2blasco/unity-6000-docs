* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture-depth.html

#  [RenderTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.html).depth
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
depth; 
### Description
The precision of the render texture's depth buffer in bits (0, 16, 24 and 32 are supported).
Set the format of the Depth/Stencil buffer. The selected format depends on the available formats on the platform and the desired format for 24bit depth. See [GraphicsFormatUtility.GetDepthStencilFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.Rendering.GraphicsFormatUtility.GetDepthStencilFormat.html) for more information on how the format is selected.  
  
The property returns the actual number of bits for depth in the selected format. This can be different than the number of bits that was set if no format with that exact number of depth bits is available on the platform. [RenderTexture.depthStencilFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture-depthStencilFormat.html) returns the actual format that was selected.  
  
Set the format directly using [RenderTexture.depthStencilFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture-depthStencilFormat.html) if you need to control exactly what format is used.  
  
Additional resources: [format](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture-graphicsFormat.html), [width](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture-width.html), [height](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture-height.html).
* * *
