* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderPickingArgs.NeedToRenderForPicking.html

#  [RenderPickingArgs](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderPickingArgs.html).NeedToRenderForPicking
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
public bool NeedToRenderForPicking([GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) go); 
### Parameters
Parameter | Description  
---|---  
go | The GameObject to test.  
### Returns
**bool** True if the GameObject should be rendered. 
### Description
Checks whether a GameObject should be rendered in the current render picking callback.
`RenderPickingArgs.NeedToRenderForPicking` is similar to [RenderObjectSetContains](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderPickingArgs.RenderObjectSetContains.html). This method checks whether a GameObject should be rendered or not.  
  
If the current [renderPickingType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderPickingArgs-renderPickingType.html) is [RenderPickingType.RenderFromIgnoreSet](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderPickingType.RenderFromIgnoreSet.html), this method returns true if the given `go` is not contained in the ignore set. Otherwise, this method returns true if the given `go` is contained in the filter set.  
  
Notice that for the [RenderPickingType.RenderFromIgnoreSet](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderPickingType.RenderFromIgnoreSet.html) type, this method returns true for all GameObjects if it is not contained in the ignore set. However, you are only required to handle the rendering of the custom geometries your callback is set to render.
* * *
