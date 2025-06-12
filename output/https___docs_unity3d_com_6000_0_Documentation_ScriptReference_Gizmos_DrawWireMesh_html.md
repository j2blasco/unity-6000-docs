* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gizmos.DrawWireMesh.html

#  [Gizmos](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gizmos.html).DrawWireMesh
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
public static void DrawWireMesh([Mesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html) mesh, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) position = Vector3.zero, [Quaternion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html) rotation = Quaternion.identity, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) scale = Vector3.one); 
## Declaration
public static void DrawWireMesh([Mesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html) mesh, int submeshIndex, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) position = Vector3.zero, [Quaternion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html) rotation = Quaternion.identity, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) scale = Vector3.one); 
### Parameters
Parameter | Description  
---|---  
mesh | Mesh to draw as a gizmo.  
position | Position (default is zero).  
rotation | Rotation (default is no rotation).  
scale | Scale (default is no scale).  
submeshIndex | Submesh to draw (default is -1, which draws whole mesh).  
### Description
Draws a wireframe mesh.
Additional resources: [DrawMesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gizmos.DrawMesh.html).
* * *
