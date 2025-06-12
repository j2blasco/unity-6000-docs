* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightProbes-bakedProbes.html

#  [LightProbes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightProbes.html).bakedProbes
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
bakedProbes; 
### Description
Coefficients of baked light probes.
Additional resources: [SphericalHarmonicsL2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.SphericalHarmonicsL2.html).
```
using UnityEngine;
using UnityEngine.Rendering;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) m_Ambient;
    public Light[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light.html)[] m_Lights;  
  
    // This script adds the contribution of an ambient light and an array of lights to calculate new spherical harmonics
    // coefficients for all the baked light probes. You can use this for example in the Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html) or at runtime to replace
    // the light probe coefficients that Unity bakes.
    void Start()
    {
        SphericalHarmonicsL2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.SphericalHarmonicsL2.html)[] bakedProbes = LightmapSettings.lightProbes.bakedProbes;
        Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)[] probePositions = LightmapSettings.lightProbes.positions;
        int probeCount = LightmapSettings.lightProbes.count;
        for (int i = 0; i < probeCount; i++)
        {
            // Clear the probe and add ambient light
            bakedProbes[i].Clear();
            bakedProbes[i].AddAmbientLight(m_Ambient);
            
            // Add the contribution of directional and point lights
            foreach (Light[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light.html) light in m_Lights)
            {
                if (light.type == LightType.Directional[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightType.Directional.html))
                {
                    bakedProbes[i].AddDirectionalLight(-light.transform.forward, light.color, light.intensity);
                }
                else if (light.type == LightType.Point[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightType.Point.html))
                {
                    AddPointLight(probePositions[i], light, ref bakedProbes[i]);
                }
            }
        }  
  
        LightmapSettings.lightProbes.bakedProbes = bakedProbes;
    }  
  
    void AddPointLight(Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) probePosition, Light[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light.html) light, ref SphericalHarmonicsL2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.SphericalHarmonicsL2.html) sh)
    {
        // Direction[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.NavigationMoveEvent.Direction.html) from the light probe to the point light
        Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) probeToLight = light.transform.position - probePosition;
        
        // Light[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light.html) attenuation between the point light and the light probe. This formula matches what Unity uses for
        // quadratic light attenuation.
        float attenuation = 1.0f / (1.0f + 25.0f * probeToLight.sqrMagnitude / (light.range * light.range));
        
        // With the normalized direction and the attenuation, the point light is equivalent to a directional
        // light in the context of a light probe.
        sh.AddDirectionalLight(probeToLight.normalized, light.color, light.intensity * attenuation);
    }
}

```

* * *
