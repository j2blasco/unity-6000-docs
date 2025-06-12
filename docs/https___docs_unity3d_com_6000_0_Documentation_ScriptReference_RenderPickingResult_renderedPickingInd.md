* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderPickingResult-renderedPickingIndexCount.html

#  [RenderPickingResult](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderPickingResult.html).renderedPickingIndexCount
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
renderedPickingIndexCount; 
### Description
The number of consecutive picking indices used during the current [RenderPickingCallback](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility.RenderPickingCallback.html).
If you return a [RenderPickingResult](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderPickingResult.html) struct with 0 count, the rendering is considered a [RenderPickingResult.NoOperation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderPickingResult.NoOperation.html) and the resolve callback is not called, even if you did render something.
* * *
