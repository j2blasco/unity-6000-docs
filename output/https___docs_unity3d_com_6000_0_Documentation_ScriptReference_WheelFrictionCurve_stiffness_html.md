* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WheelFrictionCurve-stiffness.html

#  [WheelFrictionCurve](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WheelFrictionCurve.html).stiffness
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
stiffness; 
### Description
Multiplier for the [extremumValue](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WheelFrictionCurve-extremumValue.html) and [asymptoteValue](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WheelFrictionCurve-asymptoteValue.html) values (default 1).
Changes the stiffness of the friction. Setting this to zero will completely disable all friction from the wheel.  
  
Usually you modify `stiffness` to simulate various ground materials (e.g. lower the stiffness when driving on grass). Additional resources: [WheelCollider.GetGroundHit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WheelCollider.GetGroundHit.html).
```
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public WheelCollider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WheelCollider.html) wheel;  
  
    void Start()
    {
        wheel = GetComponent<WheelCollider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WheelCollider.html)>();
    }  
  
    // When attached to the WheelCollider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WheelCollider.html), modifies tire friction based on
    // static friction of the ground material.
    void FixedUpdate[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.FixedUpdate.html)()
    {
        WheelHit[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WheelHit.html) hit;
        if (wheel.GetGroundHit(out hit))
        {
            WheelFrictionCurve[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WheelFrictionCurve.html) fFriction = wheel.forwardFriction;
            fFriction.stiffness = hit.collider.material.staticFriction;
            wheel.forwardFriction = fFriction;
            WheelFrictionCurve[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WheelFrictionCurve.html) sFriction = wheel.sidewaysFriction;
            sFriction.stiffness = hit.collider.material.staticFriction;
            wheel.sidewaysFriction = sFriction;
        }
    }
}

```

* * *
