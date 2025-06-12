* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderPickingArgs-renderPickingType.html

#  [RenderPickingArgs](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderPickingArgs.html).renderPickingType
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
[RenderPickingType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderPickingType.html) renderPickingType; 
### Description
Specifies the type of the current picking rendering the callback is invoked with.
Unity picking rendering is categorized into two types that have two different purposes. Your rendering must adhere to this type specification. Those types are: 
  * [RenderPickingType.RenderFromIgnoreSet](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderPickingType.RenderFromIgnoreSet.html): Render from an ignore set, also known as an exclusion set, of GameObjects. This is the main rendering mode. You must render all your custom geometries, except for those whose representing GameObjects are in the ignore set. You can query this information with [RenderObjectSetContained](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderPickingArgs.RenderObjectSetContained.html).
  * [RenderPickingType.RenderFromFilterSet](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderPickingType.RenderFromFilterSet.html): Render from a filter set, also known as an inclusion set, of GameObjects. Unity uses this rendering mode to verify that a GameObject is still pickable under a new mouse click position. You must only render custom geometries whose representing GameObjects are in the filter set. You can query this information with [RenderObjectSetContained](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderPickingArgs.RenderObjectSetContained.html).


Additional resources: [RenderObjectSetContains](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderPickingArgs.RenderObjectSetContains.html).
* * *
