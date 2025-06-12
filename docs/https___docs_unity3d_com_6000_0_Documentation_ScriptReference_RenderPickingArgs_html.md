* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderPickingArgs.html

# RenderPickingArgs
struct in UnityEditor
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
Provides information about what is expected to render during the current picking rendering callback.
### Properties
Property | Description  
---|---  
[pickingIndex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderPickingArgs-pickingIndex.html) | Specifies the picking index value that the first pickable object uses to write to the picking render texture.  
[renderObjectSet](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderPickingArgs-renderObjectSet.html) | A set of GameObjects to check and determine what this callback is expected to render.  
[renderPickingType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderPickingArgs-renderPickingType.html) | Specifies the type of the current picking rendering the callback is invoked with.  
### Public Methods
Method | Description  
---|---  
[NeedToRenderForPicking](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderPickingArgs.NeedToRenderForPicking.html) | Checks whether a GameObject should be rendered in the current render picking callback.  
[RenderObjectSetContains](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderPickingArgs.RenderObjectSetContains.html) | The function tests whether a GameObject is in the RenderPickingArgs.renderObjectSet.  
* * *
