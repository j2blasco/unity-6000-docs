* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ReflectionProbe-cullingMask.html

#  [ReflectionProbe](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ReflectionProbe.html).cullingMask
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ReflectionProbe.html "Go to ReflectionProbe Component in the Manual")
cullingMask; 
### Description
This is used to render parts of the reflecion probe's surrounding selectively.
If the [GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)'s `layerMask` AND the probe's `cullingMask` is zero then the game object will be invisible from this probe. See [Layers](https://docs.unity3d.com/6000.0/Documentation/Manual/Layers.html) for more information.
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
public class ExampleScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        var probe = GetComponent<ReflectionProbe[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ReflectionProbe.html)>();
        // Only render objects in the first layer (Default layer) when capturing the probe's texture
        probe.cullingMask = 1 << 0;
    }
}

```

Additional resources: [Camera.cullingMask](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-cullingMask.html).
* * *
