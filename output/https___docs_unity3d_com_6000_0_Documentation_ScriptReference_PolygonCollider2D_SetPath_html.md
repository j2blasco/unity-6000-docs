* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PolygonCollider2D.SetPath.html

#  [PolygonCollider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PolygonCollider2D.html).SetPath
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
public void SetPath(int index, Vector2[] points); 
### Parameters
Parameter | Description  
---|---  
index | Index of the path to set.  
points | An ordered array of the vertices (points) that define the path.  
### Description
Define a path by its constituent points.
A _path_ is a cyclic sequence of line segments between points that define the outline of the polygon. Because the polygon can have holes and discontinuous parts, its shape is not necessarily defined by a single path. For example, the polygon might actually be 3 separate paths. In this case [SetPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PolygonCollider2D.SetPath.html) will be called 3 times, with an `index` of 0, 1 and 2. So `index` specifies which of these three collections of points are used.  
  
Additional resources: [pathCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PolygonCollider2D-pathCount.html), [GetPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PolygonCollider2D.GetPath.html).
* * *
## Declaration
public void SetPath(int index, List<Vector2> points); 
### Parameters
Parameter | Description  
---|---  
index | Index of the path to set.  
points | An ordered list of the vertices (points) that define the path.  
### Description
Define a path by its constituent points.
A _path_ is a cyclic sequence of line segments between points that define the outline of the polygon. Because the polygon can have holes and discontinuous parts, its shape is not necessarily defined by a single path. For example, the polygon might actually be 3 separate paths. In this case [SetPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PolygonCollider2D.SetPath.html) will be called 3 times, with an `index` of 0, 1 and 2. So `index` specifies which of these three collections of points are used.  
  
Additional resources: [pathCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PolygonCollider2D-pathCount.html), [GetPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PolygonCollider2D.GetPath.html).
* * *
