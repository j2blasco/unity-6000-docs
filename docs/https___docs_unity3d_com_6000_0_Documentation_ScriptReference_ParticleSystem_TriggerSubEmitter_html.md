* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.TriggerSubEmitter.html

#  [ParticleSystem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html).TriggerSubEmitter
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
public void TriggerSubEmitter(int subEmitterIndex); 
### Parameters
Parameter | Description  
---|---  
subEmitterIndex | Index of the sub emitter to trigger.  
### Description
Triggers the specified sub emitter on all particles of the Particle System.
```
using UnityEngine;  
  
// Add a manual sub-emitter
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    private ParticleSystem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html) ps;
    private float m_Timer = 0.0f;
    public float m_Interval = 2.0f;  
  
    void Start()
    {
        // A simple particle material with no texture.
        Material[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html) particleMaterial = new Material[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html)(Shader.Find[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.Find.html)("Particles/Standard Unlit"));  
  
        // Create a green Particle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.Particle.html) System[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VirtualTexturing.System.html).
        var rootSystemGO = new GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)("Particle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.Particle.html) System[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VirtualTexturing.System.html)");
        rootSystemGO.transform.Rotate(-90, 0, 0); // Rotate[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Rotate.html) so the system emits upwards.
        ps = rootSystemGO.AddComponent<ParticleSystem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html)>();
        rootSystemGO.GetComponent<ParticleSystemRenderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemRenderer.html)>().material = particleMaterial;
        var mainModule = ps.main;
        mainModule.startColor = Color.green[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-green.html);
        mainModule.startSize = 0.5f;  
  
        // Create our sub-emitter and setup bursts.
        var subSystemGO = new GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)("Particle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.Particle.html) System[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VirtualTexturing.System.html)");
        var subParticleSystem = subSystemGO.AddComponent<ParticleSystem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html)>();
        subSystemGO.GetComponent<ParticleSystemRenderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemRenderer.html)>().material = particleMaterial;
        var subMainModule = subParticleSystem.main;
        subMainModule.startColor = Color.red[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-red.html);
        subMainModule.startSize = 0.25f;
        var emissionModule = subParticleSystem.emission;
        emissionModule.SetBursts(new ParticleSystem.Burst[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.Burst.html)[] { new ParticleSystem.Burst[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.Burst.html)(0.0f, 4) }); // We will emit 10 particles when triggered.  
  
        // Set up the sub-emitter.
        subSystemGO.transform.SetParent(rootSystemGO.transform);
        var subEmittersModule = ps.subEmitters;
        subEmittersModule.enabled = true;
        subEmittersModule.AddSubEmitter(subParticleSystem, ParticleSystemSubEmitterType.Manual[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemSubEmitterType.Manual.html), ParticleSystemSubEmitterProperties.InheritNothing[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemSubEmitterProperties.InheritNothing.html));
    }  
  
    private void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        m_Timer += Time.deltaTime[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-deltaTime.html);
        while (m_Timer >= m_Interval)
        {
            ps.TriggerSubEmitter(0);
            m_Timer -= m_Interval;
        }
    }
}

```

* * *
## Declaration
public void TriggerSubEmitter(int subEmitterIndex, ref [ParticleSystem.Particle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.Particle.html) particle); 
## Declaration
public void TriggerSubEmitter(int subEmitterIndex, List<Particle> particles); 
### Parameters
Parameter | Description  
---|---  
subEmitterIndex | Index of the sub emitter to trigger.  
particle | Triggers the sub emtter on a single particle.  
particles | Triggers the sub emtter on a list of particles.  
### Description
Triggers the specified sub emitter on the specified particle(s) of the Particle System.
* * *
