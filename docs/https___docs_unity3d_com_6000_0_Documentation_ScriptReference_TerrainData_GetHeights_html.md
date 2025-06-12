* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainData.GetHeights.html

#  [TerrainData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainData.html).GetHeights
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
public float[,] GetHeights(int xBase, int yBase, int width, int height); 
### Parameters
Parameter | Description  
---|---  
xBase | First index of heightmap samples to retrieve along the Terrain's x axis.  
yBase | First index of heightmap samples to retrieve along the Terrain's z axis.  
width | Number of samples to retrieve along the Terrain's x axis.  
height | Number of samples to retrieve along the Terrain's z axis.  
### Description
Gets an array of heightmap samples.
Returns a two dimensional array of heightmap samples. The samples are represented as float values ranging from 0 to 1. The array has the dimensions [height,width] and is indexed as [y,x].
* * *
