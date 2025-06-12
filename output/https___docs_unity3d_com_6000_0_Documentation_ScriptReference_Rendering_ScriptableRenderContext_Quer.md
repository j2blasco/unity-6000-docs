* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ScriptableRenderContext.QueryRendererListStatus.html

#  [ScriptableRenderContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ScriptableRenderContext.html).QueryRendererListStatus
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
public [Rendering.RendererListStatus](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RendererListStatus.html) QueryRendererListStatus([Rendering.RendererList](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RendererList.html) rendererList); 
### Parameters
Parameter | Description  
---|---  
rendererList | The RendererList to query.  
### Returns
**RendererListStatus** Returns the status of the RendererList. 
### Description
Queries the status of a [RendererList](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RendererList.html).
You can use this command to expose information about the visible GameObjects before recording any rendering commands in a command buffer. For example, by querying the status of a RendererList that includes only transparent GameObjects, the application can know if any transparent GameObjects are visible in the current view and, if not, skip the setup of any rendering passes required to draw them.  
  
Before querying a RendererList for its status, the application should first call [ScriptableRenderContext.PrepareRendererListsAsync](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ScriptableRenderContext.PrepareRendererListsAsync.html).
* * *
