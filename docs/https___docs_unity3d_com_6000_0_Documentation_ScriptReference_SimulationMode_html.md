* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SimulationMode.html

# SimulationMode
enumeration
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
### Description
A selection of modes that control when Unity executes the physics simulation.
Additional resources: [Physics.simulationMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics-simulationMode.html).
```
// SimulationMode.FixedUpdate[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SimulationMode.FixedUpdate.html) is the default setting in Unity.
// Attach this script to a gameObject and enter runtime mode.  
  
using UnityEngine;  
  
public class ManualPhysicsSimulation : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Current Physics.simulationMode[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics-simulationMode.html): " + Physics.simulationMode[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics-simulationMode.html));
    }
}

```

### Properties
Property | Description  
---|---  
[FixedUpdate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SimulationMode.FixedUpdate.html) | Use this enumeration to instruct Unity to execute the physics simulation immediately after the MonoBehaviour.FixedUpdate.  
[Update](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SimulationMode.Update.html) | Use this enumeration to instruct Unity to execute the physics simulation immediately after MonoBehaviour.Update.  
[Script](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SimulationMode.Script.html) | Use this enumeration to instruct Unity to execute the physics simulation manually when you call Physics.Simulate.  
* * *
