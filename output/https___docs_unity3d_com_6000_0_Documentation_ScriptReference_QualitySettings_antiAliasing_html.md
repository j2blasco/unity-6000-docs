* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings-antiAliasing.html

#  [QualitySettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings.html).antiAliasing
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-QualitySettings.html "Go to QualitySettings Component in the Manual")
antiAliasing; 
### Description
Choose the level of Multi-Sample Anti-aliasing (MSAA) that the GPU performs.
The value indicates the number of samples per pixel. Valid values are 0 (no MSAA), 2, 4, and 8. If the graphics API does not support the value you provide, it uses the next highest supported value.  
  
MSAA is compatible only with Forward rendering. For more information on other types of anti-aliasing and compatibility, see [Post processing](https://docs.unity3d.com/6000.0/Documentation/Manual/PostProcessingOverview.html). 
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        // Set AntiAliasing to use 2x Multisampling
        QualitySettings.antiAliasing[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings-antiAliasing.html) = 2;
    }
}

```

Additional resources: [Quality Settings](https://docs.unity3d.com/6000.0/Documentation/Manual/class-QualitySettings.html).
* * *
