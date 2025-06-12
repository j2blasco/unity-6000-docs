* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.TerrainPaintUtility.CollectNormals.html

#  [TerrainPaintUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.TerrainPaintUtility.html).CollectNormals
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
public static [TerrainTools.PaintContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.PaintContext.html) CollectNormals([Terrain](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Terrain.html) terrain, [Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) boundsInTerrainSpace, int extraBorderPixels = 0, bool fillOutsideTerrain = true); 
### Parameters
Parameter | Description  
---|---  
terrain | Reference Terrain tile.  
boundsInTerrainSpace | The region in terrain space from which to collect normals.  
extraBorderPixels | Number of extra border pixels required.  
fillOutsideTerrain | Whether to fill empty space outside of Terrain tiles with data from the nearest tile.  
### Returns
**PaintContext** PaintContext containing the combined normalmap data for the specified region. 
### Description
Helper function to set up a PaintContext that collects mesh normal data from one or more Terrain tiles.
CollectNormals identifies all of the normalmap pixels that are within `extraBorderPixels` of the bounds rectangle. The search is performed across adjacent connected Terrain tiles. The pixels are collected into a temporary render texture and stored in [PaintContext.sourceRenderTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.PaintContext-sourceRenderTexture.html).  
  
Important: there is no corresponding function to write modified normalmap data back to the Terrain tiles, because the normalmap is not stored; it is calculated from the heightmap.  
  
Once you are done using the sourceRenderTexture, you must call [TerrainPaintUtility.ReleaseContextResources](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.TerrainPaintUtility.ReleaseContextResources.html) to release the RenderTexture resources.  
  
Additional resources: [PaintContext.GatherNormals](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.PaintContext.GatherNormals.html) and [PaintContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.PaintContext.html). 
* * *
