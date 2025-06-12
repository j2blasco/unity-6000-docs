* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderPickingArgs-renderObjectSet.html

#  [RenderPickingArgs](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderPickingArgs.html).renderObjectSet
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
renderObjectSet; 
### Description
A set of GameObjects to check and determine what this callback is expected to render.
Depending on [renderPickingType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderPickingArgs-renderPickingType.html), the GameObjects in this set are expected to be either included or excluded from the picking rendering. Refer to [renderPickingType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderPickingArgs-renderPickingType.html).  
  
This set cannot be null, but it can be empty. Use [RenderObjectSetContains](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderPickingArgs.RenderObjectSetContains.html) to query whether a GameObject is contained in the set.
* * *
