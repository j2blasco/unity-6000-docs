* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.DetailBrushRepresentation.GetStrength.html

#  [DetailBrushRepresentation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.DetailBrushRepresentation.html).GetStrength
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
public float GetStrength(int ix, int iy); 
### Parameters
Parameter | Description  
---|---  
ix | The x position of the brush offset.  
iy | The y position of the brush offset.  
### Returns
**float** Returns the strength at the passed in position. 
### Description
Gets the strength at the passed in position.
* * *
## Declaration
public float GetStrength([Vector2Int](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2Int.html) position); 
### Parameters
Parameter | Description  
---|---  
position | The position of the brush offset.  
### Returns
**float** Returns the strength at the passed in position. 
### Description
Gets the strength at the passed in position.
**Note:** This method is an overloaded method using a `Vector2Int` instead of two separate ints for position. 
* * *
