* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderingLayerMask-value.html

#  [RenderingLayerMask](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderingLayerMask.html).value
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
value; 
### Description
Converts a layer mask value to an integer value.
```
using UnityEngine;
using UnityEngine.Rendering;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // Set the rendering layer mask for MeshRenderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshRenderer.html)  
  
    RenderingLayerMask[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderingLayerMask.html) mask = 1 << 10;
    void Start()
    {
        GetComponent<MeshRenderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshRenderer.html)>().renderingLayerMask = mask;
    }
}

```

* * *
