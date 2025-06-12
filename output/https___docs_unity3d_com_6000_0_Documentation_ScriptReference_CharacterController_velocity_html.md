* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CharacterController-velocity.html

#  [CharacterController](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CharacterController.html).velocity
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-CharacterController.html "Go to CharacterController Component in the Manual")
[Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) velocity; 
### Description
The current relative velocity of the Character (see notes).
This allows you to track how fast the character is actually walking, for example when it is stuck at a wall this value will be the zero vector.  
  
Note: The velocity returned is simply the difference in distance for the current timestep before and after a call to [CharacterController.Move](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CharacterController.Move.html) or [CharacterController.SimpleMove](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CharacterController.SimpleMove.html). The velocity is relative because it won't track movements to the transform that happen outside of the CharacterController (e.g. character parented under another moving Transform, such as a moving vehicle).
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    CharacterController[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CharacterController.html) controller;
    void Start()
    {
        controller = GetComponent<CharacterController[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CharacterController.html)>();
    }  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) horizontalVelocity = controller.velocity;
        horizontalVelocity = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(controller.velocity.x, 0, controller.velocity.z);  
  
        // The speed on the x-z plane ignoring any speed
        float horizontalSpeed = horizontalVelocity.magnitude;
        // The speed from gravity or jumping
        float verticalSpeed  = controller.velocity.y;
        // The overall speed
        float overallSpeed = controller.velocity.magnitude;
    }
}

```

* * *
