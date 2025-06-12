* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshRenderer-enlightenVertexStream.html

#  [MeshRenderer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshRenderer.html).enlightenVertexStream
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-MeshRenderer.html "Go to MeshRenderer Component in the Manual")
[Mesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html) enlightenVertexStream; 
### Description
Vertex attributes that override the primary mesh when the MeshRenderer uses lightmaps in the Realtime Global Illumination system.
This vertex stream is used exclusively for UVs for real-time lightmaps.  
  
When Unity renders a `MeshRenderer` that uses real-time lightmaps, Unity streams the data in `MeshRenderer.enlightenVertexStream` to `TEXCOORD2` instead of the data in [Mesh.uv3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh-uv3.html)]. For more information, see [Lightmap UVs](https://docs.unity3d.com/6000.0/Documentation/Manual/LightingGiUvs.html).  
  
This data is not serialized. Unity calculates the UVs for the Realtime Global Illumination system during the precompute stage.
* * *
