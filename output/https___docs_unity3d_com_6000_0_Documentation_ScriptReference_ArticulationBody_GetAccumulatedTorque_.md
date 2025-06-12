* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody.GetAccumulatedTorque.html

#  [ArticulationBody](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody.html).GetAccumulatedTorque
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
public [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) GetAccumulatedTorque(float step = Time.fixedDeltaTime); 
### Parameters
Parameter | Description  
---|---  
step | The timestep of the next physics simulation.  
### Returns
**Vector3** Accumulated torque expressed in [ForceMode.Force](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ForceMode.Force.html). 
### Description
Returns the torque that the [ArticulationBody](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody.html) has accumulated before the simulation step.
The accumulated torque is reset during each physics simulation step.
```
using UnityEngine;  
  
public class AddTorqueScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    private ArticulationBody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody.html) articulationBody;  
  
    void Start()
    {
        articulationBody = GetComponent<ArticulationBody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody.html)>();
        articulationBody.useGravity = false;
    }  
  
    private void FixedUpdate[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.FixedUpdate.html)()
    {
        articulationBody.AddTorque(Vector3.right[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-right.html) * 10f, ForceMode.Impulse[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ForceMode.Impulse.html));
        var accumulatedTorque = articulationBody.GetAccumulatedTorque();
        articulationBody.AddTorque(accumulatedTorque * -1f, ForceMode.Force[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ForceMode.Force.html));
    }
}

```

In this example, the angular velocity of the ArticulationBody is 0.
* * *
