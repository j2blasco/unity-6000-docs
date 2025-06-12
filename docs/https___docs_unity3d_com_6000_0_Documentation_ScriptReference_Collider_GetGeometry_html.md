* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.GetGeometry.html

#  [Collider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html).GetGeometry
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
## Declaration
public T GetGeometry(); 
### Returns
**T** Type of geometrical shape. 
### Description
Returns the geometric shape of the collider of the requested type.
Throws an InvalidOperationException if you request a shape that is not present in the collider. Additional resources: [BoxGeometry](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LowLevelPhysics.BoxGeometry.html), [SphereGeometry](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LowLevelPhysics.SphereGeometry.html), [CapsuleGeometry](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LowLevelPhysics.CapsuleGeometry.html), [ConvexMeshGeometry](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LowLevelPhysics.ConvexMeshGeometry.html), [TriangleMeshGeometry](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LowLevelPhysics.TriangleMeshGeometry.html), [TerrainGeometry](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LowLevelPhysics.TerrainGeometry.html).
* * *
