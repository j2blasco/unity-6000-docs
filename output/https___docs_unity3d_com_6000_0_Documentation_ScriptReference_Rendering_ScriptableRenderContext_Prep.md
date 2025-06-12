* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ScriptableRenderContext.PrepareRendererListsAsync.html

#  [ScriptableRenderContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ScriptableRenderContext.html).PrepareRendererListsAsync
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
public void PrepareRendererListsAsync(List<RendererList> rendererLists); 
### Parameters
Parameter | Description  
---|---  
rendererLists | The list of RendererList objects to prepare for rendering.  
### Description
Starts to process the provided RendererLists in the background.
With this command, an application can manually start the batch processing and filtering of the visible GameObjects. It is an asynchronous operation and the control returns immediately to the application. To check the status for each RendererList, use ScriptableRenderContext.QueryRendererList.  
  
If you do not use this command, then the batch processing of RendererLists begins with [ScriptableRenderContext.Submit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ScriptableRenderContext.Submit.html). By using this command, the application can start the processing of a number of RendererLists manually at the beginning of a frame, before recording any other rendering commands. This enables RendererList processing to overlap with other work, which improves performance.  
  
Furthermore, by using the [ScriptableRenderContext.QueryRendererListStatus](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ScriptableRenderContext.QueryRendererListStatus.html) command, the application can get information about the type of visible objects in the scene and optimize rendering accordingly (for example by skipping a color pyramid generation pass if no objects with distortion are visible).
* * *
