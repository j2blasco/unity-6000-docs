* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EdgeCollider2D.SetPoints.html

#  [EdgeCollider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EdgeCollider2D.html).SetPoints
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
public bool SetPoints(List<Vector2> points); 
### Parameters
Parameter | Description  
---|---  
points | A list of [Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) used to set the points. This list must contain at least two points.  
### Returns
**bool** Returns true if the list contains two or more points and the points are correctly set. Returns false otherwise. 
### Description
Sets all the points that define a set of continuous edges.
If the provided `points` list contains less than two points then `false` is returned indicating the points were not set. Any points that are not valid such as them being NaN or Infinite are set to [Vector2.zero](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2-zero.html).
* * *
