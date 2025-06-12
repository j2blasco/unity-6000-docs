* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.PaintContext.CreateFromBounds.html

#  [PaintContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.PaintContext.html).CreateFromBounds
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
public static [TerrainTools.PaintContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.PaintContext.html) CreateFromBounds([Terrain](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Terrain.html) terrain, [Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) boundsInTerrainSpace, int inputTextureWidth, int inputTextureHeight, int extraBorderPixels = 0, bool sharedBoundaryTexel = true, bool fillOutsideTerrain = true); 
### Parameters
Parameter | Description  
---|---  
terrain | Terrain that defines terrain space for this PaintContext.  
boundsInTerrainSpace | Terrain space bounds to edit in the target terrain texture.  
inputTextureWidth | Width of the input Terrain Texture for all connected Terrains.  
inputTextureHeight | Height of the input Terrain Texture for all connected Terrains.  
extraBorderPixels | Number of extra border pixels required. The default value is 0.  
sharedBoundaryTexel | Whether to stretch the Textures so that edge texels lie on the Terrain boundary, and are shared with connected Terrains.  
fillOutsideTerrain | Whether to fill empty space outside of the Terrain tiles with data from the nearest tile.  
### Description
Constructs a PaintContext that you can use to edit a texture on a Terrain, in the region defined by boundsInTerrainSpace and extraBorderPixels.
This function calculates a pixelRect from `boundsInTerrainSpace` and `extraBorderPixels`, and then constructs a PaintContext from the pixelRect.  
  
This function is called internally by [TerrainPaintUtility.BeginPaintHeightmap](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.TerrainPaintUtility.BeginPaintHeightmap.html), [TerrainPaintUtility.BeginPaintTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.TerrainPaintUtility.BeginPaintTexture.html) and [TerrainPaintUtility.CollectNormals](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.TerrainPaintUtility.CollectNormals.html).  
  
Additional resources: [PaintContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.PaintContext.html).
* * *
