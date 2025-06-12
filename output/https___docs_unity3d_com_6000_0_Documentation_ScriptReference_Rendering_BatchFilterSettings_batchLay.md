* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchFilterSettings-batchLayer.html

#  [BatchFilterSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchFilterSettings.html).batchLayer
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
batchLayer; 
### Description
The batch layer to use for draw commands in this draw range.
Use `batchLayer` to control which ranges Unity draws in a renderer list or shadow renderer list, based on [FilteringSettings.batchLayerMask](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.FilteringSettings-batchLayerMask.html) or [ShadowDrawingSettings.batchLayerMask](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ShadowDrawingSettings-batchLayerMask.html).  
  
Objects that are not rendered using [BatchRendererGroup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchRendererGroup.html) are in batch layer `0`.
* * *
