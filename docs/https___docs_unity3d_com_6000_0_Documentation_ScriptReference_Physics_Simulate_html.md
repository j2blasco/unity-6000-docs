* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.Simulate.html

#  [Physics](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.html).Simulate
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
public static void Simulate(float step); 
### Parameters
Parameter | Description  
---|---  
step | The time to advance physics by.  
### Description
Simulate physics in the Scene.
Call this to simulate physics manually when the simulation mode is set to Script. Simulation includes all the stages of collision detection, rigidbody and joints integration, and filing of the physics callbacks (contact, trigger and joints). Calling Physics.Simulate does not cause FixedUpdate to be called. [MonoBehaviour.FixedUpdate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.FixedUpdate.html) will still be called at the rate defined by [Time.fixedDeltaTime](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-fixedDeltaTime.html) whether simulation mode is set to Script or not, and regardless of when you call Physics.Simulate.  
  
Note that if you pass framerate-dependent step values (such as [Time.deltaTime](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-deltaTime.html)) to the physics engine, your simulation will be non-deterministic because of the unpredictable fluctuations in framerate that can arise.  
  
To achieve deterministic physics results, you should pass a fixed step value to Physics.Simulate every time you call it. Usually, `step` should be a small positive number. Using `step` values greater than 0.03 is likely to produce inaccurate results.  
  
Additional resources: [Physics.simulationMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics-simulationMode.html), [SimulationMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SimulationMode.html).  
  
Here is an example of a basic simulation that implements what's being done in the [SimulationMode.FixedUpdate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SimulationMode.FixedUpdate.html) simulation mode (excluding [Time.maximumDeltaTime](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-maximumDeltaTime.html)).
```
using UnityEngine;  
  
public class BasicSimulation : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    private float timer;  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        if (Physics.simulationMode[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics-simulationMode.html) != SimulationMode.Script[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SimulationMode.Script.html))
            return; // do nothing if the automatic simulation is enabled  
  
        timer += Time.deltaTime[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-deltaTime.html);  
  
        // Catch up with the game time.
        // Advance the physics simulation in portions of Time.fixedDeltaTime[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-fixedDeltaTime.html)
        // Note that generally, we don't want to pass variable delta to Simulate as that leads to unstable results.
        while (timer >= Time.fixedDeltaTime[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-fixedDeltaTime.html))
        {
            timer -= Time.fixedDeltaTime[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-fixedDeltaTime.html);
            Physics.Simulate[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.Simulate.html)(Time.fixedDeltaTime[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-fixedDeltaTime.html));
        }  
  
        // Here you can access the transforms state right after the simulation, if needed
    }
}

```

* * *
