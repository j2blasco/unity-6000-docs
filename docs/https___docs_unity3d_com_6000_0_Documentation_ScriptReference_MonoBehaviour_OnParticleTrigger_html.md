* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.OnParticleTrigger.html

#  [MonoBehaviour](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html).OnParticleTrigger()
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-MonoBehaviour.html "Go to MonoBehaviour Component in the Manual")
### Description
OnParticleTrigger is called when any particles in a Particle System meet the conditions in the trigger module.
This can be used to kill or modify particles that are inside or outside a collision volume.
```
using UnityEngine;
using System.Collections;
using System.Collections.Generic;  
  
public class TriggerScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void OnParticleTrigger()
    {
        ParticleSystem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html) ps = GetComponent<ParticleSystem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html)>();  
  
        // particles
        List<ParticleSystem.Particle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.Particle.html)> enter = new List<ParticleSystem.Particle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.Particle.html)>();
        List<ParticleSystem.Particle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.Particle.html)> exit = new List<ParticleSystem.Particle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.Particle.html)>();  
  
        // get
        int numEnter = ps.GetTriggerParticles(ParticleSystemTriggerEventType.Enter[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemTriggerEventType.Enter.html), enter);
        int numExit = ps.GetTriggerParticles(ParticleSystemTriggerEventType.Exit[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemTriggerEventType.Exit.html), exit);  
  
        // iterate
        for (int i = 0; i < numEnter; i++)
        {
            ParticleSystem.Particle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.Particle.html) p = enter[i];
            p.startColor = new Color32[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color32.html)(255, 0, 0, 255);
            enter[i] = p;
        }
        for (int i = 0; i < numExit; i++)
        {
            ParticleSystem.Particle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.Particle.html) p = exit[i];
            p.startColor = new Color32[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color32.html)(0, 255, 0, 255);
            exit[i] = p;
        }  
  
        // set
        ps.SetTriggerParticles(ParticleSystemTriggerEventType.Enter[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemTriggerEventType.Enter.html), enter);
        ps.SetTriggerParticles(ParticleSystemTriggerEventType.Exit[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemTriggerEventType.Exit.html), exit);
    }
}

```

In order to retrieve detailed information about all the collisions caused by the [ParticleSystem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html), [ParticlePhysicsExtensions.GetTriggerParticles](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticlePhysicsExtensions.GetTriggerParticles.html) must be used to retrieve the array of [Particle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.Particle.html).
* * *
