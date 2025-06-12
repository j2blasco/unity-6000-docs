* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-layerCullDistances.html

#  [Camera](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html).layerCullDistances
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Camera.html "Go to Camera Component in the Manual")
layerCullDistances; 
### Description
Per-layer culling distances.
Normally Camera skips rendering of objects that are further away than [farClipPlane](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-farClipPlane.html). You can set up some [Layers](https://docs.unity3d.com/6000.0/Documentation/Manual/Layers.html) to use smaller culling distances using layerCullDistances. This is very useful to cull small objects early on, if you put them into appropriate layers.  
  
When assigning layerCullDistances, you need to assign float array that has 32 values. Zero values in cull distances means "use far plane distance".  
  
By default, per-layer culling will use a plane aligned with the camera. You can change this to a sphere by setting layerCullSpherical on the Camera to true.
```
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        Camera[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html) camera = GetComponent<Camera[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html)>();
        float[] distances = new float[32];
        distances[10] = 15;
        camera.layerCullDistances = distances;
    }
}

```

Additional resources: [farClipPlane](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-farClipPlane.html), [layerCullSpherical](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-layerCullSpherical.html).
* * *
