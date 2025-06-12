* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsShape2D.html

# PhysicsShape2D
struct in UnityEngine
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
Represents an efficient low-level physics shape used by the physics engine.
A [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) is a high-level representation of physics geometry that produces low-level [PhysicsShape2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsShape2D.html) geometry that the physics engine understands. A [PhysicsShape2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsShape2D.html) can represent any shape type as defined by [PhysicsShapeType2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsShapeType2D.html).  
  
Additional resources: [PhysicsShapeGroup2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsShapeGroup2D.html).
### Properties
Property | Description  
---|---  
[adjacentEnd](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsShape2D-adjacentEnd.html) | Defines the position of a virtual point adjacent to the end vertex of an edge shape.  
[adjacentStart](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsShape2D-adjacentStart.html) | Defines the position of a virtual point adjacent to the start vertex of an edge shape.  
[radius](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsShape2D-radius.html) | The radius of the shape.  
[shapeType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsShape2D-shapeType.html) | The shape type determines how the vertices and radius are used by this PhysicsShape2D.  
[useAdjacentEnd](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsShape2D-useAdjacentEnd.html) | When the value is true, then the shape will use the adjacentEnd feature. When the value is false, then the shape will not use the adjacentEnd feature.  
[useAdjacentStart](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsShape2D-useAdjacentStart.html) | When the value is true, then the shape will use the adjacentStart feature. When the value is false, then the shape will not use the adjacentStart feature.  
[vertexCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsShape2D-vertexCount.html) | The total number of vertices used to represent the shape type.  
[vertexStartIndex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsShape2D-vertexStartIndex.html) | The start index for the geometry of this shape within the PhysicsShapeGroup2D.  
* * *
