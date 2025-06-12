* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.Particle-startLifetime.html

#  [ParticleSystem.Particle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.Particle.html).startLifetime
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
startLifetime; 
### Description
The starting lifetime of the particle.
This is the total lifetime of this particle in seconds. The Particle System sets this value when it first spawns the particle.
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        ParticleSystem.Particle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.Particle.html) particle = new ParticleSystem.Particle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.Particle.html)();  
  
        // Calculate how long the particle has been alive.
        float timeAlive = particle.startLifetime - particle.lifetime;
    }
}

```

* * *
