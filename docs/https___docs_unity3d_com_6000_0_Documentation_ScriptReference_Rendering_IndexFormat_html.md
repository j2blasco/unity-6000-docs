* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.IndexFormat.html

# IndexFormat
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
Format of the mesh index buffer data.
Index buffer can either be 16 bit (supports up to 65535 vertices in a mesh), or 32 bit (supports up to 4 billion vertices). Default index format is 16 bit, since that takes less memory and bandwidth.  
  
Note that GPU support for 32 bit indices is not guaranteed on all platforms; for example Android devices with Mali-400 GPU do not support them. When using 32 bit indices on such a platform, a warning message will be logged and mesh will not render.  
  
**Note:** the maximum possible vertex index (for example, 0xFFFF for a 16 bit index format) might not be usable. Some graphics APIs and GPUs skip rendering triangles with maximum vertex indices.  
  
Additional resources: [Mesh.indexFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh-indexFormat.html), [ModelImporter.indexFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter-indexFormat.html), [Mesh.SetIndices](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.SetIndices.html).
### Properties
Property | Description  
---|---  
[UInt16](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.IndexFormat.UInt16.html) | 16 bit mesh index buffer format.  
[UInt32](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.IndexFormat.UInt32.html) | 32 bit mesh index buffer format.  
* * *
