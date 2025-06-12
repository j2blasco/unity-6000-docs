* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.PaintContext.GetTerrain.html

#  [PaintContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.PaintContext.html).GetTerrain
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
public [Terrain](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Terrain.html) GetTerrain(int terrainIndex); 
### Parameters
Parameter | Description  
---|---  
terrainIndex | Index of the terrain.  
### Returns
**Terrain** Returns the Terrain object. 
### Description
Retrieves a Terrain from the PaintContext.
When painting across a border, the PaintContext can refer to several Terrain tiles. GetTerrain is used to access those Terrain tiles. terrainIndex must be between 0 and [PaintContext.terrainCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.PaintContext-terrainCount.html) - 1. Additional resources: [PaintContext.GetClippedPixelRectInTerrainPixels](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.PaintContext.GetClippedPixelRectInTerrainPixels.html) and [PaintContext.GetClippedPixelRectInRenderTexturePixels](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.PaintContext.GetClippedPixelRectInRenderTexturePixels.html). 
* * *
