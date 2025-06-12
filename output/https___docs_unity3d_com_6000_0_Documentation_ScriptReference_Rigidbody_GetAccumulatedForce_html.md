* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.GetAccumulatedForce.html

#  [Rigidbody](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html).GetAccumulatedForce
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
public [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) GetAccumulatedForce(float step = Time.fixedDeltaTime); 
### Parameters
Parameter | Description  
---|---  
step | The timestep of the next physics simulation.  
### Returns
**Vector3** Accumulated force expressed in [ForceMode.Force](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ForceMode.Force.html). 
### Description
Returns the force that the [Rigidbody](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html) has accumulated before the simulation step.
The accumulated force is reset during each physics simulation step.
```
using UnityEngine;  
  
public class AddForceScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    private Rigidbody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html) rigidbody;  
  
    void Start()
    {
        rigidbody = GetComponent<Rigidbody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html)>();
        rigidbody.useGravity = false;
    }  
  
    private void FixedUpdate[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.FixedUpdate.html)()
    {
        rigidbody.AddForce(Vector3.up[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-up.html) * 10f, ForceMode.Impulse[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ForceMode.Impulse.html));
        var accumulatedForce = rigidbody.GetAccumulatedForce();
        rigidbody.AddForce(accumulatedForce * -1f, ForceMode.Force[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ForceMode.Force.html));
    }
}

```

In this example, the Rigidbody doesn't move.
* * *
