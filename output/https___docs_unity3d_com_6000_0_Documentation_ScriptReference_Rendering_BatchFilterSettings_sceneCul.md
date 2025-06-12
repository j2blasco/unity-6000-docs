* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchFilterSettings-sceneCullingMask.html

#  [BatchFilterSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchFilterSettings.html).sceneCullingMask
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
sceneCullingMask; 
### Description
Use this bit mask to discard the draw commands in a particular context. A draw command is not discarded if the expression `(1 << layer) & sceneCullingMask` is true. This field is typically used when rendering Editor previews.
* * *
