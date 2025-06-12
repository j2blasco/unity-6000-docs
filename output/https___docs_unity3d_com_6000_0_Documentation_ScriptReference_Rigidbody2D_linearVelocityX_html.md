* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D-linearVelocityX.html

#  [Rigidbody2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html).linearVelocityX
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
linearVelocityX; 
### Description
The X component of the linear velocity of the Rigidbody2D in world-units per second.
The linear velocity is specified as a [Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) with components in the X and Y directions (there is no Z direction in 2D physics).  
  
This property lets you read and write only the X component of the [Rigidbody2D.linearVelocity](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D-linearVelocity.html) without affecting the Y component of the [Rigidbody2D.linearVelocity](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D-linearVelocity.html). This is convenient when dealing with X and Y directions in isolation.  
  
Additional resources: [Rigidbody2D.linearVelocity](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D-linearVelocity.html) and [Rigidbody2D.linearVelocityY](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D-linearVelocityY.html).
```
using UnityEngine;  
  
// Ensure that the maximum horizontal speed moving right isn't larger than the configurable value.
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public float MaximumSpeedRight = 2f;  
  
    private Rigidbody2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html) rb;  
  
    void Start()
    {
        rb = GetComponent<Rigidbody2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html)>();
    }  
  
    void FixedUpdate[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.FixedUpdate.html)()
    {
        // Clamp the horizontal speed.
        if (rb.linearVelocityX > MaximumSpeedRight)
        {
            rb.linearVelocityX = MaximumSpeedRight;
        }
    }
}
```

* * *
