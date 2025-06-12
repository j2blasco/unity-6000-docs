* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsShapeType2D.Edges.html

#  [PhysicsShapeType2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsShapeType2D.html).Edges
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
### Description
Use multiple edges to interpret the [PhysicsShape2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsShape2D.html) geometry.
An edge geometry type is comprised of an unlimited quantity of vertices in the [PhysicsShape2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsShape2D.html) and a [PhysicsShape2D.radius](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsShape2D-radius.html). The vertices represent the consecutive edges where each vertex connects to the next vertex. These edges represent an open shape with no interior even if the first and last vertices overlap. The [PhysicsShape2D.radius](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsShape2D-radius.html) is the radius of all edges. (Edges with a radius of zero become infinitely thin edges while a radius greater than zero results in capsule shaped edges i.e. any edge with a radius.)  
  
Edges also have an [PhysicsShape2D.adjacentStart](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsShape2D-adjacentStart.html) and [PhysicsShape2D.adjacentEnd](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsShape2D-adjacentEnd.html) feature allowing separate edge shapes to be joined.  
  
**NOTE** : You should ensure that edges do not self-intersect as this can produce incorrect collision responses. As checking self-intersection has a runtime cost, this constraint is not validated and so you should ensure this does not occur.
* * *
