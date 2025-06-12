* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.LightsModule.html

# LightsModule
struct in UnityEngine
/
Implemented in:[UnityEngine.ParticleSystemModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.ParticleSystemModule.html)
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
### Description
Access the ParticleSystem Lights Module.
This module allows you to attach real-time Lights to a percentage of your particles.  
  
The Lights Module is a simple and powerful module that allows particles to cast light onto their environment easily. Lights can inherit properties from the particles they are attached to, such as color and size. Point and Spot Lights are supported, including shadow casting and Light cookies.
```
using UnityEngine;
using System.Collections;  
  
[RequireComponent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RequireComponent.html)(typeof(ParticleSystem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html)))]
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public Light[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light.html) myLight;  
  
    void Start()
    {
        ParticleSystem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html) ps = GetComponent<ParticleSystem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html)>();
        var lights = ps.lights;
        lights.enabled = true;
        lights.ratio = 0.5f;
        lights.light = myLight;
    }
}

```

### Properties
Property | Description  
---|---  
[alphaAffectsIntensity](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.LightsModule-alphaAffectsIntensity.html) | Toggle whether the system multiplies the particle alpha by the light intensity when it computes the final light intensity.  
[enabled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.LightsModule-enabled.html) | Specifies whether the LightsModule is enabled or disabled.  
[intensity](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.LightsModule-intensity.html) | Define a curve to apply custom intensity scaling to particle Lights.  
[intensityMultiplier](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.LightsModule-intensityMultiplier.html) | Intensity multiplier.  
[light](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.LightsModule-light.html) | Select what Light Prefab you want to base your particle lights on.  
[maxLights](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.LightsModule-maxLights.html) | Set a limit on how many Lights this Module can create.  
[range](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.LightsModule-range.html) | Define a curve to apply custom range scaling to particle Lights.  
[rangeMultiplier](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.LightsModule-rangeMultiplier.html) | Range multiplier.  
[ratio](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.LightsModule-ratio.html) | Choose what proportion of particles receive a dynamic light.  
[sizeAffectsRange](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.LightsModule-sizeAffectsRange.html) | Toggle whether the system multiplies the particle size by the light range to determine the final light range.  
[useParticleColor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.LightsModule-useParticleColor.html) | Toggle whether the particle lights multiply their color by the particle color.  
[useRandomDistribution](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.LightsModule-useRandomDistribution.html) | Randomly assign Lights to new particles based on ParticleSystem.LightsModule.ratio.  
* * *
