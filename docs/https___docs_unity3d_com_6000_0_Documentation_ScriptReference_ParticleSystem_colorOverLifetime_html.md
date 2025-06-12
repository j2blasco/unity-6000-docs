* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem-colorOverLifetime.html

#  [ParticleSystem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html).colorOverLifetime
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
[ParticleSystem.ColorOverLifetimeModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.ColorOverLifetimeModule.html) colorOverLifetime; 
### Description
Script interface for the ColorOverLifetimeModule of a Particle System.
This module changes the colors assigned to particles over time, based on how long each particle has been alive.  
  
Particle System modules do not need to be reassigned back to the system; they are interfaces and not independent objects.
```
using UnityEngine;
using System.Collections;  
  
[RequireComponent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RequireComponent.html)(typeof(ParticleSystem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html)))]
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html) {
    void Start() {
        ParticleSystem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html) ps = GetComponent<ParticleSystem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html)>();
        var col = ps.colorOverLifetime;
        col.enabled = true;  
  
        Gradient[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gradient.html) grad = new Gradient[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gradient.html)();
        grad.SetKeys( new GradientColorKey[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GradientColorKey.html)[] { new GradientColorKey[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GradientColorKey.html)(Color.blue[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-blue.html), 0.0f), new GradientColorKey[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GradientColorKey.html)(Color.red[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-red.html), 1.0f) }, new GradientAlphaKey[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GradientAlphaKey.html)[] { new GradientAlphaKey[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GradientAlphaKey.html)(1.0f, 0.0f), new GradientAlphaKey[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GradientAlphaKey.html)(0.0f, 1.0f) } );  
  
        col.color = grad;
    }
}
```

* * *
