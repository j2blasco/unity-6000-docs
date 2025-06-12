* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.GetShapes.html

#  [Rigidbody2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html).GetShapes
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
**int** Returns the number of [PhysicsShape2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsShape2D.html) retrieved from the [Rigidbody2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html). 
### Description
Gets all the [PhysicsShape2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsShape2D.html) used by all [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) attached to the [Rigidbody2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html).
Where [Collider2D.GetShapes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.GetShapes.html) will retrieve all shapes used by a specific [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html), this method will return all the shapes on all [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) attached to the [Rigidbody2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html).  
  
For a complete description of how retrieving shapes works, refer to [Collider2D.GetShapes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.GetShapes.html).
* * *
