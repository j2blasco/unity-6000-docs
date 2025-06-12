* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.PaintContext.GatherNormals.html

#  [PaintContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.PaintContext.html).GatherNormals
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
public void GatherNormals(); 
### Description
Gathers the normal information into `sourceRenderTexture`.
This function collects the terrain mesh normalmap data from all Terrain tiles in the PaintContext into `sourceRenderTexture`.  
  
This function is called internally by [TerrainPaintUtility.CollectNormals](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.TerrainPaintUtility.CollectNormals.html).  
  
Important: There is no corresponding ScatterNormals function, because the normals are not stored, but calculated from the heightmap.  
  
Additional resources: [PaintContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.PaintContext.html), [PaintContext.GatherHeightmap](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.PaintContext.GatherHeightmap.html)
* * *
