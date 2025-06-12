* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TrailRenderer.GetVisiblePositions.html

#  [TrailRenderer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TrailRenderer.html).GetVisiblePositions
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TrailRenderer.html "Go to TrailRenderer Component in the Manual")
## Declaration
public int GetVisiblePositions(out Vector3[] positions); 
## Declaration
public int GetVisiblePositions(out NativeArray<Vector3> positions); 
## Declaration
public int GetVisiblePositions(out NativeSlice<Vector3> positions); 
### Parameters
Parameter | Description  
---|---  
positions | The array of positions to retrieve.  
### Returns
**int** How many positions were actually stored in the output array. 
### Description
Get the visible positions of all vertices in the trail.
This method is similar to [GetPositions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TrailRenderer.GetPositions.html), except that it will not return positions that the Trail Renderer created while [emitting](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TrailRenderer-emitting.html) was set to `false`.
* * *
