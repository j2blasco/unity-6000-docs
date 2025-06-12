* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CharacterController-isGrounded.html

#  [CharacterController](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CharacterController.html).isGrounded
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
isGrounded; 
### Description
Was the CharacterController touching the ground during the last move?
Indicates whether the CharacterController was touching the ground during the most recent call to CharacterController.Move or CharacterController.SimpleMove.  
  
This property is updated after each call to Move, based on collision detection with the ground. It returns true if the controller collided with any object below it during the movement — typically used to determine if the character is standing on a surface (e.g., terrain, platform, floor).
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    CharacterController[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CharacterController.html) characterController;  
  
    void Start()
    {
        characterController = GetComponent<CharacterController[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CharacterController.html)>();
    }  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        if (characterController.isGrounded)
        {
            print("CharacterController[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CharacterController.html) is grounded");
        }
    }
}

```

* * *
