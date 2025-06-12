* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LensFlare-brightness.html

#  [LensFlare](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LensFlare.html).brightness
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LensFlare.html "Go to LensFlare Component in the Manual")
brightness; 
### Description
The strength of the flare.
This controls the size and brightness of the flare elements.  
  
Additional resources: [Lens flare component](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LensFlare.html), [flare assets](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Flare.html).
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // Increments the strenght of the Lensflare lf when the Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) tr
    // gets closer to the Lens flare  
  
    public LensFlare[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LensFlare.html) lf;
    public Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) tr;  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        lf.brightness = 1 / Vector3.Distance[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.Distance.html)(lf.transform.position, tr.position);
    }
}

```

* * *
