* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.PaintContext.GatherAlphamap.html

#  [PaintContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.PaintContext.html).GatherAlphamap
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
public void GatherAlphamap([TerrainLayer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainLayer.html) inputLayer, bool addLayerIfDoesntExist); 
### Parameters
Parameter | Description  
---|---  
inputLayer | TerrainLayer used for painting.  
addLayerIfDoesntExist | Set to true to specify that the inputLayer is added to the terrain if it does not already exist. Set to false to specify that terrain layers are not added to the terrain.  
### Description
Gathers the alphamap information into `sourceRenderTexture`.
This function collects the alphamap data from all Terrain tiles in the PaintContext into `sourceRenderTexture`.  
  
This function is called internally by [TerrainPaintUtility.BeginPaintTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.TerrainPaintUtility.BeginPaintTexture.html).  
  
Additional resources: [PaintContext.ScatterAlphamap](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.PaintContext.ScatterAlphamap.html). 
* * *
