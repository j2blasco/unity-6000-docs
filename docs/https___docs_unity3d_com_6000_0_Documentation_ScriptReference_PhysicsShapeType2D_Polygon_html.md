* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsShapeType2D.Polygon.html

#  [PhysicsShapeType2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsShapeType2D.html).Polygon
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
Use a convex polygon shape to interpret the [PhysicsShape2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsShape2D.html) geometry.
A polygon geometry type is comprised of a minimum of three (triangle) vertices and maximum defined by [Physics2D.MaxPolygonShapeVertices](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics2D.MaxPolygonShapeVertices.html) in the [PhysicsShape2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsShape2D.html). The vertices represent a set of consecutive edges where each vertex connects to the next vertex with the last vertex automatically representing an edge connecting to the first vertex resulting in a closed primitive shape. These edges must result in a convex polygon. If this is not the case then the physics system will constrain the polygon to be convex by producing a convex hull. All polygon collision detection uses convex polygons for performance reasons.
* * *
