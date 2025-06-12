* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.SetVertices.html

#  [Mesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html).SetVertices
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
public void SetVertices(Vector3[] inVertices); 
## Declaration
public void SetVertices(List<Vector3> inVertices); 
## Declaration
public void SetVertices(NativeArray<T> inVertices); 
### Parameters
Parameter | Description  
---|---  
inVertices | Per-vertex positions.  
### Description
Assigns a new vertex positions array.
Additional resources: [vertices](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh-vertices.html) property.
* * *
## Declaration
public void SetVertices(Vector3[] inVertices, int start, int length, [Rendering.MeshUpdateFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.MeshUpdateFlags.html) flags = MeshUpdateFlags.Default); 
## Declaration
public void SetVertices(List<Vector3> inVertices, int start, int length, [Rendering.MeshUpdateFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.MeshUpdateFlags.html) flags = MeshUpdateFlags.Default); 
## Declaration
public void SetVertices(NativeArray<T> inVertices, int start, int length, [Rendering.MeshUpdateFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.MeshUpdateFlags.html) flags = MeshUpdateFlags.Default); 
### Parameters
Parameter | Description  
---|---  
inVertices | Per-vertex positions.  
start | Index of the first element to take from the input array.  
length | Number of elements to take from the input array.  
flags | Flags controlling the function behavior, see [MeshUpdateFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.MeshUpdateFlags.html).  
### Description
Sets the vertex positions of the Mesh, using a part of the input array.
This method behaves as if you called SetVertices with an array that is a slice of the whole array, starting at `start` index and being of a given `length`. The resulting Mesh has `length` amount of vertices.
* * *
