* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.OnControllerColliderHit.html

#  [MonoBehaviour](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html).OnControllerColliderHit(ControllerColliderHit)
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-MonoBehaviour.html "Go to MonoBehaviour Component in the Manual")
### Description
OnControllerColliderHit is called when the controller hits a collider while performing a Move.
This can be used to push objects when they collide with the character.
```
// This script pushes all rigidbodies that the character touches  
  
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public float pushPower = 2.0F;  
  
    void OnControllerColliderHit(ControllerColliderHit[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ControllerColliderHit.html) hit)
    {
        Rigidbody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html) body = hit.collider.attachedRigidbody;  
  
        // no rigidbody
        if (body == null || body.isKinematic)
            return;  
  
        // We dont want to push objects below us
        if (hit.moveDirection.y < -0.3f)
            return;  
  
        // Calculate push direction from move direction,
        // we only push objects to the sides never up and down
        Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) pushDir = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(hit.moveDirection.x, 0, hit.moveDirection.z);  
  
        // If you know how fast your character is trying to move,
        // then you can also multiply the push velocity by that.  
  
        // Apply the push
        body.velocity = pushDir * pushPower;
    }
}

```

* * *
