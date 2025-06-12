* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchFilterSettings.html

# BatchFilterSettings
struct in UnityEngine.Rendering
/
Implemented in:[UnityEngine.CoreModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.CoreModule.html)
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
Represents settings that Unity applies to draw commands in this [draw range](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchDrawRange.html).
For more information, see [BatchRendererGroup](https://docs.unity3d.com/6000.0/Documentation/Manual/batch-renderer-group.html).
### Properties
Property | Description  
---|---  
[allDepthSorted](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchFilterSettings-allDepthSorted.html) | Indicates whether all draw commands in the current draw range have the BatchDrawCommandFlags.HasSortingPosition flag set.  
[batchLayer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchFilterSettings-batchLayer.html) | The batch layer to use for draw commands in this draw range.  
[layer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchFilterSettings-layer.html) | The layer to use for draw commands in this draw range.  
[motionMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchFilterSettings-motionMode.html) | Specifies how to generate motion vectors in this draw range.  
[receiveShadows](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchFilterSettings-receiveShadows.html) | Indicates whether instances from draw commands in this draw range should receive shadows.  
[rendererPriority](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchFilterSettings-rendererPriority.html) | The sorting priority to use for draw commands in this draw range.  
[renderingLayerMask](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchFilterSettings-renderingLayerMask.html) | The rendering layer mask to use for draw commands in this draw range.  
[sceneCullingMask](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchFilterSettings-sceneCullingMask.html) | Use this bit mask to discard the draw commands in a particular context. A draw command is not discarded if the expression (1 << layer) & sceneCullingMask is true. This field is typically used when rendering Editor previews.  
[shadowCastingMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchFilterSettings-shadowCastingMode.html) | Specifies how instances from the draw commands in this draw range cast shadows.  
[staticShadowCaster](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchFilterSettings-staticShadowCaster.html) | Indicates whether instances from the draw commands in this draw range render into cached shadow maps.  
* * *
