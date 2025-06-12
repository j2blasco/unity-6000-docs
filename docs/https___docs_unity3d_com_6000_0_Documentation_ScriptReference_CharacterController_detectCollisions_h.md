* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CharacterController-detectCollisions.html

#  [CharacterController](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CharacterController.html).detectCollisions
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
detectCollisions; 
### Description
Determines whether other rigidbodies or character controllers collide with this character controller (by default this is always enabled).
This method does not affect collisions detected during the character controller's movement but rather decides whether an incoming collider will be blocked by the controller's collider. For example, a box collider in the Scene will block the movement of the controller, but the box may still fall through the controller if detectCollisions is false. This property is useful to disable the character controller temporarily. For example, you might want to mount a character into a car and disable collision detection until it exits the car again.
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    CharacterController[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CharacterController.html) controller;  
  
    void Start()
    {
        controller = GetComponent<CharacterController[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CharacterController.html)>();
        controller.detectCollisions = false;
    }
}

```

* * *
