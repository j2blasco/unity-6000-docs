* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D-totalTorque.html

#  [Rigidbody2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html).totalTorque
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
totalTorque; 
### Description
The total amount of torque that has been explicitly applied to this [Rigidbody2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html) since the last physics simulation step.
When adding torque to the [Rigidbody2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html) using [Rigidbody2D.AddTorque](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.AddTorque.html) or [Rigidbody2D.AddForceAtPosition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.AddForceAtPosition.html) (when force is applied away from the [worldCenterOfMass](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D-worldCenterOfMass.html)) the torque total is summed. When the physics simulation step runs, this total torque is used.  
  
During the next simulation step, the total torque will be time-integrated into the [Rigidbody2D.angularVelocity](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D-angularVelocity.html) then automatically reset to zero.  
  
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
  
        // Make the assumption the body has no previous torque applied.
        Assert.AreApproximatelyEqual[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Assertions.Assert.AreApproximatelyEqual.html)(0.0f, body.totalTorque, Mathf.Epsilon[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.Epsilon.html));  
  
        // Initialize a torque.
        var torque = 5f;  
  
        // Add the torque.
        body.AddTorque(torque);  
  
        // The total torque should be what we just added.
        Assert.AreApproximatelyEqual[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Assertions.Assert.AreApproximatelyEqual.html)(torque, body.totalTorque, Mathf.Epsilon[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.Epsilon.html));  
  
        // Add the same torque again.
        body.AddTorque(torque);  
  
        // The total torque should still be what we've added.
        Assert.AreEqual[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Assertions.Assert.AreEqual.html)(torque * 2f, body.totalTorque);  
  
        // We can reset any torque that has been applied since the last simulation step.
        body.totalTorque = 0f;
    }
}

```

* * *
