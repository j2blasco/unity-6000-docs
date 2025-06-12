* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.GetRelativePointVelocity.html

#  [Rigidbody](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html).GetRelativePointVelocity
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
public [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) GetRelativePointVelocity([Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) relativePoint); 
### Description
The velocity relative to the rigidbody at the point `relativePoint`.
GetRelativePointVelocity will take the angularVelocity of the rigidbody into account when calculating the velocity.
```
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public Rigidbody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html) rb;  
  
    void Start()
    {
        rb = GetComponent<Rigidbody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html)>();
    }  
  
    // Get the velocity of a wheel, specified by its position in local space.
    // This method assumes that the wheel is a child of the Rigidbody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html), or that the wheel translates relative to the Rigidbody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html). 
    Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) CalcWheelVelocity(Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) localWheelPos)
    {
        return rb.GetRelativePointVelocity(localWheelPos);
    }
}

```

* * *
