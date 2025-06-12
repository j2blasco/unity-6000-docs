* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CollisionFlags.html

# CollisionFlags
enumeration
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
### Description
CollisionFlags is a bitmask returned by CharacterController.Move.
It gives you a broad overview of where your character collided with any other objects.
```
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        CharacterController[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CharacterController.html) controller = GetComponent<CharacterController[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CharacterController.html)>();  
  
        if (controller.collisionFlags == CollisionFlags.None[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CollisionFlags.None.html))
        {
            print("Free floating!");
        }  
  
        if ((controller.collisionFlags & CollisionFlags.Sides[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CollisionFlags.Sides.html)) != 0)
        {
            print("Touching sides!");
        }  
  
        if (controller.collisionFlags == CollisionFlags.Sides[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CollisionFlags.Sides.html))
        {
            print("Only touching sides, nothing else!");
        }  
  
        if ((controller.collisionFlags & CollisionFlags.Above[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CollisionFlags.Above.html)) != 0)
        {
            print("Touching Ceiling!");
        }  
  
        if (controller.collisionFlags == CollisionFlags.Above[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CollisionFlags.Above.html))
        {
            print("Only touching Ceiling, nothing else!");
        }  
  
        if ((controller.collisionFlags & CollisionFlags.Below[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CollisionFlags.Below.html)) != 0)
        {
            print("Touching ground!");
        }  
  
        if (controller.collisionFlags == CollisionFlags.Below[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CollisionFlags.Below.html))
        {
            print("Only touching ground, nothing else!");
        }
    }
}

```

### Properties
Property | Description  
---|---  
[None](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CollisionFlags.None.html) | CollisionFlags is a bitmask returned by CharacterController.Move.  
[Sides](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CollisionFlags.Sides.html) | CollisionFlags is a bitmask returned by CharacterController.Move.  
[Above](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CollisionFlags.Above.html) | CollisionFlags is a bitmask returned by CharacterController.Move.  
[Below](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CollisionFlags.Below.html) | CollisionFlags is a bitmask returned by CharacterController.Move.  
* * *
