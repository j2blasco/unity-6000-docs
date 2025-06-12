* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ScriptableRenderContext.CreateWireOverlayRendererList.html

#  [ScriptableRenderContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ScriptableRenderContext.html).CreateWireOverlayRendererList
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
public [Rendering.RendererList](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RendererList.html) CreateWireOverlayRendererList([Camera](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html) camera); 
### Parameters
Parameter | Description  
---|---  
camera | The camera that is used for rendering the WireOverlay.  
### Returns
**RendererList** Returns a new RendererList based on the settings you pass in. 
### Description
Creates a new WireOverlay [RendererList](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RendererList.html).
A [RendererList](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RendererList.html) represents a set of draw commands. To draw the WireOverlay in a RendererList, add the [CommandBuffer.DrawRendererList](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.DrawRendererList.html) command to a [CommandBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.html).
* * *
