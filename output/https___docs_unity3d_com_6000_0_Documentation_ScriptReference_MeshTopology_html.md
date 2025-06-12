* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshTopology.html

# MeshTopology
enumeration
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
Topology of [Mesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html) faces.
Normally meshes are composed of triangles (three vertex indices per face), but in some cases you might want to render complex things that are made up from lines or points. Creating a [Mesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html) with that topology and using it to render is usually the most efficient way.  
  
Additional resources: [Mesh.SetIndices](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.SetIndices.html) function.
### Properties
Property | Description  
---|---  
[Triangles](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshTopology.Triangles.html) | Mesh is made from triangles.  
[Quads](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshTopology.Quads.html) | Mesh is made from quads.  
[Lines](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshTopology.Lines.html) | Mesh is made from lines.  
[LineStrip](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshTopology.LineStrip.html) | Mesh is a line strip.  
[Points](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshTopology.Points.html) | Mesh is made from points.  
* * *
