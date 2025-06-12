* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Projector-ignoreLayers.html

#  [Projector](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Projector.html).ignoreLayers
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Projector.html "Go to Projector Component in the Manual")
ignoreLayers; 
### Description
Which object layers are ignored by the projector.
See [layer mask](https://docs.unity3d.com/6000.0/Documentation/Manual/Layers.html).  
  
By default this is zero - i.e. no layers are ignored. Each set bit in `ignoreLayers` will make this layer not affected by the projector.
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        Projector[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Projector.html) proj = GetComponent<Projector[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Projector.html)>();
        // Make the projector ignore Default (0) layer
        proj.ignoreLayers = (1 << 0);
    }
}

```

Additional resources: [projector component](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Projector.html), [Layers](https://docs.unity3d.com/6000.0/Documentation/Manual/Layers.html).
* * *
