* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.SetNormals.html

#  [Mesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html).SetNormals
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
## Declaration
public void SetNormals(Vector3[] inNormals); 
## Declaration
public void SetNormals(List<Vector3> inNormals); 
## Declaration
public void SetNormals(NativeArray<T> inNormals); 
### Parameters
Parameter | Description  
---|---  
inNormals | Per-vertex normals.  
### Description
Set the normals of the Mesh.
Additional resources: [normals](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh-normals.html) property.
* * *
## Declaration
public void SetNormals(Vector3[] inNormals, int start, int length, [Rendering.MeshUpdateFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.MeshUpdateFlags.html) flags = MeshUpdateFlags.Default); 
## Declaration
public void SetNormals(List<Vector3> inNormals, int start, int length, [Rendering.MeshUpdateFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.MeshUpdateFlags.html) flags = MeshUpdateFlags.Default); 
## Declaration
public void SetNormals(NativeArray<T> inNormals, int start, int length, [Rendering.MeshUpdateFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.MeshUpdateFlags.html) flags = MeshUpdateFlags.Default); 
### Parameters
Parameter | Description  
---|---  
inNormals | Per-vertex normals.  
start | Index of the first element to take from the input array.  
length | Number of elements to take from the input array.  
flags | Flags controlling the function behavior, see [MeshUpdateFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.MeshUpdateFlags.html).  
### Description
Sets the vertex normals of the Mesh, using a part of the input array.
This method behaves as if you called SetNormals with an array that is a slice of the whole array, starting at `start` index and being of a given `length`. The resulting Mesh has `length` amount of vertices.
* * *
