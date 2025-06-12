* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/ProgressiveLightmapper-CustomFallOff.html

  * [Lighting](https://docs.unity3d.com/6000.0/Documentation/Manual/LightingOverview.html)
  * [Direct and indirect lighting](https://docs.unity3d.com/6000.0/Documentation/Manual/direct-and-indirect-lighting.html)
  * [Precalculating surface lighting with lightmaps](https://docs.unity3d.com/6000.0/Documentation/Manual/Lightmapping-landing.html)
  * [Configuring lightmapping](https://docs.unity3d.com/6000.0/Documentation/Manual/configure-lightmapping-settings.html)
  * Change the fade distance of lights with fall-off


[](https://docs.unity3d.com/6000.0/Documentation/Manual/global-illumination-configure.html)
Configure lightmapping with a Lighting Settings Asset
[](https://docs.unity3d.com/6000.0/Documentation/Manual/LightmappingDirectional.html)
Store light direction with Directional Mode
# Change the fade distance of lights with fall-off
In the real world, light fades over distance, and dim lights have a lower range than bright lights. The term “fall-off” refers to the rate at which light fades. Alongside Unity’s default fall-off lighting behaviour, you can also use custom fall-off settings.
Progressive **Lightmapper** A tool in Unity that bakes lightmaps according to the arrangement of lights and geometry in your scene. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Lightmapping.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Lightmapper) provides custom fall-off presets, which you can implement via script. See the image below the table for a visual representation of how these work, and the code sample below the image for an example of how to use this functionality.
Refer to [`FalloffType`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GlobalIllumination.FalloffType.html) for more information.
![An example of the visual effect of each custom fall-off preset](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/ProgressiveLightmapper-CustomFallOff.jpg) An example of the visual effect of each custom fall-off preset
## Example
**Note** : The code example below only works with the Progressive Lightmapper when you use Baked or Mixed lights. To use the code example with **realtime lights** Light components whose Mode property is set to Realtime. Unity calculates and updates the lighting of Realtime Lights every frame at runtime. No Realtime Lights are precomputed. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/LightModes-introduction.html#realtime)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#RealtimeLights), use [Enlighten Realtime Global Illumination](https://docs.unity3d.com/6000.0/Documentation/Manual/realtime-gi-using-enlighten.html). 
```
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.Experimental.GlobalIllumination;
using UnityEngine.SceneManagement;
[ExecuteInEditMode]
public class ExtractFalloff : MonoBehaviour
{
    public void OnEnable()
    {
        Lightmapping.RequestLightsDelegate testDel = (Light[] requests, Unity.Collections.NativeArray<LightDataGI> lightsOutput) =>
        {
            DirectionalLight dLight = new DirectionalLight();
            PointLight point = new PointLight();
            SpotLight spot = new SpotLight();
            RectangleLight rect = new RectangleLight();
            DiscLight disc = new DiscLight();
            Cookie cookie = new Cookie();
            LightDataGI ld = new LightDataGI();
            
            for (int i = 0; i < requests.Length; i++)
            {
                Light l = requests[i];
                switch (l.type)
                {
                    case UnityEngine.LightType.Directional: LightmapperUtils.Extract(l, ref dLight); LightmapperUtils.Extract(l, out cookie); ld.Init(ref dLight, ref cookie); break;
                    case UnityEngine.LightType.Point: LightmapperUtils.Extract(l, ref point); LightmapperUtils.Extract(l, out cookie); ld.Init(ref point, ref cookie); break;
                    case UnityEngine.LightType.Spot: LightmapperUtils.Extract(l, ref spot); LightmapperUtils.Extract(l, out cookie); ld.Init(ref spot, ref cookie); break;
                    case UnityEngine.LightType.Rectangle: LightmapperUtils.Extract(l, ref rect); LightmapperUtils.Extract(l, out cookie); ld.Init(ref rect, ref cookie); break;
                    case UnityEngine.LightType.Disc: LightmapperUtils.Extract(l, ref disc); LightmapperUtils.Extract(l, out cookie); ld.Init(ref disc, ref cookie); break;
                    default: ld.InitNoBake(l.GetInstanceID()); break;
                }

                if (l.cookie != null)
                {
                    ld.cookieID = l.cookie.GetInstanceID();
                }
                else
                {
                    ld.cookieID = 0;
                }
                
                ld.falloff = FalloffType.InverseSquared;
                lightsOutput[i] = ld;
            }
        };
        Lightmapping.SetDelegate(testDel);
    }
    void OnDisable()
    {
        Lightmapping.ResetDelegate();
    }
}

```

**Note** : All code in the example above is necessary for the custom falloff to work; however, you can change `InverseSquared` in the line `ld.falloff = FalloffType.InverseSquared;` to use any of [the presets](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GlobalIllumination.FalloffType.html).
* * *
Progressive Lightmapper added in [2018.1](https://docs.unity3d.com/2018.1/Documentation/Manual/30_search.html?q=newin20181) NewIn20181
2018–03–28 Page published 
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/global-illumination-configure.html)
Configure lightmapping with a Lighting Settings Asset
[](https://docs.unity3d.com/6000.0/Documentation/Manual/LightmappingDirectional.html)
Store light direction with Directional Mode
