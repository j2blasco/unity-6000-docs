* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderPickingResult-resolver.html

#  [RenderPickingResult](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderPickingResult.html).resolver
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
[HandleUtility.ResolvePickingCallback](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility.ResolvePickingCallback.html) resolver; 
### Description
The callback to invoke to resolve a picking index into a GameObject reference.
The callback is invoked only if one of the picking indices rendered ends up being the topmost one under the mouse click position.  
  
The callback is provided with a local picking index: the 0-based index that is offset from picking indices you used for rendering by subtracting [RenderPickingArgs.pickingIndex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderPickingArgs-pickingIndex.html).  
  
The callback returns a [GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) reference from the given arguments. If you need more contextual data for the resolve callback to work, you can construct the callback as a lambda function from the render callback so that you can capture variables such as `pickingIndex` into it.  
  
Returns null if the picking index doesn't resolve to any GameObject. This signals Unity to end the picking loop (for finding all objects under the mouse) and to start over.  
  
Additional resources: [RenderPickingResult.resolverWithWorldPos](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderPickingResult-resolverWithWorldPos.html).
* * *
