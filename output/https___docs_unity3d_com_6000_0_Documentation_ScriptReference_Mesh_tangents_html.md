* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh-tangents.html

#  [Mesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html).tangents
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Mesh.html "Go to Mesh Component in the Manual")
tangents; 
### Description
The tangents of the Mesh.
Tangents are mostly used in bump-mapped Shaders. A tangent is a unit-length vector that follows Mesh surface along horizontal (U) texture direction. Tangents in Unity are represented as [Vector4](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector4.html), with _x,y,z_ components defining the vector, and `w` used to flip the binormal if needed.  
  
Unity calculates the other surface vector (binormal) by taking a cross product between the normal and the tangent, and multiplying the result by tangent.w. Therefore, `w` should always be 1 or -1.  
  
You should calculate tangents yourself if you plan to use bump-mapped shaders on the Mesh. Assign tangents after assigning [normals](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh-normals.html) or using [RecalculateNormals](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.RecalculateNormals.html).  
  
**Note:** To make changes to the [tangents](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh-tangents.html), it is important to copy the tangents from the [Mesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html). Once the [tangents](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh-tangents.html) have been copied and changed, the [tangents](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh-tangents.html) can be reassigned back to the [Mesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html).
* * *
