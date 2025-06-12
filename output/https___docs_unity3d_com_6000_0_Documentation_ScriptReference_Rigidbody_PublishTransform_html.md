* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.PublishTransform.html

#  [Rigidbody](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html).PublishTransform
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
public void PublishTransform(); 
### Description
Applies the [position](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody-position.html) and [rotation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody-rotation.html) of the Rigidbody to the corresponding [Transform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) component.
This is more efficient than setting [Transform.position](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform-position.html) and [Transform.rotation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform-rotation.html) manually.  
  
Note: This method doesn't update the child Transforms. It should be called from the topmost Transform, down the hierarchy.
```
using UnityEngine;  
  
public class PositionTracker : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    private PhysicsScene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsScene.html) m_SomeScene;
    private Rigidbody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html) m_Rigidbody;  
  
    public void SimulateTrajectory(float totalTime)
    {
        m_SomeScene.RunSimulationStages(0f, SimulationStage.PrepareSimulation[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SimulationStage.PrepareSimulation.html));  
  
        for (int i = 0; i < totalTime / Time.fixedDeltaTime[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-fixedDeltaTime.html); i++)
            m_SomeScene.RunSimulationStages(Time.fixedDeltaTime[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-fixedDeltaTime.html), SimulationStage.RunSimulation[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SimulationStage.RunSimulation.html));  
  
        // Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) of the m_Rigidbody is still like it was at the start of the method
        m_Rigidbody.PublishTransform();
        // Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) of the m_Rigidbody is now up to date and can be accessed to see where the body ended up after simulating for "totalTime" seconds
    }
}

```

Simulate a [PhysicsScene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsScene.html) with a [Rigidbody](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html) and use [PublishTransform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.PublishTransform.html) to read the information from the physics system to the [Transform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) component.
* * *
