* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemRenderer.SetMeshWeightings.html

#  [ParticleSystemRenderer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemRenderer.html).SetMeshWeightings
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
## Declaration
public void SetMeshWeightings(float[] weightings, int size); 
## Declaration
public void SetMeshWeightings(float[] weightings); 
### Parameters
Parameter | Description  
---|---  
weightings | The array of weights to use.  
size | The number of elements from the weighting array to apply.  
### Description
Sets the weights that the [ParticleSystemRenderer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemRenderer.html) uses to assign Meshes to particles.
The [ParticleSystemRenderer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemRenderer.html) only uses these weights if you set [ParticleSystemRenderer.renderMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemRenderer-renderMode.html) to [ParticleSystemRenderMode.Mesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemRenderMode.Mesh.html) and set [ParticleSystemRenderer.meshDistribution](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemRenderer-meshDistribution.html) to [ParticleSystemMeshDistribution.NonUniformRandom](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemMeshDistribution.NonUniformRandom.html).
The weightings are relative to each other but can be any positive value. For example, if you set the weights to 6 and 3, the ParticleSystemRenderer randomly selects the first Mesh approximately twice as often as the second Mesh. It can be most intuitive to use percentages for the weightings and ensure that the sum of the weightings adds up to 100, but this is not a requirement.
```
using UnityEngine;
using System.Collections;  
  
[RequireComponent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RequireComponent.html)(typeof(ParticleSystem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html)))]
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    private ParticleSystem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html) ps;
    private ParticleSystemRenderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemRenderer.html) psr;  
  
    void Start() {  
  
        ps = GetComponent<ParticleSystem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html)>();
        psr = GetComponent<ParticleSystemRenderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemRenderer.html)>();  
  
        psr.renderMode = ParticleSystemRenderMode.Mesh[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemRenderMode.Mesh.html);
        psr.meshDistribution = ParticleSystemMeshDistribution.NonUniformRandom[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemMeshDistribution.NonUniformRandom.html);
        psr.SetMeshes(new Mesh[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html)[]{ Resources.GetBuiltinResource<Mesh[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html)>("Capsule.fbx"), Resources.GetBuiltinResource<Mesh[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html)>("Cube.fbx"), Resources.GetBuiltinResource<Mesh[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html)>("Sphere.fbx") });
        psr.SetMeshWeightings(new float[]{ 0.1f, 0.1f, 0.8f });
    }  
  
    void OnGUI() {
        GUI.Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Label.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(25, 40, 200, 30), "Mesh[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html) Count: " + psr.meshCount.ToString());
    }
}
```

* * *
