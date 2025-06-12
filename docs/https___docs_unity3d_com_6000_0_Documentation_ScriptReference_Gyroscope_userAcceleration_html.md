* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gyroscope-userAcceleration.html

#  [Gyroscope](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gyroscope.html).userAcceleration
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
[Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) userAcceleration; 
### Description
Returns the acceleration that the user is giving to the device.
The significance of this value is that the effect of gravity (which is also detected by the accelerometer) has been removed to leave just the acceleration from the user's movements.
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) forceVec;
    Rigidbody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html) rb;  
  
    void Start()
    {
        rb = GetComponent<Rigidbody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html)>();
    }  
  
    void FixedUpdate[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.FixedUpdate.html)()
    {
        // Apply forces to an object to match the side-to-side acceleration
        // the user is giving to the device.
        rb.AddForce(Input.gyro.userAcceleration.x * forceVec);
    }
}

```

* * *
