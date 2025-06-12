* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsShape2D-radius.html

#  [PhysicsShape2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsShape2D.html).radius
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
radius; 
### Description
The radius of the shape.
All [PhysicsShapeType2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsShapeType2D.html) use this radius with the exception of the [Polygon](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsShapeType2D.Polygon.html) type. Refer to the individual shape types for details on how the radius is used for the respective shape.
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
  
        // Validate the shape radius.
        Assert.AreApproximatelyEqual[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Assertions.Assert.AreApproximatelyEqual.html)(1f, circleShape.radius);
        Assert.AreApproximatelyEqual[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Assertions.Assert.AreApproximatelyEqual.html)(0.5f, capsuleShape.radius);
    }
}

```

* * *
