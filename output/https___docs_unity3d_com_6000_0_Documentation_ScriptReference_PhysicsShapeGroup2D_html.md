* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsShapeGroup2D.html

# PhysicsShapeGroup2D
class in UnityEngine
/
Implemented in:[UnityEngine.Physics2DModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.Physics2DModule.html)
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
Represents a group of [PhysicsShape2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsShape2D.html) and their geometry.
A shape group represents multiple [PhysicsShape2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsShape2D.html) of the same or mixed [PhysicsShapeType2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsShapeType2D.html) along with their geometry. It is comprised of a single list of vertices ([GetShapeVertices](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsShapegroup2D.GetShapeVertices.html)) along with a list of [PhysicsShape2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsShape2D.html) which refer to specific ranges of those vertices i.e. they index into the list of vertices. Some shape types ([PhysicsShapeType2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsShapeType2D.html)) use a fixed number of vertices and some use a variable number of vertices therefore this single vertices list is a compact and efficient representation for multiple [PhysicsShape2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsShape2D.html) in a group.  
  
The shape group can be created by using the following methods: 
  * Calling [Collider2D.GetShapes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.GetShapes.html) where it would then represent all the shapes produced by that [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html)
  * Calling [Rigidbody2D.GetShapes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.GetShapes.html) where it would then represent all the shapes produced by all the[Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) attached to that [Rigidbody2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html)
  * Manually populating with custom shapes by calling [AddCircle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsShapeGroup2D.AddCircle.html), [AddCapsule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsShapeGroup2D.AddCapsule.html), [AddPolygon](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsShapeGroup2D.AddPolygon.html), [AddBox](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsShapeGroup2D.AddBox.html) or [AddEdges](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsShapeGroup2D.AddEdges.html).


### Properties
Property | Description  
---|---  
[localToWorldMatrix](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsShapeGroup2D-localToWorldMatrix.html) | Gets or sets a matrix that transforms the PhysicsShapeGroup2D vertices from local space into world space.  
[shapeCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsShapeGroup2D-shapeCount.html) | The total number of PhysicsShape2D in the shape group. (Read Only)  
[vertexCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsShapeGroup2D-vertexCount.html) | The total number of vertices in the shape group used to represent all PhysicsShape2D within it. (Read Only)  
### Constructors
Constructor | Description  
---|---  
[PhysicsShapeGroup2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsShapeGroup2D-ctor.html) | Initializes and returns an instance of PhysicsShapeGroup2D. The shape group will be empty and ready for use by Collider2D.GetShapes, Rigidbody2D.GetShapes or manually adding shapes.  
### Public Methods
Method | Description  
---|---  
[Add](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsShapeGroup2D.Add.html) | Adds a copy of all the PhysicsShape2D and their geometry from the specified physicsShapeGroup into this shape group. The specified physicsShapeGroup is not modified.  
[AddBox](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsShapeGroup2D.AddBox.html) | Adds a box shape (PhysicsShapeType2D.Polygon) to the shape group.  
[AddCapsule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsShapeGroup2D.AddCapsule.html) | Adds a capsule shape (PhysicsShapeType2D.Capsule) to the shape group.  
[AddCircle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsShapeGroup2D.AddCircle.html) | Adds a circle shape (PhysicsShapeType2D.Circle) to the shape group.  
[AddEdges](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsShapeGroup2D.AddEdges.html) | Adds an edges shape (PhysicsShapeType2D.Edges) to the shape group.  
[AddPolygon](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsShapeGroup2D.AddPolygon.html) | Adds a polygon shape (PhysicsShapeType2D.Polygon) to the shape group.  
[Clear](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsShapeGroup2D.Clear.html) | Clears all the vertices and shapes from the PhysicsShapeGroup.  
[DeleteShape](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsShapeGroup2D.DeleteShape.html) | When destroying a shape at the specified shapeIndex, all other shapes that exist above the specified shapeIndex will have their shape indices updated appropriately.  
[GetShape](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsShapeGroup2D.GetShape.html) | Gets the PhysicsShape2D stored at the specified shapeIndex.  
[GetShapeData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsShapeGroup2D.GetShapeData.html) | Gets a copy of both the shapes and vertices in the PhysicsShapeGroup2D.  
[GetShapeVertex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsShapeGroup2D.GetShapeVertex.html) | Gets a single vertex of a shape. The vertex index is zero-based with the shape having a quantity of vertex specified by PhysicsShape2D.vertexCount.  
[GetShapeVertices](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsShapeGroup2D.GetShapeVertices.html) | Gets a copy of the shape vertices in the PhysicsShapeGroup2D.  
[SetShapeAdjacentVertices](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsShapeGroup2D.SetShapeAdjacentVertices.html) | Sets the adjacent vertices of a shape.  
[SetShapeRadius](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsShapeGroup2D.SetShapeRadius.html) | Sets the radius of a shape.  
[SetShapeVertex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsShapeGroup2D.SetShapeVertex.html) | Sets a single vertex of a shape.  
* * *
