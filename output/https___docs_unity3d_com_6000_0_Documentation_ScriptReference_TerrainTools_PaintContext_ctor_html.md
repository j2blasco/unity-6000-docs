* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.PaintContext-ctor.html

# PaintContext Constructor
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
public PaintContext([Terrain](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Terrain.html) terrain, [RectInt](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RectInt.html) pixelRect, int targetTextureWidth, int targetTextureHeight, bool sharedBoundaryTexel = true, bool fillOutsideTerrain = true); 
### Parameters
Parameter | Description  
---|---  
terrain | Terrain that defines terrain space for this PaintContext.  
pixelRect | Pixel rectangle to edit in the target terrain texture.  
targetTextureWidth | Width of the target terrain texture (per Terrain).  
targetTextureHeight | Height of the target terrain texture (per Terrain).  
sharedBoundaryTexel | Whether to stretch the Textures so that edge texels lie on the Terrain boundary, and are shared with connected Terrains.  
fillOutsideTerrain | Whether to fill empty space outside of the Terrain tiles with data from the nearest tile.  
### Description
Creates a new PaintContext, to edit a target texture on a Terrain, in a region defined by pixelRect.
This constructor finds all Terrain tiles that touch the pixelRect, searching across adjacent connected Terrain tiles. It also calculates the relevant regions on each Terrain, as well as the transforms between them.  
  
Additional resources: [PaintContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.PaintContext.html).
* * *
