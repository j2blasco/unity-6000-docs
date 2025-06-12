* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainData.GetSupportedLayers.html

#  [TerrainData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainData.html).GetSupportedLayers
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
public int[] GetSupportedLayers(int xBase, int yBase, int totalWidth, int totalHeight); 
## Declaration
public int[] GetSupportedLayers([Vector2Int](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2Int.html) positionBase, [Vector2Int](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2Int.html) size); 
### Description
Returns an array of all supported detail layer indices in the area.
The Terrain uses a detail layer density map. Each pixel in the map determines the amount of details objects that will be procedurally placed in the pixel area. The layer determines the detail prototype that will be instantiated at the location.
* * *
