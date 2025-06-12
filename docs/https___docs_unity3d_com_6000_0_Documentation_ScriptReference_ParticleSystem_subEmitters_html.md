* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem-subEmitters.html

#  [ParticleSystem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html).subEmitters
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
[ParticleSystem.SubEmittersModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.SubEmittersModule.html) subEmitters; 
### Description
Script interface for the SubEmittersModule of a Particle System.
The triggering of the child particle emission is linked to events such as the birth, death and collision of particles in the parent system.  
  
Particle System modules do not need to be reassigned back to the system; they are interfaces and not independent objects.
```
using UnityEngine;
using System.Collections;  
  
// A simple example showing access.
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html) {  
  
    public ParticleSystem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html) mySubEmitter;  
  
    void Start() {
        ParticleSystem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html) ps = GetComponent<ParticleSystem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html)>();
        var sub = ps.subEmitters;
        sub.enabled = true;
        sub.AddSubEmitter(mySubEmitter, ParticleSystemSubEmitterType.Death[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemSubEmitterType.Death.html), ParticleSystemSubEmitterProperties.InheritNothing[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemSubEmitterProperties.InheritNothing.html));
    }
}
```

```
using UnityEngine;  
  
// An example showing how to create 2 Particle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.Particle.html) Systems; one as a sub-emitter.
public class SubEmitterDeathExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start ()
    {
        // A simple particle material with no texture.
        Material[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html) particleMaterial = new Material[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html)(Shader.Find[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.Find.html)("Particles/Standard Unlit"));  
  
        // Create a green Particle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.Particle.html) System[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VirtualTexturing.System.html).
        var rootSystemGO = new GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)("Particle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.Particle.html) System[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VirtualTexturing.System.html)");
        rootSystemGO.transform.Rotate(-90, 0, 0); // Rotate[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Rotate.html) so the system emits upwards.
        var rootParticleSystem = rootSystemGO.AddComponent<ParticleSystem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html)>();
        rootSystemGO.GetComponent<ParticleSystemRenderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemRenderer.html)>().material = particleMaterial;
        var mainModule = rootParticleSystem.main;
        mainModule.startColor = Color.green[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-green.html);
        mainModule.startSize = 0.5f;  
  
        // Create our sub-emitter and set up bursts.
        var subSystemGO = new GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)("Particle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.Particle.html) System[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VirtualTexturing.System.html)");
        var subParticleSystem = subSystemGO.AddComponent<ParticleSystem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html)>();
        subSystemGO.GetComponent<ParticleSystemRenderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemRenderer.html)>().material = particleMaterial;
        var subMainModule = subParticleSystem.main;
        subMainModule.startColor = Color.red[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-red.html);
        subMainModule.startSize = 0.25f;
        var emissionModule = subParticleSystem.emission;
        emissionModule.SetBursts(new ParticleSystem.Burst[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.Burst.html)[] { new ParticleSystem.Burst[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.Burst.html)(0.0f, 10) }); // We will emit 10 particles upon death.  
  
        // Set up the sub-emitter.
        subSystemGO.transform.SetParent(rootSystemGO.transform);
        var subEmittersModule = rootParticleSystem.subEmitters;
        subEmittersModule.enabled = true;
        subEmittersModule.AddSubEmitter(subParticleSystem, ParticleSystemSubEmitterType.Death[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemSubEmitterType.Death.html), ParticleSystemSubEmitterProperties.InheritNothing[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemSubEmitterProperties.InheritNothing.html));
    }
}

```

* * *
