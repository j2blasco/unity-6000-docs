* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ShadowDrawingSettings-batchLayerMask.html

#  [ShadowDrawingSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ShadowDrawingSettings.html).batchLayerMask
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
batchLayerMask; 
### Description
Unity renders objects whose [BatchFilterSettings.batchLayer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchFilterSettings-batchLayer.html) value is enabled in this bit mask.
Unity renders the object if you enable the [BatchFilterSettings.batchLayer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchFilterSettings-batchLayer.html) value in this bit mask. You can use [BatchFilterSettings.batchLayer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchFilterSettings-batchLayer.html) to specify a batch layer in each [BatchDrawRange](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchDrawRange.html).  
  
Objects that are not rendered using [BatchRendererGroup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchRendererGroup.html) are in batch layer `0`, so you can use bit 0 of `batchLayerMask` to control whether they're included in this renderer list.
* * *
