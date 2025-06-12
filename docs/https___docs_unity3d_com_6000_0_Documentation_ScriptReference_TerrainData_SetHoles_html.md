* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainData.SetHoles.html

#  [TerrainData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainData.html).SetHoles
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
public void SetHoles(int xBase, int yBase, bool[,] holes); 
### Parameters
Parameter | Description  
---|---  
xBase | First x index of Terrain holes samples to set.  
yBase | First y index of Terrain holes samples to set.  
holes | Array of Terrain holes samples to set (array indexed as [y,x]).  
### Description
Sets an array of Terrain holes samples.
Sets Terrain holes data using a two-dimensional array of Terrain holes samples. The samples are represented as bool values: `true` for surface and `false` for hole. The array dimensions define the area affected, which starts at `xBase` and `yBase`. The Terrain holes array is indexed as [y,x].  
  
This method recomputes all LOD and vegetation information for the Terrain on each call, which can be computationally expensive. In interactive editing scenarios, it might be better to call [TerrainData.SetHolesDelayLOD](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainData.SetHolesDelayLOD.html) instead, followed by [TerrainData.SyncTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainData.SyncTexture.html) when the user completes an editing action.
* * *
