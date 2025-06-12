* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RayTracingSubMeshFlags.Enabled.html

#  [RayTracingSubMeshFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RayTracingSubMeshFlags.html).Enabled
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
The sub-mesh is provided as input to a [RayTracingAccelerationStructure](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RayTracingAccelerationStructure.html) build operation.
Unity does not consider a sub-mesh opaque if this is the only flag it has, and allows the GPU to invoke a user-defined any hit shader when a ray intersects with that sub-mesh. This can potentially impact GPU performance during acceleration structure traversal.
* * *
