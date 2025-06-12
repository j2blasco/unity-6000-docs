* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody.PublishTransform.html

#  [ArticulationBody](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody.html).PublishTransform
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
public void PublishTransform(); 
### Description
Reads the position and rotation of the Articulation Body from the physics system and applies it to the corresponding [Transform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) component.
Note: This method doesn't update the child Transforms. It should be called from the topmost Transform, down the hierarchy.
```
using System.Linq;
using UnityEngine;  
  
public class ExampleScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    private PhysicsScene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsScene.html) m_SomeScene;
    private ArticulationBody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody.html) m_RootArticulation;  
  
    public void SimulateTrajectory(float totalTime)
    {
        m_SomeScene.RunSimulationStages(0f, SimulationStage.PrepareSimulation[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SimulationStage.PrepareSimulation.html));  
  
        for (int i = 0; i < totalTime / Time.fixedDeltaTime[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-fixedDeltaTime.html); i++)
            m_SomeScene.RunSimulationStages(Time.fixedDeltaTime[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-fixedDeltaTime.html), SimulationStage.RunSimulation[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SimulationStage.RunSimulation.html));  
  
        // Transforms of the ArticulationBody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody.html) tree are still like they were at the start of the method  
  
        var links = m_RootArticulation.gameObject.GetComponentsInChildren<ArticulationBody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody.html)>().ToList();
        links.Sort((a0, a1) => a0.index.CompareTo(a1.index));
        foreach (var ab in links)
            ab.PublishTransform();  
  
        // Transforms of the ArticulationBody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody.html) tree are now up to date and can be accessed to see where the bodies ended up after simulating for "totalTime" seconds
    }  
  
    // Teleports the root body of the Articulation and applies the resulting position and rotation to the Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) component
    public void TeleportAndUpdate(Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) position, Quaternion[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html) rotation)
    {
        m_RootArticulation.TeleportRoot(position, rotation);
        m_RootArticulation.PublishTransform();
    }
}

```

Simulate a [PhysicsScene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsScene.html) with an [ArticulationBody](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody.html) and use [PublishTransform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody.PublishTransform.html) to read the information from the physics system to the [Transform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) component.
* * *
