* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PolygonCollider2D.GetPath.html

#  [PolygonCollider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PolygonCollider2D.html).GetPath
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
public Vector2[] GetPath(int index); 
### Parameters
Parameter | Description  
---|---  
index | The index of the path to retrieve.  
### Returns
**Vector2[]** An ordered array of the vertices (points) in the selected path. 
### Description
Gets a path from the Collider by its index.
A _path_ is a cyclic sequence of line segments between points that define the outline of the Collider. Because the Collider can have holes and discontinuous parts, its shape is not necessarily defined by a single path.  
  
Returns an ordered array of the points in the path.  
  
Additional resources: [pathCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PolygonCollider2D-pathCount.html), [SetPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PolygonCollider2D.SetPath.html).
* * *
## Declaration
public int GetPath(int index, List<Vector2> points); 
### Parameters
Parameter | Description  
---|---  
index | The index of the path to retrieve.  
points | An ordered list of the vertices (points) in the selected path.  
### Returns
**int** Returns the number of results placed in the `points` list. 
### Description
Gets a path from the Collider by its index.
A _path_ is a cyclic sequence of line segments between points that define the outline of the Collider. Because the Collider can have holes and discontinuous parts, its shape is not necessarily defined by a single path.  
  
Returns an ordered list of the points in the path.  
  
The integer return value is the number of results written into the `points` list. The points list will be resized if it doesn't contain enough elements to report all the points.This prevents memory from being allocated for results when the `points` list does not need to be resized, and improves garbage collection performance when the query is performed frequently.  
  
Additional resources: [pathCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PolygonCollider2D-pathCount.html), [SetPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PolygonCollider2D.SetPath.html).
* * *
