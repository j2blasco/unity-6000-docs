* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchCullingContext.html

# BatchCullingContext
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
Culling context for a batch.
Specifies the data required to perform culling. Additional resources: [OnPerformCulling](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchRendererGroup.OnPerformCulling.html).
### Properties
Property | Description  
---|---  
[cullingFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchCullingContext-cullingFlags.html) | Additional culling information for the current context.  
[cullingLayerMask](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchCullingContext-cullingLayerMask.html) | The cullingLayerMask value of the object from which the culling is invoked. The draw command is discarded by the internal culling if the expression (1 << layer) & cullingLayerMask is false. Using this field is optional, use it for performance or other optimization purposes.  
[cullingPlanes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchCullingContext-cullingPlanes.html) | Planes to cull against.  
[cullingSplits](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchCullingContext-cullingSplits.html) | The array of CullingSplit structs.  
[localToWorldMatrix](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchCullingContext-localToWorldMatrix.html) | Local to world matrix.  
[lodParameters](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchCullingContext-lodParameters.html) | Additional resources: LODParameters.  
[projectionType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchCullingContext-projectionType.html) | The projection of the view from which the culling is invoked. Usage example: take different culling paths for orthographic vs perspective views.  
[receiverPlaneCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchCullingContext-receiverPlaneCount.html) | The number of receiver planes.  
[receiverPlaneOffset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchCullingContext-receiverPlaneOffset.html) | The index of the first receiver plane in the BatchCullingContext.cullingPlanes array.  
[sceneCullingMask](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchCullingContext-sceneCullingMask.html) | Use this bit mask to discard the draw commands in a particular context. A draw command is not discarded if the expression (1 << layer) & sceneCullingMask is true. This field is typically used when rendering Editor previews.  
[splitExclusionMask](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchCullingContext-splitExclusionMask.html) | A bitmask that represents the BatchCullingContext.cullingSplits Unity ignores in a BatchDrawCommand struct.  
[viewID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchCullingContext-viewID.html) | The ID of the object from which the culling is invoked. Usage example: store culling-related data for each object.  
[viewType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchCullingContext-viewType.html) | The type of the view from which the culling is invoked. Usage examples: skip culling, take different culling paths depending on the view type, etc.  
* * *
