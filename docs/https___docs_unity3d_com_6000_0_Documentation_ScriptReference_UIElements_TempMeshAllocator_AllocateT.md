* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.TempMeshAllocator.AllocateTempMesh.html

#  [TempMeshAllocator](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.TempMeshAllocator.html).AllocateTempMesh
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
public void AllocateTempMesh(int vertexCount, int indexCount, out NativeSlice<Vertex> vertices, out NativeSlice<ushort> indices); 
### Parameters
Parameter | Description  
---|---  
vertexCount | The number of vertices to allocate, with a maximum limit of 65535 (or UInt16.MaxValue).  
indexCount | The number of triangle list indices to allocate, where every three indices represent one triangle. Therefore, this value should always be a multiple of three.  
vertices | The returned vertices.  
indices | The returned indices.  
### Description
Allocates the specified number of vertices and indices from a temporary allocator. 
You can only call this method during the mesh generation phase of the panel and shouldn't use it beyond. 
* * *
