* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.IndexFormat.UInt32.html

#  [IndexFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.IndexFormat.html).UInt32
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
32 bit mesh index buffer format.
This format supports meshes with up to 4 billion vertices.  
  
Note that GPU support for 32 bit indices is not guaranteed on all platforms; for example Android devices with Mali-400 GPU do not support them. When using 32 bit indices on such a platform, a warning message will be logged and mesh will not render.  
  
Additional resources: [Mesh.indexFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh-indexFormat.html), [ModelImporter.indexFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter-indexFormat.html), [SystemInfo.supports32bitsIndexBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-supports32bitsIndexBuffer.html).
* * *
