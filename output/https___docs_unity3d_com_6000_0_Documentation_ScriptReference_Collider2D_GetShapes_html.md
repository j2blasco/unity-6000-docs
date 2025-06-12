* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.GetShapes.html

#  [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html).GetShapes
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
public int GetShapes([PhysicsShapeGroup2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsShapeGroup2D.html) physicsShapeGroup); 
### Parameters
Parameter | Description  
---|---  
physicsShapeGroup | The [PhysicsShapeGroup2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsShapeGroup2D.html) to store the retrieved [PhysicsShape2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsShape2D.html) in.  
### Returns
**int** Returns the number of [PhysicsShape2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsShape2D.html) retrieved from the [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html). 
### Description
Gets all the [PhysicsShape2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsShape2D.html) used by the [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html).
All [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) represent a high-level definition of 2D geometry that is used to create efficient low-level primitive shapes used by the physics engine for collision detection. These low-level primitive shapes are what the 2D physics gizmos draw within the Unity Editor. This method provides access to a copy of these primitive shapes which can be useful in various use-cases such as debugging and gizmos or rendering [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) geometry at runtime.  
  
Use this method to gain access to a copy of all the low-level primitive shapes that are produced by a [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html). If no such shapes exist on the [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) as indicated by [Collider2D.shapeCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D-shapeCount.html) then the shape group will not be populated with shapes. If shapes do exist, the group is first emptied before being populated with shapes.  
  
Each [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) produces either a single or multiple [PhysicsShape2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsShape2D.html) of a single [PhysicsShapeType2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsShapeType2D.html) as indicated below: 
  * A [CircleCollider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CircleCollider2D.html) produces a single [PhysicsShapeType2D.Circle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsShapeType2D.Circle.html) object
  * A [CapsuleCollider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CapsuleCollider2D.html) produces a single [PhysicsShapeType2D.Capsule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsShapeType2D.Capsule.html) object
  * An [EdgeCollider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EdgeCollider2D.html) produces a single [PhysicsShapeType2D.Edges](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsShapeType2D.Edges.html) object
  * A [BoxCollider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BoxCollider2D.html) produces a single [PhysicsShapeType2D.Polygon](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsShapeType2D.Polygon.html) object (a box is a convex polygon)
  * A [PolygonCollider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PolygonCollider2D.html) produces either a single or multiple [PhysicsShapeType2D.Polygon](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsShapeType2D.Polygon.html) object(s)
  * A [TilemapCollider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Tilemaps.TilemapCollider2D.html) produces either a single or multiple [PhysicsShapeType2D.Polygon](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsShapeType2D.Polygon.html) object(s) (each tile can produce multiple polygons so this can produce a lot of data)
  * A [CompositeCollider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CompositeCollider2D.html) produces either a single or multiple [PhysicsShapeType2D.Polygon](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsShapeType2D.Polygon.html) ([CompositeCollider2D.GeometryType.Polygons](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CompositeCollider2D.GeometryType.Polygons.html)) or [PhysicsShapeType2D.Edges](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsShapeType2D.Edges.html) ([CompositeCollider2D.GeometryType.Outlines](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CompositeCollider2D.GeometryType.Outlines.html)) object(s)


All [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) shape vertices are stored in the local space of the [Rigidbody2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html) they are attached to i.e. their vertices are relative to the pose of the [Rigidbody2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html) therefore when a [Rigidbody2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html) translates or rotates, the vertices of attached [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) do not change. This is why changes to position or rotation should only ever happen via the [Rigidbody2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html) as this is the most efficient method. When retrieving shapes, the shape vertices are in the local space of the [Rigidbody2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html). The current position and rotation of the [Rigidbody2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html) is stored in [PhysicsShapeGroup2D.localToWorldMatrix](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsShapeGroup2D-localToWorldMatrix.html) and can be used to transform the shape vertices to world space. If the [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) is not attached to any [Rigidbody2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html) i.e. it is Static then the local space and world space are identical therefore the [PhysicsShapeGroup2D.localToWorldMatrix](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsShapeGroup2D-localToWorldMatrix.html) is set to [Matrix4x4.identity](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4-identity.html).  
  
**Note:** It is recommened to reuse the [PhysicsShapeGroup2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsShapeGroup2D.html) because then memory allocations only occur if the number of shapes or vertices retrieved are greater than the existing capacity of the [PhysicsShapeGroup2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsShapeGroup2D.html). Reusing this object therefore minimizes allocations to a bare minimum and eventually to none so no work is produced for the garbage collector.  
  
Additional resources: [Rigidbody2D.GetShapes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.GetShapes.html).
* * *
## Declaration
public int GetShapes([PhysicsShapeGroup2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsShapeGroup2D.html) physicsShapeGroup, int shapeIndex, int shapeCount = 1); 
### Parameters
Parameter | Description  
---|---  
physicsShapeGroup | The [PhysicsShapeGroup2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsShapeGroup2D.html) to store the retrieved [PhysicsShape2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsShape2D.html) in.  
shapeIndex | The index of the first shape to retrieve. This should be in the range of 0 to [Collider2D.shapeCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D-shapeCount.html)-1.  
shapeCount | The number of shapes to retrieve. The `shapeIndex` + `shapeCount` must be less than or equal to [Collider2D.shapeCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D-shapeCount.html).  
### Returns
**int** Returns the number of [PhysicsShape2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsShape2D.html) retrieved from the [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html). In all cases this should be the same number as `shapeCount` . 
### Description
Gets the specified range of the [PhysicsShape2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsShape2D.html) used by the [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html).
* * *
