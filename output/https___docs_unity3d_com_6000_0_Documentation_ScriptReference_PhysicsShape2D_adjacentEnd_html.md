* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsShape2D-adjacentEnd.html

#  [PhysicsShape2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsShape2D.html).adjacentEnd
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
[Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) adjacentEnd; 
### Description
Defines the position of a virtual point adjacent to the end vertex of an edge shape.
An edges shape is comprised of multiple edges (line segments) defined by all its vertices. However, when a collision occurs with the end vertex of the shape then this vertex can be used to form a collision normal, and calculate the collision response. This allows for joining of individual edge shapes to produce a continuous collision surface.  
  
This property is identical to [EdgeCollider2D.adjacentEndPoint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EdgeCollider2D-adjacentEndPoint.html). It is only used when the [shapeType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsShape2D-shapeType.html) is [PhysicsShapeType2D.Edges](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsShapeType2D.Edges.html) and [useAdjacentEnd](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsShape2D-useAdjacentEnd.html) is true.
* * *
