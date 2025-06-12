* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem-customData.html

#  [ParticleSystem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html).customData
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
[ParticleSystem.CustomDataModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.CustomDataModule.html) customData; 
### Description
Script interface for the CustomDataModule of a Particle System.
Once configured, this module will generate custom per-particle data, which you can use either in script or shaders. To read the data from script, simply call [ParticleSystem.GetCustomParticleData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.GetCustomParticleData.html). To read it in a shader, enable the custom data streams in the [ParticleSystemRenderer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemRenderer.html) Module, or call [ParticleSystemRenderer.SetActiveVertexStreams](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemRenderer.SetActiveVertexStreams.html) from script. Once enabled, the custom data will be passed to your vertex shader through a TEXCOORD channel. The [ParticleSystemRenderer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemRenderer.html) Inspector will tell you which channels are being used.  
  
Particle System modules do not need to be reassigned back to the system; they are interfaces and not independent objects.  
  
Additional resources: [ParticleSystemRenderer.SetActiveVertexStreams](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemRenderer.SetActiveVertexStreams.html).
```
using UnityEngine;
using System.Collections;  
  
[RequireComponent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RequireComponent.html)(typeof(ParticleSystem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html)))]
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        ParticleSystem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html) ps = GetComponent<ParticleSystem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html)>();
        var customData = ps.customData;
        customData.enabled = true;  
  
        Gradient[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gradient.html) grad = new Gradient[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gradient.html)();
        grad.SetKeys(new GradientColorKey[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GradientColorKey.html)[] { new GradientColorKey[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GradientColorKey.html)(Color.blue[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-blue.html), 0.0f), new GradientColorKey[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GradientColorKey.html)(Color.red[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-red.html), 1.0f) }, new GradientAlphaKey[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GradientAlphaKey.html)[] { new GradientAlphaKey[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GradientAlphaKey.html)(1.0f, 0.0f), new GradientAlphaKey[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GradientAlphaKey.html)(0.0f, 1.0f) });  
  
        customData.SetMode(ParticleSystemCustomData.Custom1[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemCustomData.Custom1.html), UnityEngine.ParticleSystemCustomDataMode.Color);
        customData.SetColor(ParticleSystemCustomData.Custom1[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemCustomData.Custom1.html), grad);
    }
}
```

* * *
