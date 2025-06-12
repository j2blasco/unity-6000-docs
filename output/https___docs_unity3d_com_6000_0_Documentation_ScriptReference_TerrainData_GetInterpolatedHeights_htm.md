* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainData.GetInterpolatedHeights.html

#  [TerrainData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainData.html).GetInterpolatedHeights
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
public float[,] GetInterpolatedHeights(float xBase, float yBase, int xCount, int yCount, float xInterval, float yInterval); 
### Parameters
Parameter | Description  
---|---  
xBase | The base x coordinate.  
yBase | The base y coordinate.  
xCount | The number of queries along the X axis.  
yCount | The number of queries along the Y axis.  
xInterval | The interval between each query along the X axis.  
yInterval | The interval between each query along the Y axis.  
### Description
Gets an array of terrain height values using the normalized x,y coordinates.
The function returns a two-dimensional array of size [yCount, xCount]. Each returned value is an interpolation between the four neighboring Terrain height samples, based on where the sampling point is located within the quad of the four neighboring samples. The sampling points are evenly distributed, starting at (xBase, yBase). Points are spaced `xInterval` apart along the X axis, and `yInterval` apart along the Y axis. All the floating point arguments are specified as normalized coordinates, with 0 indicating the left/top border of the Terrain, and 1 indicating the right/bottom border of the Terrain. If a sampling point is placed outside of [0,1], it is clamped to the range.
* * *
## Declaration
public void GetInterpolatedHeights(float[,] results, int resultXOffset, int resultYOffset, float xBase, float yBase, int xCount, int yCount, float xInterval, float yInterval); 
### Parameters
Parameter | Description  
---|---  
results | The array to fill with height values.  
resultXOffset | The offset from the beginning of the array, along the X axis, at which to start filling in height values.  
resultYOffset | The offset from the beginning of the array, along the Y axis, at which to start filling in height values.  
xBase | The base x coordinate.  
yBase | The base y coordinate.  
xCount | The number of queries along the X axis.  
yCount | The number of queries along the Y axis.  
xInterval | The interval between each query along the X axis.  
yInterval | The interval between each query along the Y axis.  
### Description
Fills the array with Terrain height values using normalized x,y coordinates.
The function takes a two-dimensional array, and fills height values into the part starting at (resultXOffset, resultYOffset). Unlike the function overload above, Unity guarantees not to allocate any memory during calls to the `GetInterpolatedHeights` function.
* * *
