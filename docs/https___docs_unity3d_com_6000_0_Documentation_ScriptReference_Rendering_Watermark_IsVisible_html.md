* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.Watermark.IsVisible.html

#  [Watermark](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.Watermark.html).IsVisible
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
## Declaration
public static bool IsVisible(); 
### Returns
**bool** True, if the watermark is visible. 
### Description
Returns `true` if the watermark is visible on-screen. Whether the watermark is visible depends on your build settings and Unity plan.
The following code sample checks if the watermark is visible.
```
using System.Collections;
using UnityEngine;
using UnityEngine.Rendering;  
  
public class WatermarkExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        if(Watermark.IsVisible[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.Watermark.IsVisible.html)())
        {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Watermark[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.Watermark.html) is visible in current setup");
        }
    }
}

```

* * *
