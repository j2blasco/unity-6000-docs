* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.GetParticles.html

#  [ParticleSystem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html).GetParticles
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
## Declaration
public int GetParticles(out Particle[] particles); 
## Declaration
public int GetParticles(out Particle[] particles, int size); 
## Declaration
public int GetParticles(out Particle[] particles, int size, int offset); 
## Declaration
public int GetParticles(out NativeArray<Particle> particles); 
## Declaration
public int GetParticles(out NativeArray<Particle> particles, int size); 
## Declaration
public int GetParticles(out NativeArray<Particle> particles, int size, int offset); 
### Parameters
Parameter | Description  
---|---  
particles | Output particle buffer, containing the current particle state.  
size | The number of elements that are read from the Particle System.  
offset | The offset into the active particle list, from which to copy the particles.  
### Returns
**int** The number of particles written to the input particle array (the number of particles currently alive). 
### Description
Gets the particles of this Particle System.
This method is allocation free as long the input "particles" array is preallocated once (see example below). The method only gets the particles that are currently alive in the Particle System when it is called, so it may only get a small part of the particles array.  
  
Additional resources: [Particle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.Particle.html), [SetParticles](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.SetParticles.html).
```
using UnityEngine;  
  
[RequireComponent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RequireComponent.html)(typeof(ParticleSystem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html)))]
public class ParticleFlow : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    ParticleSystem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html) m_System;
    ParticleSystem.Particle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.Particle.html)[] m_Particles;
    public float m_Drift = 0.01f;  
  
    private void LateUpdate()
    {
        InitializeIfNeeded();  
  
        // GetParticles is allocation free because we reuse the m_Particles buffer between updates
        int numParticlesAlive = m_System.GetParticles(m_Particles);  
  
        // Change only the particles that are alive
        for (int i = 0; i < numParticlesAlive; i++)
        {
            m_Particles[i].velocity += Vector3.up[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-up.html) * m_Drift;
        }  
  
        // Apply the particle changes to the Particle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.Particle.html) System[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VirtualTexturing.System.html)
        m_System.SetParticles(m_Particles, numParticlesAlive);
    }  
  
    void InitializeIfNeeded()
    {
        if (m_System == null)
            m_System = GetComponent<ParticleSystem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html)>();  
  
        if (m_Particles == null || m_Particles.Length < m_System.main.maxParticles)
            m_Particles = new ParticleSystem.Particle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.Particle.html)[m_System.main.maxParticles];
    }
}

```

* * *
