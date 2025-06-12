* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainData.SetHeightsDelayLOD.html

#  [TerrainData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainData.html).SetHeightsDelayLOD
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
public void SetHeightsDelayLOD(int xBase, int yBase, float[,] heights); 
### Parameters
Parameter | Description  
---|---  
xBase | First x index of heightmap samples to set.  
yBase | First y index of heightmap samples to set.  
heights | Array of heightmap samples to set (values range from 0 to 1, array indexed as [y,x]).  
### Description
Sets an array of heightmap samples.
Sets heightmap data using a two dimensional array of heightmap samples. The samples are represented as float values ranging from 0 to 1. The area affected is defined by the array dimensions and starts at xBase and yBase. The heights array is indexed as [y,x].  
  
Unlike [TerrainData.SetHeights](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainData.SetHeights.html), this method does not update the LOD information for the terrain, or any trees/vegetation objects; this means the terrain may be temporarily rendered at an inappropriately high level of detail, but makes the method fast enough to be used in interactive editing scenarios. Once modifications to the terrain have been completed - for example, when the user releases the mouse button - call [TerrainData.SyncHeightmap](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainData.SyncHeightmap.html) to update all the LOD and vegetation information.
* * *
