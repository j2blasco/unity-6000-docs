* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TrailRenderer.SetPositions.html

#  [TrailRenderer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TrailRenderer.html).SetPositions
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
public void SetPositions(Vector3[] positions); 
## Declaration
public void SetPositions(NativeArray<Vector3> positions); 
## Declaration
public void SetPositions(NativeSlice<Vector3> positions); 
### Parameters
Parameter | Description  
---|---  
positions | The array of positions to set.  
### Description
Sets the positions of all vertices in the trail.
You can only use this method to modify existing positions in the Trail. You cannot use it to add new positions.  
  
When setting all positions, use this method instead of [SetPosition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TrailRenderer.SetPosition.html) because it is more efficient to set all positions using a single command than to set each position individually.  
  
Additional resources: [positionCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TrailRenderer-positionCount.html) property.  
  
Additional resources: [SetPosition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TrailRenderer.SetPosition.html) function.
* * *
