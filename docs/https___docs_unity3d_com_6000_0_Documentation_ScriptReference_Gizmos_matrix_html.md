* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gizmos-matrix.html

#  [Gizmos](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gizmos.html).matrix
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
[Matrix4x4](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.html) matrix; 
### Description
Sets the [Matrix4x4](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.html) that the Unity Editor uses to draw [Gizmos](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gizmos.html).
The [Gizmos.matrix](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gizmos-matrix.html) stores the position, rotation and scale of the [Gizmos](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gizmos.html). By default, [Gizmos](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gizmos.html) always uses world coordinates. The default [Gizmos.matrix](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gizmos-matrix.html) transforms the world coordinates using a default identity matrix. [Transform.localToWorldMatrix](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform-localToWorldMatrix.html) changes local coordinate space to world space.  
  
[GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)s often use local coordinates. [Gizmos.matrix](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gizmos-matrix.html) changes these local coordinates into world coordinates to allow [Gizmos](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gizmos.html) to use them. For example, a rotating object uses local coordinates. A transfer into world coordinates happens using [Gizmos.matrix](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gizmos-matrix.html). To visualise the object, use [Gizmos.DrawCube](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gizmos.DrawCube.html). See below.  
  
To use the example to draw a red, semi-transparent, cube gizmo:  
1. Place this example script on a Cylinder at the origin.  
2. Select the Cylinder in the Hierarchy and then click the `Play` button.  
3. Next, click the `Scene` button. The gizmo should appear.  
The cylinder will rotate in `Play` mode and be seen rotating in `Scene` view.
```
using System.Collections;
using System.Collections.Generic;
using UnityEngine;  
  
// Gizmos.matrix[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gizmos-matrix.html) example  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // Allow the speed of rotation to be changed.
    public float rotationSpeed = 50.0f;  
  
    void OnDrawGizmosSelected()
    {
        Gizmos.color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gizmos-color.html) = new Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html)(0.75f, 0.0f, 0.0f, 0.75f);  
  
        // Convert the local coordinate values into world
        // coordinates for the matrix transformation.
        Gizmos.matrix[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gizmos-matrix.html) = transform.localToWorldMatrix;
        Gizmos.DrawCube[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gizmos.DrawCube.html)(Vector3.zero[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-zero.html), Vector3.one[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-one.html));
    }  
  
    // Rotate[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Rotate.html) the cylinder.
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        float zRot = rotationSpeed * Time.deltaTime[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-deltaTime.html);
        transform.Rotate(0.0f, 0.0f, zRot);
    }
}

```

* * *
