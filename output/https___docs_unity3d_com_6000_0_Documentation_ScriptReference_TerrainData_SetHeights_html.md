* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainData.SetHeights.html

#  [TerrainData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainData.html).SetHeights
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
public void SetHeights(int xBase, int yBase, float[,] heights); 
### Parameters
Parameter | Description  
---|---  
xBase | First x index of heightmap samples to set.  
yBase | First y index of heightmap samples to set.  
heights | Array of heightmap samples to set (values range from 0 to 1, array indexed as [y,x]).  
### Description
Sets an array of heightmap samples.
Sets heightmap data using a two dimensional array of heightmap samples. The samples are represented as float values ranging from 0 to 1. The area affected is defined by the array dimensions and starts at xBase and yBase. The heights array is indexed as [y,x].  
  
This method recomputes all the LOD and vegetation information for the terrain on each call, which can be computationally expensive. In interactive editing scenarios, it may be better to call [TerrainData.SetHeightsDelayLOD](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainData.SetHeightsDelayLOD.html) instead, followed by [TerrainData.SyncHeightmap](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainData.SyncHeightmap.html) when the user completes an editing action.
* * *
