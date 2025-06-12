* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.MeshGenerationNode.DrawMesh.html

#  [MeshGenerationNode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.MeshGenerationNode.html).DrawMesh
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
public void DrawMesh(NativeSlice<Vertex> vertices, NativeSlice<ushort> indices, [Texture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) texture); 
### Parameters
Parameter | Description  
---|---  
vertices | The vertices to be drawn. All referenced vertices must be initialized.  
indices | The triangle list indices. Must be a multiple of 3. All indices must be initialized.  
texture | An optional texture to be applied on the triangles. Pass null to rely on vertex colors only.  
### Description
Records a draw command with the provided triangle-list indexed mesh. 
* * *
