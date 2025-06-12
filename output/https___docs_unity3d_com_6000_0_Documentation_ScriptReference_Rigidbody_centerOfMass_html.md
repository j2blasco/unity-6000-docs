* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody-centerOfMass.html

#  [Rigidbody](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html).centerOfMass
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
[Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) centerOfMass; 
### Description
The center of mass relative to the transform's origin.
If you don't set the center of mass from a script it will be calculated automatically from all colliders attached to the rigidbody. After a custom center of mass set, it will no longer be recomputed automatically on modifications such as adding or removing colliders, translating them, scaling etc. To revert back to the automatically computed center of mass, use [Rigidbody.ResetCenterOfMass](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.ResetCenterOfMass.html).  
  
Setting the center of mass is often useful when simulating cars to make them more stable. A car with a lower center of mass is less likely to topple over.  
  
Note: `centerOfMass` is relative to the transform's position and rotation, but will not reflect the transform's scale!
```
// Expose center of mass to allow it to be set from
// the inspector.
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) com;
    public Rigidbody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html) rb;  
  
    void Start()
    {
        rb = GetComponent<Rigidbody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html)>();
        rb.centerOfMass = com;
    }
}

```

* * *
