* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.DrawRendererList.html

#  [CommandBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.html).DrawRendererList
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
public void DrawRendererList([Rendering.RendererList](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RendererList.html) rendererList); 
### Parameters
Parameter | Description  
---|---  
rendererList | The RendererList to draw.  
### Description
Adds a "draw renderer list" command.
This command schedules the drawing of visible GameObjects in a RendererList. To create a RendererList, see [ScriptableRenderContext.CreateRendererList](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ScriptableRenderContext.CreateRendererList.html).
* * *
