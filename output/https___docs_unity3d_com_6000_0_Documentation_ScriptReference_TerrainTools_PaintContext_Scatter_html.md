* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.PaintContext.Scatter.html

#  [PaintContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.PaintContext.html).Scatter
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
public void Scatter(Func<ITerrainInfo,RenderTexture> terrainDest, [Material](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html) blitMaterial, int blitPass, Action<ITerrainInfo> beforeBlit, Action<ITerrainInfo> afterBlit); 
### Parameters
Parameter | Description  
---|---  
terrainDest | Function returning the RenderTexture to be written for each Terrain.  
blitMaterial | The material used to copy the data. If null, the default blit material is used.  
blitPass | The material pass used to copy the data. Its default value is 0.  
beforeBlit | An optional action to call before copying to each Terrain.  
afterBlit | An optional action to call after copying to each Terrain.  
### Description
Applies an edited PaintContext by copying modifications back to user-specified RenderTextures for the source Terrain tiles.
After the edits to a PaintContext are complete, this function applies the modified data in `destinationRenderTexture` to the data stored for each Terrain. Scatter performs this copy to a set of RenderTextures, which is specified by `terrainDest`.  
  
This function uses the following steps to scatter to each Terrain in the PaintContext:  
1) Calls `terrainDest` to retrieve the target RenderTexture.  
2) Calls `beforeBlit`.  
3) Uses `blitMaterial` and `blitPass` to copy the `destinationRenderTexture` into the target RenderTexture.  
4) Calls `afterBlit`.  
  
Additional resources: [PaintContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.PaintContext.html), [PaintContext.Gather](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.PaintContext.Gather.html).
* * *
