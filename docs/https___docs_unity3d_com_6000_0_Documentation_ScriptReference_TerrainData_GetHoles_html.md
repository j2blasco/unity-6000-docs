* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainData.GetHoles.html

#  [TerrainData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainData.html).GetHoles
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
public bool[,] GetHoles(int xBase, int yBase, int width, int height); 
### Parameters
Parameter | Description  
---|---  
xBase | First x index of Terrain holes samples to retrieve.  
yBase | First y index of Terrain holes samples to retrieve.  
width | Number of samples to retrieve along the Terrain holes x axis.  
height | Number of samples to retrieve along the Terrain holes y axis.  
### Description
Gets an array of Terrain holes samples.
Returns a two-dimensional array of Terrain holes samples. The samples are represented as bool values: `true` for surface and `false` for hole. The array has the dimensions [height,width] and is indexed as [y,x].
* * *
