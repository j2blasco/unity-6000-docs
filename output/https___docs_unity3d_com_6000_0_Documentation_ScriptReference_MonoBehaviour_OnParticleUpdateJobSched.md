* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.OnParticleUpdateJobScheduled.html

#  [MonoBehaviour](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html).OnParticleUpdateJobScheduled()
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
OnParticleUpdateJobScheduled is called when a Particle System's built-in update job has been scheduled.
This can be used to attach custom managed jobs to run after the default particle update.
```
using UnityEngine;
using UnityEngine.ParticleSystemJobs;  
  
public class JobScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void OnParticleUpdateJobScheduled()
    {
        ParticleSystem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html) ps = GetComponent<ParticleSystem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html)>();
        new UpdateParticlesJob { m_DeltaTime = Time.deltaTime[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-deltaTime.html) }.Schedule(ps);
    }  
  
    struct UpdateParticlesJob : IJobParticleSystem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemJobs.IJobParticleSystem.html)
    {
        public float m_DeltaTime;  
  
        public void Execute(ParticleSystemJobData[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemJobs.ParticleSystemJobData.html) particles)
        {
            var positionsY = particles.positions.x;  
  
            for (int i = 0; i < particles.count; i++)
            {
                positionsY[i] += 3.0f * m_DeltaTime;
            }
        }
    }
}

```

In order to retrieve detailed information about all the collisions caused by the [ParticleSystem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html), [ParticlePhysicsExtensions.GetTriggerParticles](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticlePhysicsExtensions.GetTriggerParticles.html) must be used to retrieve the array of [Particle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.Particle.html).
* * *
