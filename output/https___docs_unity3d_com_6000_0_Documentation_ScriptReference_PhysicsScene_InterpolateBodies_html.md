* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsScene.InterpolateBodies.html

#  [PhysicsScene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsScene.html).InterpolateBodies
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
## Declaration
public void InterpolateBodies(); 
### Description
Interpolates Rigidbodies in this [PhysicsScene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsScene.html).
Interpolates all Rigidbodies in this [PhysicsScene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsScene.html) with [Rigidbody.interpolation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody-interpolation.html) set to either [RigidbodyInterpolation.Interpolate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RigidbodyInterpolation.Interpolate.html) or [RigidbodyInterpolation.Extrapolate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RigidbodyInterpolation.Extrapolate.html) with the current [Time.time](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-time.html) value.  
  
This method is called automatically for the default [PhysicsScene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsScene.html) and therefore any manual calls on the [defaultPhysicsScene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics-defaultPhysicsScene.html) will fail.  
  
Additional resources: [PhysicsScene.Simulate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsScene.Simulate.html), [PhysicsScene.ResetInterpolationPoses](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsScene.ResetInterpolationPoses.html).
```
using UnityEngine;  
  
public class SimpleSimulator : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    private PhysicsScene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsScene.html) m_PhysicsScene;  
  
    private void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        m_PhysicsScene.InterpolateBodies();
    }  
  
    private void FixedUpdate[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.FixedUpdate.html)()
    {
        m_PhysicsScene.ResetInterpolationPoses();
        m_PhysicsScene.Simulate(Time.fixedDeltaTime[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-fixedDeltaTime.html));
    }
}

```

Simulates and interpolates a non-default [PhysicsScene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsScene.html).
* * *
