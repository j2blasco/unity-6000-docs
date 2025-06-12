* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem-emission.html

#  [ParticleSystem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html).emission
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
[ParticleSystem.EmissionModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.EmissionModule.html) emission; 
### Description
Script interface for the EmissionModule of a Particle System.
This module provides control over how many particles are emitted.  
  
Particle System modules do not need to be reassigned back to the system; they are interfaces and not independent objects.
```
// Create a Particle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.Particle.html) System[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VirtualTexturing.System.html)
// At 2 and 4 secs the number of particles are changed to 100, then 200
using UnityEngine;
using System.Collections;  
  
[RequireComponent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RequireComponent.html)(typeof(ParticleSystem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html)))]
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        ParticleSystem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html) ps = GetComponent<ParticleSystem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html)>();
        var em = ps.emission;
        em.enabled = true;  
  
        em.rateOverTime = 20.0f;  
  
        em.SetBursts(
            new ParticleSystem.Burst[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.Burst.html)[]{
                new ParticleSystem.Burst[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.Burst.html)(2.0f, 100),
                new ParticleSystem.Burst[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.Burst.html)(4.0f, 100)
            });
    }
}
```

* * *
