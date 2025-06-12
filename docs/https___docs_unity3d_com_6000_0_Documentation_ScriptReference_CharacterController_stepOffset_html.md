* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CharacterController-stepOffset.html

#  [CharacterController](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CharacterController.html).stepOffset
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
stepOffset; 
### Description
The character controllers step offset in meters.
The maximum height in meters that the character can climb over automatically when moving. This is used to allow the character to smoothly step over small obstacles like stairs or ledges instead of colliding with them.  
  
Increasing the `stepOffset` allows the character to step over taller obstacles without jumping. Decreasing the value restricts the character to only stepping over smaller objects. 
  * **Higher values** allow smoother traversal over high steps or uneven terrain, but may cause unrealistic movement if set too high (e.g., stepping over full-height walls).
  * **Lower values** make the character collide with even small obstacles, potentially requiring jumping or custom logic to overcome them.


This value works in conjunction with the slope limit—if an obstacle’s slope is too steep, even within the `stepOffset`, it might still block movement.  
  
**Note:** See the Manual page [Character Controller component](https://docs.unity3d.com/6000.0/Documentation/Manual/class-CharacterController.html) which describes `stepOffset` in detail.
```
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public CharacterController[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CharacterController.html) controller;  
  
    void Example()
    {
        controller = GetComponent<CharacterController[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CharacterController.html)>();
        // Allow the character to step over obstacles up to 0.5 meters high
        controller.stepOffset = 0.5f;
    }
}

```

* * *
