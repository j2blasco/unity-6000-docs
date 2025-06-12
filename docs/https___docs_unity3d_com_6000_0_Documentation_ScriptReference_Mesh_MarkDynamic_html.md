* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.MarkDynamic.html

#  [Mesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html).MarkDynamic
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
public void MarkDynamic(); 
### Description
Optimize mesh for frequent updates.
Call this before assigning vertices to get better performance when continually updating the Mesh. Internally, this makes the Mesh use "dynamic buffers" in the underlying graphics API, which are more efficient when Mesh data changes often.  
  
Additional resources: [vertices](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh-vertices.html), [normals](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh-normals.html), [triangles](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh-triangles.html), [UploadMeshData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.UploadMeshData.html).
* * *
