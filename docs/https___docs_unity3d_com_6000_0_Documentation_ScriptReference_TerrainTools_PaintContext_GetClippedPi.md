* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.PaintContext.GetClippedPixelRectInTerrainPixels.html

#  [PaintContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.PaintContext.html).GetClippedPixelRectInTerrainPixels
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
public [RectInt](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RectInt.html) GetClippedPixelRectInTerrainPixels(int terrainIndex); 
### Parameters
Parameter | Description  
---|---  
terrainIndex | Index of the Terrain.  
### Returns
**RectInt** Returns the clipped pixel rectangle. 
### Description
Retrieves the clipped pixel rectangle for a Terrain.
When painting across a border, the PaintContext can refer to several Terrain tiles. GetClippedPixelRectInTerrainPixels returns the [PaintContext.pixelRect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.PaintContext-pixelRect.html) clipped to the specified Terrain, in the pixel coordinates of the target texture on that Terrain. terrainIndex must be between 0 and [PaintContext.terrainCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.PaintContext-terrainCount.html) - 1. Additional resources: [PaintContext.GetTerrain](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.PaintContext.GetTerrain.html), [PaintContext.targetTextureWidth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.PaintContext-targetTextureWidth.html), and [PaintContext.targetTextureHeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.PaintContext-targetTextureHeight.html). 
* * *
