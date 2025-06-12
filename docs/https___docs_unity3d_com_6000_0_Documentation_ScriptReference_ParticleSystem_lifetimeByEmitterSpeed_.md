* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem-lifetimeByEmitterSpeed.html

#  [ParticleSystem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html).lifetimeByEmitterSpeed
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ParticleSystem.html "Go to ParticleSystem Component in the Manual")
[ParticleSystem.LifetimeByEmitterSpeedModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.LifetimeByEmitterSpeedModule.html) lifetimeByEmitterSpeed; 
### Description
Script interface for the Particle System Lifetime By Emitter Speed module.
This module controls the initial lifetime of each particle based on the speed of the emitter when the particle was spawned.  
  
Particle System modules do not need to be reassigned back to the system; they are interfaces and not independent objects.
```
using UnityEngine;
using System.Collections;  
  
[RequireComponent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RequireComponent.html)(typeof(ParticleSystem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html)))]
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    private ParticleSystem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html) ps;
    public bool moduleEnabled = true;
    public float maxSpeed = 5.0f;
    public AnimationCurve[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationCurve.html) curve = AnimationCurve.EaseInOut[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationCurve.EaseInOut.html)(0.0f, 1.0f, 1.0f, 0.2f);  
  
    void Start()
    {
        ps = GetComponent<ParticleSystem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html)>();  
  
        var mainModule = ps.main;
        mainModule.startLifetime = 1.0f;  
  
        // make particles less random to more clearly see effect of lifetime.
        var shapeModule = ps.shape;
        shapeModule.radius = 0.1f;
        shapeModule.angle = 1.0f;  
  
        var main = ps.main;
        main.simulationSpace = ParticleSystemSimulationSpace.World[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemSimulationSpace.World.html);  
  
        // add a sphere so we can see our transform position as it moves
        var sphere = GameObject.CreatePrimitive[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.CreatePrimitive.html)(PrimitiveType.Sphere[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrimitiveType.Sphere.html));
        sphere.transform.parent = ps.transform;
    }  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        var lifetimeByEmitterSpeed = ps.lifetimeByEmitterSpeed;
        lifetimeByEmitterSpeed.enabled = moduleEnabled;
        lifetimeByEmitterSpeed.range = new Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html)(0, maxSpeed);
        lifetimeByEmitterSpeed.curve = new ParticleSystem.MinMaxCurve[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.MinMaxCurve.html)(1f, curve);  
  
        ps.transform.position = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(Mathf.Sin[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.Sin.html)(Time.time[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-time.html) * 2.0f) * 4.0f, 0.0f, 0.0f);
    }  
  
    void OnGUI()
    {
        moduleEnabled = GUI.Toggle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Toggle.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(25, 45, 100, 30), moduleEnabled, "Enabled");
        maxSpeed = GUI.HorizontalSlider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.HorizontalSlider.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(25, 85, 100, 30), maxSpeed, 0.0f, 10.0f);
    }
}

```

* * *
