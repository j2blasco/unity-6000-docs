* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D-linearDamping.html

#  [Rigidbody2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html).linearDamping
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
linearDamping; 
### Description
The linear damping of the Rigidbody2D linear velocity.
Damping can be used to reduce the magnitude of the [Rigidbody2D.linearVelocity](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D-linearVelocity.html) (linear speed) of a [Rigidbody2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html) over time.  
  
Zero indicates that no damping should be used whereas higher values increase the damping, effectively slowing down the linear motion faster. Unlike contact friction, linear damping is always applied.  
  
**Note:** The following formula is how the linear damping is applied: `linearVelocity *= 1.0f / ( 1.0f + simulation-time-step * linearDamping )`  
  
Additional resources: [Rigidbody2D.angularDamping](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D-angularDamping.html).
```
using UnityEngine;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    private Rigidbody2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html) rb;  
  
    void Start()
    {
        rb = GetComponent<Rigidbody2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html)>();
    }  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        if (Input.GetButton[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetButton.html)("Fire1"))
            OpenParachute();  
  
        if (Input.GetButton[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetButton.html)("space"))
            CloseParachute();
    }  
  
    void OpenParachute()
    {
        // Set a large damping to simulate an open parachute.
        rb.linearDamping = 20f;
    }  
  
    void CloseParachute()
    {
        // Turn-off damping to simulate a closed parachute.
        rb.linearDamping = 0f;
    }
}
```

* * *
