* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.AddForceAtPosition.html

#  [Rigidbody](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html).AddForceAtPosition
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Rigidbody.html "Go to Rigidbody Component in the Manual")
## Declaration
public void AddForceAtPosition([Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) force, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) position, [ForceMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ForceMode.html) mode = ForceMode.Force); 
### Parameters
Parameter | Description  
---|---  
force | Force vector in world coordinates.  
position | Position in world coordinates.  
### Description
Applies `force` at `position`. As a result this will apply a torque and force on the object.
For realistic effects `position` should be approximately in the range of the surface of the rigidbody. This is most commonly used for explosions. When applying explosions it is best to apply forces over several frames instead of just one. Note that when `position` is far away from the center of the rigidbody the applied torque will be unrealistically large.  
  
Force can be applied only to an active rigidbody. If a GameObject is inactive, AddForceAtPosition has no effect.  
  
Wakes up the Rigidbody by default. If the force size is zero then the Rigidbody will not be woken up.  
  
For more information on how ForceMode affects velocity, see [Rigidbody.AddForce](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.AddForce.html).  
  
Additional resources: [AddForce](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.AddForce.html), [AddRelativeForce](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.AddRelativeForce.html), [AddTorque](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.AddTorque.html).
```
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void ApplyForce(Rigidbody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html) body)
    {
        Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) direction = body.transform.position - transform.position;
        body.AddForceAtPosition(direction.normalized, transform.position);
    }
}

```

* * *
