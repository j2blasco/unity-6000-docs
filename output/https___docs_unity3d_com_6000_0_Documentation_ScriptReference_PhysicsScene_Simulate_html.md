* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsScene.Simulate.html

#  [PhysicsScene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsScene.html).Simulate
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
public void Simulate(float step); 
### Parameters
Parameter | Description  
---|---  
step | The time to advance physics by.  
### Returns
**void** Whether the simulation was run or not. Running the simulation during physics callbacks will always fail. 
### Description
Simulate physics associated with this [PhysicsScene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsScene.html).
Calling this method causes the physics to be simulated over the specified `step` time. Only the physics associated with this [PhysicsScene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsScene.html) will be simulated. If this [PhysicsScene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsScene.html) is not the default physics Scene (see [Physics.defaultPhysicsScene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics-defaultPhysicsScene.html)) then it is associated with a specific [Scene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) and as such, only components added to that [Scene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) are affected when running the simulation.  
  
If you pass framerate-dependent step values (such as [Time.deltaTime](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-deltaTime.html)) to the physics engine, your simulation will be less deterministic because of the unpredictable fluctuations in framerate that can arise. To achieve more deterministic physics results, you should pass a fixed step value to [PhysicsScene.Simulate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsScene.Simulate.html) every time you call it.  
  
You can call [PhysicsScene.Simulate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsScene.Simulate.html) in the Editor outside of play mode however caution is advised as this will cause the simulation to move GameObject that have a [Rigidbody](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html) component attached. When simulating in the Editor outside of play mode, a full simulation occurs for all physics components including [Rigidbody](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html), [Collider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html) and [Joint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Joint.html) including the generation of contacts however contacts are not reported via the standard script callbacks. This is a safety measure to prevent allowing callbacks to delete objects in the Scene which would not be an undoable operation. Here is an example of a basic simulation that implements what's being done in the automatic simulation mode.
```
using UnityEngine;
using UnityEngine.SceneManagement;  
  
public class MultiScenePhysics : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    private Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) extraScene;  
  
    public void Start()
    {
        // First create an extra scene with local physics
        extraScene = SceneManager.CreateScene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.SceneManager.CreateScene.html)("Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html)", new CreateSceneParameters[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.CreateSceneParameters.html)(LocalPhysicsMode.Physics3D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.LocalPhysicsMode.Physics3D.html)));  
  
        // Mark the scene active, so that all the new GameObjects end up in the newly created scene
        SceneManager.SetActiveScene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.SceneManager.SetActiveScene.html)(extraScene);  
  
        PopulateExtraSceneWithObjects();
    }  
  
    public void FixedUpdate[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.FixedUpdate.html)()
    {
        // All of the non-default physics scenes need to be simulated manually
        var physicsScene = extraScene.GetPhysicsScene();
        physicsScene.Simulate(Time.fixedDeltaTime[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-fixedDeltaTime.html));
    }  
  
    public void PopulateExtraSceneWithObjects()
    {
        // Create GameObjects for physics simulation
        var sphere = GameObject.CreatePrimitive[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.CreatePrimitive.html)(PrimitiveType.Sphere[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrimitiveType.Sphere.html));
        sphere.AddComponent<Rigidbody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html)>();
        sphere.transform.position = Vector3.up[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-up.html) * 4;
    }
}

```

Additional resources: [Physics.Simulate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.Simulate.html).
* * *
