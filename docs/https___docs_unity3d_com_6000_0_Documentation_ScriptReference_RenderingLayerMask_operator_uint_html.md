* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderingLayerMask-operator_uint.html

#  [RenderingLayerMask](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderingLayerMask.html).RenderingLayerMask
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
Implicitly converts `uint` to a RenderingLayerMask.
```
using UnityEngine;
using UnityEngine.Rendering;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        // Converts a uint to a rendering layer and prints all the rendering layer names.
        // As the value is 1025, it will print "Default" and Rendering Layer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.GraphView.Layer.html) 10 Name.
        // 2^0 + 2^10 = 1 + 1024 = 1025  
  
        uint number = 1025;
        RenderingLayerMask[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderingLayerMask.html) mask = number;
        for (int i = 0; i < 32; i++)
        {
            if ((mask.value & (1 << i)) != 0)
            {
                Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)($"Rendering Layer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.GraphView.Layer.html) {i}: {RenderingLayerMask.RenderingLayerToName[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderingLayerMask.RenderingLayerToName.html)(i)}");
            }
        }
    }
}
```

* * *
