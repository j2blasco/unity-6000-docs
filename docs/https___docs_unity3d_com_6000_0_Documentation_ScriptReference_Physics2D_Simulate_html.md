* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics2D.Simulate.html

#  [Physics2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics2D.html).Simulate
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
public static bool Simulate(float deltaTime, int simulationLayers = Physics2D.AllLayers); 
### Parameters
Parameter | Description  
---|---  
deltaTime | The time to advance physics by.  
simulationLayers | The [Rigidbody2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html) and [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) layers to simulate.  
### Returns
**bool** Whether the simulation was run or not. Running the simulation during physics callbacks will always fail. 
### Description
Simulate physics in the default physics scene.
Calling [Physics2D.Simulate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics2D.Simulate.html) will perform a single simulation step, simulating physics over the specified `step` time.  
  
By default, [All Layers](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics2D.AllLayers.html) are simulated, however if you specify layers then only the [Rigidbody2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html) on those layers will be simulated. Along with this, only contacts for [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) on the specified layer(s) will be handled. Finally, only [joints](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Joint2D.html) or [effectors](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Effector2D.html) on the specified layer(s) will be handled.  
  
You can call [Physics2D.Simulate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics2D.Simulate.html) in the Editor outside of play mode, however caution is advised as this will cause the simulation to move GameObjects that have an attached [Rigidbody2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html) component. When simulating in the Editor outside of play mode, a full simulation occurs for all physics components including [Rigidbody2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html), [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html), [Joint2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Joint2D.html) and [Effector2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Effector2D.html), and contacts are generated. However, contacts are not reported via the standard script callbacks. This is a safety measure to prevent callbacks from deleting objects in the Scene, which is not an undoable operation.  
  
**NOTE:** Calling [Physics2D.Simulate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics2D.Simulate.html) does not cause Unity to call FixedUpdate. Unity still calls [MonoBehaviour.FixedUpdate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.FixedUpdate.html) at the rate defined by [Time.fixedDeltaTime](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-fixedDeltaTime.html) whether automatic simulation is on or off, and regardless of when you call Physics2D.Simulate. Also, if you pass framerate-dependent step values (such as [Time.deltaTime](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-deltaTime.html)) to the physics engine, your simulation will be less deterministic because of the unpredictable fluctuations in framerate that can arise. To achieve more deterministic physics results, you should pass a fixed step value to Physics2D.Simulate every time you call it.  
  
Additional resources: [Physics2D.simulationMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics2D-simulationMode.html) and [PhysicsScene2D.Simulate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsScene2D.Simulate.html).  
  
Here is an example of a basic simulation that implements what's being done in the automatic simulation mode.
```
using UnityEngine;  
  
public class BasicSimulation : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    private float timer;  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        if (Physics2D.simulationMode[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics2D-simulationMode.html) != SimulationMode2D.Script[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SimulationMode2D.Script.html))
            return; // do nothing if simulation is not set to be executed via script.  
  
        timer += Time.deltaTime[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-deltaTime.html);  
  
        // Catch up with the game time.
        // Advance the physics simulation in portions of Time.fixedDeltaTime[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-fixedDeltaTime.html)
        // Note that generally, we don't want to pass variable delta to Simulate as that leads to unstable results.
        while (timer >= Time.fixedDeltaTime[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-fixedDeltaTime.html))
        {
            timer -= Time.fixedDeltaTime[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-fixedDeltaTime.html);
            Physics2D.Simulate[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics2D.Simulate.html)(Time.fixedDeltaTime[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-fixedDeltaTime.html));
        }  
  
        // Here you can access the transforms state right after the simulation, if needed...
    }
}

```

* * *
