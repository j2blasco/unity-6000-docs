* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderPickingArgs.RenderObjectSetContains.html

#  [RenderPickingArgs](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderPickingArgs.html).RenderObjectSetContains
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
public bool RenderObjectSetContains([GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) go); 
### Parameters
Parameter | Description  
---|---  
go | The GameObject to test.  
### Returns
**bool** True if the GameObject is in either the ignore set or the filter set depending on [renderPickingType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderPickingArgs-renderPickingType.html). 
### Description
The function tests whether a GameObject is in the [RenderPickingArgs.renderObjectSet](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderPickingArgs-renderObjectSet.html).
* * *
