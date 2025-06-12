* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LineRenderer.GetPositions.html

#  [LineRenderer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LineRenderer.html).GetPositions
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LineRenderer.html "Go to LineRenderer Component in the Manual")
## Declaration
public int GetPositions(out Vector3[] positions); 
## Declaration
public int GetPositions(out NativeArray<Vector3> positions); 
## Declaration
public int GetPositions(out NativeSlice<Vector3> positions); 
### Parameters
Parameter | Description  
---|---  
positions | The array of positions to retrieve. The array passed should be of at least [positionCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LineRenderer-positionCount.html) in size.  
### Returns
**int** How many positions were actually stored in the output array. 
### Description
Get the positions of all vertices in the line.
This method is preferred to [GetPosition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LineRenderer.GetPosition.html) when retrieving all positions, as it is more efficient to get all positions using a single command than to get each position individually.  
  
Additional resources: [positionCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LineRenderer-positionCount.html) property, [GetPosition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LineRenderer.GetPosition.html) function.
* * *
