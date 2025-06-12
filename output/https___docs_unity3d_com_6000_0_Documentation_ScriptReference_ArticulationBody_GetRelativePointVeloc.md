* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody.GetRelativePointVelocity.html

#  [ArticulationBody](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody.html).GetRelativePointVelocity
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
public [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) GetRelativePointVelocity([Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) relativePoint); 
### Description
The velocity relative to the articulation body at the point `relativePoint`.
Gets the velocity relative to the articulation body at the specified `relativePoint`.
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
    // This method assumes that the wheel is a child of the ArticulationBody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody.html), or that the wheel translates relative to the ArticulationBody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody.html).
    Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) CalcWheelVelocity(Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) localWheelPos)
    {
        return ab.GetRelativePointVelocity(localWheelPos);
    }
}

```

* * *
