* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody-rotation.html

#  [Rigidbody](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html).rotation
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Rigidbody.html "Go to Rigidbody Component in the Manual")
[Quaternion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html) rotation; 
### Description
The rotation of the Rigidbody.
Use Rigidbody.rotation to get and set the rotation of a Rigidbody using the physics engine.  
  
Changing the rotation of a Rigidbody using Rigidbody.rotation updates the Transform after the next physics simulation step. This is faster than updating the rotation using Transform.rotation, as Transform.rotation causes all attached Colliders to recalculate their rotation relative to the Rigidbody, whereas Rigidbody.rotation sets the values directly to the physics system.  
  
If you want to continuously rotate a rigidbody use [MoveRotation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.MoveRotation.html) instead, which takes interpolation into account.  
  
**Note:** [rotation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody-rotation.html) is world-space. 
```
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        // Set a custom rotation: 45 degrees around the Y-axis
        GetComponent<Rigidbody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html)>().rotation = Quaternion.Euler[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.Euler.html)(0, 45, 0);
    }
}

```

* * *
