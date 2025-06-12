* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EdgeCollider2D.GetPoints.html

#  [EdgeCollider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EdgeCollider2D.html).GetPoints
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
public int GetPoints(List<Vector2> points); 
### Parameters
Parameter | Description  
---|---  
points | A list of [Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) used to receive the points.  
### Returns
**int** Returns the number of points placed in the `points` list. 
### Description
Gets all the points that define a set of continuous edges.
Ensure the provided list capacity is large enough to contain all retrieved points you need. Unity automatically increases the list capacity if it is not large enough to contain all retrieved points. As the list is usually reused, it is recommended to make the list large enough to return a reasonable quantity of points for its expected use. If the list capacity does not need to be increased, then this function will not allocate any memory and no additional work is produced for the garbage collector.
* * *
