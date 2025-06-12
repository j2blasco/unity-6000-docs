* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightBakingOutput.html

# LightBakingOutput
struct in UnityEngine
/
Implemented in:[UnityEngine.CoreModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.CoreModule.html)
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
### Description
Struct describing the result of a Global Illumination bake for a given light.
The example below demonstrates how you can check the baked status of a light and change its active state.
```
using UnityEngine;
using System.Collections;  
  
public class LightBakingOutputExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void TurnOffLight(Light[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light.html) light)
    {
        if (light.bakingOutput.isBaked && light.bakingOutput.lightmapBakeType != LightmapBakeType.Realtime[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightmapBakeType.Realtime.html))
        {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Light[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light.html) got some contribution statically baked, it cannot be turned off at runtime.");
        }
        else
        {
            light.enabled = false;
        }
    }
}

```

### Properties
Property | Description  
---|---  
[isBaked](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightBakingOutput-isBaked.html) | Is the light contribution already stored in lightmaps and/or lightprobes?  
[lightmapBakeType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightBakingOutput-lightmapBakeType.html) | This property describes what part of a light's contribution was baked.  
[mixedLightingMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightBakingOutput-mixedLightingMode.html) | In case of a LightmapBakeType.Mixed light, describes what Mixed mode was used to bake the light, irrelevant otherwise.  
[occlusionMaskChannel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightBakingOutput-occlusionMaskChannel.html) | In case of a LightmapBakeType.Mixed light, contains the index of the occlusion mask channel to use if any, otherwise -1.  
[probeOcclusionLightIndex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightBakingOutput-probeOcclusionLightIndex.html) | In case of a LightmapBakeType.Mixed light, contains the index of the light as seen from the occlusion probes point of view if any, otherwise -1.  
* * *
