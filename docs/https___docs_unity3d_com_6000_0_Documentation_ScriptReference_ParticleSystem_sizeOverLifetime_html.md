* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem-sizeOverLifetime.html

#  [ParticleSystem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html).sizeOverLifetime
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
[ParticleSystem.SizeOverLifetimeModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.SizeOverLifetimeModule.html) sizeOverLifetime; 
### Description
Script interface for the SizeOverLifetimeModule of a Particle System. 
This module controls the size of particles throughout their lifetime.  
  
Particle System modules do not need to be reassigned back to the system; they are interfaces and not independent objects.
```
using UnityEngine;
using System.Collections;  
  
[RequireComponent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RequireComponent.html)(typeof(ParticleSystem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html)))]
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html) {
    void Start() {
        ParticleSystem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html) ps = GetComponent<ParticleSystem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html)>();
        var sz = ps.sizeOverLifetime;
        sz.enabled = true;  
  
        AnimationCurve[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationCurve.html) curve = new AnimationCurve[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationCurve.html)();
        curve.AddKey(0.0f, 0.1f);
        curve.AddKey(0.75f, 1.0f);  
  
        sz.size = new ParticleSystem.MinMaxCurve[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.MinMaxCurve.html)(1.5f, curve);
    }
}
```

* * *
