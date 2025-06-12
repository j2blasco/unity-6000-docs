* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchFilterSettings-allDepthSorted.html

#  [BatchFilterSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchFilterSettings.html).allDepthSorted
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
allDepthSorted; 
### Description
Indicates whether all draw commands in the current draw range have the [BatchDrawCommandFlags.HasSortingPosition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchDrawCommandFlags.HasSortingPosition.html) flag set.
Set this to `true` if all the draw commands have the flag set, and `false` otherwise. As an optimization, Unity can efficiently skip the rendering of the entire draw range when this is true and the render pass is not depth sorted. Otherwise, Unity must check every draw command inside the range separately for the flag.
* * *
