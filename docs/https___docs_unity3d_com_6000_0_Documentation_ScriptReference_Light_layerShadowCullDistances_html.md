* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light-layerShadowCullDistances.html

#  [Light](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light.html).layerShadowCullDistances
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Light.html "Go to Light Component in the Manual")
layerShadowCullDistances; 
### Description
Per-light, per-layer shadow culling distances. Directional lights only. 
Dynamic shadows can be cast into view from shadow casters that are very far away from the camera. At low incident light angles, this can lead to a lot of objects needing to cast dynamic shadows, which in turn can result in high rendering costs during shadow maps generation.  
  
Using [Light.layerShadowCullDistances](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light-layerShadowCullDistances.html) lets you limit, on a per-layer basis, how far from the camera shadows casters are allowed to be before they get culled from shadow maps generation. The feature complements [Camera.layerCullDistances](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-layerCullDistances.html), but only affects shadow casting, not regular object rendering.  
  
Just like [Camera.layerCullDistances](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-layerCullDistances.html), [Light.layerShadowCullDistances](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light-layerShadowCullDistances.html) requires that you assign a float array of exactly 32 values. A distance of 0 in a layer's index means keep current behaviour for that layer. Assigning null completely disables shadow distance culling, and is effectively the same as passing an array of 32 zeros.  
  
By default, per-layer shadow culling will use a plane aligned with the camera. You can change this to a sphere by setting [Camera.layerCullSpherical](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-layerCullSpherical.html) to true. The effect of this flag is shared by both [Camera.layerCullDistances](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-layerCullDistances.html) and [Light.layerShadowCullDistances](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light-layerShadowCullDistances.html).  
  
Please be aware that when you restrict camera culling distances using [Camera.layerCullDistances](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-layerCullDistances.html), this also restricts shadow casting to those same culling distances. As a result, if you use [Camera.layerCullDistances](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-layerCullDistances.html) and [Light.layerShadowCullDistances](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light-layerShadowCullDistances.html) at the same time *for the same layer index*, the effective shadow culling distance for that layer will be the smallest of those two distances. For layer indices where one of the values are zero, the other value gets used directly, and for layer indices where both values are zero, no special culling behaviour gets applied for that layer.  
  
Only works with [Directional](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightType.Directional.html) lights.  
  
See Also: [Camera.layerCullDistances](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-layerCullDistances.html), [Camera.layerCullSpherical](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-layerCullSpherical.html)
```
using UnityEngine;  
  
[RequireComponent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RequireComponent.html)(typeof(Light[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light.html)))]
public class LayerShadowCullDistancesExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void OnEnable()
    {
        // Setup shadow cull distances
        var shadowCullDistances = new float[32];
        shadowCullDistances[10] = 5f;   // Let's imagine this is our 'Tiny Objects' layer
        shadowCullDistances[11] = 15f;  // Let's imagine this is our 'Small Things' layer
        shadowCullDistances[12] = 100f; // Let's imagine this is our 'Trees' layer  
  
        // Assign shadow cull distances. This will only affect layers 10, 11 and 12.
        GetComponent<Light[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light.html)>().layerShadowCullDistances = shadowCullDistances;
    }  
  
    void OnDisable()
    {
        // Completely disable shadow cull distances
        GetComponent<Light[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light.html)>().layerShadowCullDistances = null;
    }
}

```

* * *
