* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody.GetPointVelocity.html

#  [ArticulationBody](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody.html).GetPointVelocity
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ArticulationBody.html "Go to ArticulationBody Component in the Manual")
## Declaration
public [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) GetPointVelocity([Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) worldPoint); 
### Description
Gets the velocity of the articulation body at the specified `worldPoint` in global space.
GetPointVelocity takes the angularVelocity of the articulation body into account when calculating the velocity.
```
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public ArticulationBody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody.html) ab;  
  
    void Start()
    {
        ab = GetComponent<ArticulationBody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody.html)>();
    }  
  
    // Get the velocity of a wheel, specified by its position in local space.
    Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) CalcWheelVelocity(Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) localWheelPos)
    {
        return ab.GetPointVelocity(transform.TransformPoint(localWheelPos));
    }
}

```

* * *
