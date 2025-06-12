* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.PaintContext.Gather.html

#  [PaintContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.PaintContext.html).Gather
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
public void Gather(Func<ITerrainInfo,Texture> terrainSource, [Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) defaultColor, [Material](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html) blitMaterial, int blitPass, Action<ITerrainInfo> beforeBlit, Action<ITerrainInfo> afterBlit); 
### Parameters
Parameter | Description  
---|---  
terrainSource | A function that returns the Texture data to collect from each Terrain.  
defaultColor | The default color for `sourceRenderTexture`.  
blitMaterial | The material used to copy the data. If null, the default blit material is used.  
blitPass | The material pass used to copy the data.  
beforeBlit | An optional action to call before copying from each Terrain. The default is null.  
afterBlit | An optional action to call after copying from each Terrain. The default is null.  
### Description
Gathers user-specified Texture data into `sourceRenderTexture`.
This function collects Texture data from all Terrain tiles in the PaintContext, and merges that data into `sourceRenderTexture`. The `terrainSource` function specifies what data to collect from each Terrain. Gather assumes that the Texture data, which `terrainSource` returns, is mapped over the Terrain tile in a manner similar to the Heightmap and Alphamaps.  
  
First, the function clears `sourceRenderTexture` to `defaultColor`.  
Then, it uses the following steps to gather each Terrain in the PaintContext:  
1) Calls `terrainSource` to retrieve the Texture.  
2) Calls `beforeBlit`.  
3) Uses `blitMaterial` and `blitPass` to copy The Texture into `sourceRenderTexture`.  
4) Calls `afterBlit`.  
  
Additional resources: [PaintContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.PaintContext.html), [PaintContext.Scatter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.PaintContext.Scatter.html). 
* * *
