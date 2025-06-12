* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsShape2D-vertexCount.html

#  [PhysicsShape2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsShape2D.html).vertexCount
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
vertexCount; 
### Description
The total number of vertices used to represent the [shape type](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsShape2D-shapeType.html).
See [PhysicsShapeType2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsShapeType2D.html) for details on how each type uses different quantities of vertices to represent itself.
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
  
        // Validate the shape vertex count.
        Assert.AreEqual[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Assertions.Assert.AreEqual.html)(1, circleShape.vertexCount);
        Assert.AreEqual[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Assertions.Assert.AreEqual.html)(2, capsuleShape.vertexCount);
    }
}

```

* * *
