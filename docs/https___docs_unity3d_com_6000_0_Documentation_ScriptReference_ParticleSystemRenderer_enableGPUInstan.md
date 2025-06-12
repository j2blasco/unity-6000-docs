* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemRenderer-enableGPUInstancing.html

#  [ParticleSystemRenderer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemRenderer.html).enableGPUInstancing
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
enableGPUInstancing; 
### Description
Enables GPU Instancing on platforms that support it.
To use GPU Instancing to render a Particle System, the particle must use a Shader that contains a Procedural Instancing pass (that is, it contains the `#pragma instancing_options procedural` directive).
```
using UnityEngine;
using System.Collections;
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    private ParticleSystem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html) ps;
    private ParticleSystemRenderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemRenderer.html) psr;
    private bool enableGPUInstancing = true;  
  
    void Start()
    {
        ps = GetComponent<ParticleSystem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html)>();
        psr = GetComponent<ParticleSystemRenderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemRenderer.html)>();  
  
        psr.renderMode = ParticleSystemRenderMode.Mesh[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemRenderMode.Mesh.html);
        psr.SetMeshes(new Mesh[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html)[] { Resources.GetBuiltinResource<Mesh[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html)>("Capsule.fbx"), Resources.GetBuiltinResource<Mesh[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html)>("Cube.fbx"), Resources.GetBuiltinResource<Mesh[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html)>("Sphere.fbx") });  
  
        psr.sharedMaterial = new Material[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html)(Shader.Find[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.Find.html)("Particles/Standard Surface"));
    }  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        psr.enableGPUInstancing = enableGPUInstancing;
    }  
  
    void OnGUI()
    {
        enableGPUInstancing = GUI.Toggle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Toggle.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(25, 45, 200, 30), enableGPUInstancing, "Enabled");
    }
}

```

* * *
