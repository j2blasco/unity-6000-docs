* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.OnParticleSystemStopped.html

#  [MonoBehaviour](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html).OnParticleSystemStopped()
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
OnParticleSystemStopped is called when all particles in the system have died, and no new particles will be born. New particles cease to be created either after Stop is called, or when the duration property of a non-looping system has been exceeded.
This can be used to notify a script of when a Particle System has finished. In order to receive the callback, you must set the [ParticleSystem.MainModule.stopAction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.MainModule-stopAction.html) property to Callback.
```
using UnityEngine;
using System.Collections;
using System.Collections.Generic;  
  
public class StoppedScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        var main = GetComponent<ParticleSystem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html)>().main;
        main.stopAction = ParticleSystemStopAction.Callback[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemStopAction.Callback.html);
    }  
  
    void OnParticleSystemStopped()
    {
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("System[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VirtualTexturing.System.html) has stopped!");
    }
}

```

In order to retrieve detailed information about all the collisions caused by the [ParticleSystem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html), you must use [ParticlePhysicsExtensions.GetTriggerParticles](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticlePhysicsExtensions.GetTriggerParticles.html) to retrieve the array of [Particle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.Particle.html).
* * *
