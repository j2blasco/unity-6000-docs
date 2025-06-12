* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CharacterController-collisionFlags.html

#  [CharacterController](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CharacterController.html).collisionFlags
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
[CollisionFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CollisionFlags.html) collisionFlags; 
### Description
What part of the capsule collided with the environment during the last CharacterController.Move call.
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
        if ((controller.collisionFlags & CollisionFlags.Above[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CollisionFlags.Above.html)) != 0)
        {
            print("touched the ceiling");
        }
    }
}

```

* * *
