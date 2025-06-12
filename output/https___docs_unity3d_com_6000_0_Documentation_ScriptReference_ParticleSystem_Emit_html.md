* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.Emit.html

#  [ParticleSystem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html).Emit
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
public void Emit(int count); 
### Parameters
Parameter | Description  
---|---  
count | Number of particles to emit.  
### Description
Emit `count` particles immediately.
* * *
## Declaration
public void Emit([ParticleSystem.EmitParams](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.EmitParams.html) emitParams, int count); 
### Parameters
Parameter | Description  
---|---  
emitParams | Overidden particle properties.  
count | Number of particles to emit.  
### Description
Emit a number of particles from script.
Setting properties in the emitParams will override those properties in the emitted particles. Any properties not modified will inherit the behavior specified in the inspector.
```
using UnityEngine;  
  
// In this example, we have a Particle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.Particle.html) System[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VirtualTexturing.System.html) emitting green particles; we then emit and override some properties every 2 seconds.
public class EmitExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public ParticleSystem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html) system;  
  
    void Start()
    {
        // A simple particle material with no texture.
        Material[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html) particleMaterial = new Material[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html)(Shader.Find[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.Find.html)("Particles/Standard Unlit"));  
  
        // Create a green Particle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.Particle.html) System[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VirtualTexturing.System.html).
        var go = new GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)("Particle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.Particle.html) System[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VirtualTexturing.System.html)");
        go.transform.Rotate(-90, 0, 0); // Rotate[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Rotate.html) so the system emits upwards.
        system = go.AddComponent<ParticleSystem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html)>();
        go.GetComponent<ParticleSystemRenderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemRenderer.html)>().material = particleMaterial;
        var mainModule = system.main;
        mainModule.startColor = Color.green[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-green.html);
        mainModule.startSize = 0.5f;  
  
        // Every 2 secs we will emit.
        InvokeRepeating("DoEmit", 2.0f, 2.0f);
    }  
  
    void DoEmit()
    {
        // Any parameters we assign in emitParams will override the current system's when we call Emit.
        // Here we will override the start color and size.
        var emitParams = new ParticleSystem.EmitParams[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.EmitParams.html)();
        emitParams.startColor = Color.red[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-red.html);
        emitParams.startSize = 0.2f;
        system.Emit(emitParams, 10);
        system.Play(); // Continue normal emissions
    }
}

```

* * *
