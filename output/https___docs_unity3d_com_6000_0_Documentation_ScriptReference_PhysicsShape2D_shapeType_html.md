* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsShape2D-shapeType.html

#  [PhysicsShape2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsShape2D.html).shapeType
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
[PhysicsShapeType2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsShapeType2D.html) shapeType; 
### Description
The shape type determines how the vertices and radius are used by this [PhysicsShape2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsShape2D.html).
Refer to the [PhysicsShapeType2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsShapeType2D.html) documentation for more information about the different shape types.
```
using UnityEngine;
using UnityEngine.Assertions;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        // Create a shape group.
        var shapeGroup = new PhysicsShapeGroup2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsShapeGroup2D.html)();  
  
        // Add a Circle to the shape group.
        var circleShapeIndex = shapeGroup.AddCircle
            (
                center: new Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html)(-2f, 3f),
                radius: 1f
            );  
  
        // Add a Capsule to the shape group.
        var capsuleShapeIndex = shapeGroup.AddCapsule
            (
                vertex0: Vector2.down[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2-down.html),
                vertex1: Vector2.up[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2-up.html),
                radius: 0.5f
            );  
  
        // Fetch the shapes.
        var circleShape = shapeGroup.GetShape(circleShapeIndex);
        var capsuleShape = shapeGroup.GetShape(capsuleShapeIndex);  
  
        // Validate the shape types.
        Assert.AreEqual[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Assertions.Assert.AreEqual.html)(PhysicsShapeType2D.Circle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsShapeType2D.Circle.html), circleShape.shapeType);
        Assert.AreEqual[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Assertions.Assert.AreEqual.html)(PhysicsShapeType2D.Capsule[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsShapeType2D.Capsule.html), capsuleShape.shapeType);
    }
}

```

* * *
