* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporterIndexFormat.Auto.html

#  [ModelImporterIndexFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporterIndexFormat.html).Auto
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
Use 16 or 32 bit index buffer depending on mesh size.
Meshes that have less than 65536 vertices will use 16 bit index buffer, and larger meshes will use 32 bit one.  
  
Note however that GPU support for 32 bit indices is not guaranteed on all platforms; for example Android devices with Mali-400 GPU do not support them. When using 32 bit indices on such a platform, a warning message will be logged and mesh will not render. If you need to use large meshes on such devices, set index format to [UInt16](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporterIndexFormat.UInt16.html), then the mesh will be split up into 64k vertex chunks at import time.  
  
Additional resources: [ModelImporter.indexFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter-indexFormat.html), [Mesh.indexFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh-indexFormat.html).
* * *
