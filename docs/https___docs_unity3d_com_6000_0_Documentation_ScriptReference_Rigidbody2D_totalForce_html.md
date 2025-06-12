* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D-totalForce.html

#  [Rigidbody2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html).totalForce
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
[Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) totalForce; 
### Description
The total amount of force that has been explicitly applied to this [Rigidbody2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html) since the last physics simulation step.
When adding force to the [Rigidbody2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html) using [Rigidbody2D.AddForce](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.AddForce.html), [Rigidbody2D.AddForceAtPosition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.AddForceAtPosition.html) or [Rigidbody2D.AddRelativeForce](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.AddRelativeForce.html) the force total is summed. This only applies when using [ForceMode2D.Force](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ForceMode2D.Force.html) and not when using [ForceMode2D.Impulse](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ForceMode2D.Impulse.html).  
  
During the next simulation step, the total force will be time-integrated into the [Rigidbody2D.linearVelocity](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D-linearVelocity.html) then automatically reset to [zero](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2-zero.html).  
  
**NOTE** : Only a [Rigidbody2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html) with a [Dynamic Body Type](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RigidbodyType2D.Dynamic.html) will respond to force or torque. Setting this property on a [Kinematic Body Type](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RigidbodyType2D.Kinematic.html) or [Static Body Type](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RigidbodyType2D.Static.html) will have no effect.
```
using UnityEngine;
using UnityEngine.Assertions;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        // Fetch the rigidbody.
        var body = GetComponent<Rigidbody2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html)>();  
  
        // Make the assumption the body has no previous force applied.
        Assert.AreEqual[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Assertions.Assert.AreEqual.html)(Vector2.zero[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2-zero.html), body.totalForce);  
  
        // Initialize a force.
        var force = new Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html)(3f, 2f);  
  
        // Add the force.
        body.AddForce(force);  
  
        // The total force should be what we just added.
        Assert.AreEqual[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Assertions.Assert.AreEqual.html)(force, body.totalForce);  
  
        // Add the same force again.
        body.AddForce(force);  
  
        // The total force should still be what we've added.
        Assert.AreEqual[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Assertions.Assert.AreEqual.html)(force * 2f, body.totalForce);  
  
        // We can reset any force that has been applied since the last simulation step.
        body.totalForce = Vector2.zero[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2-zero.html);
    }
}

```

* * *
