* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.MainModule-stopAction.html

#  [ParticleSystem.MainModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.MainModule.html).stopAction
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
[ParticleSystemStopAction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemStopAction.html) stopAction; 
### Description
Select whether to Disable or Destroy the GameObject, or to call the [MonoBehaviour.OnParticleSystemStopped](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.OnParticleSystemStopped.html) script Callback, when the Particle System stops and all particles have died.
```
using UnityEngine;
using System.Collections;  
  
[RequireComponent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RequireComponent.html)(typeof(ParticleSystem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html)))]
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    private ParticleSystem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html) ps;  
  
    void Start()
    {
        ps = GetComponent<ParticleSystem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html)>();
        ps.Stop();  
  
        var main = ps.main;
        main.loop = false;
        main.duration = 1.0f;
        main.stopAction = ParticleSystemStopAction.Destroy[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemStopAction.Destroy.html);  
  
        ps.Play();
    }
}

```

* * *
