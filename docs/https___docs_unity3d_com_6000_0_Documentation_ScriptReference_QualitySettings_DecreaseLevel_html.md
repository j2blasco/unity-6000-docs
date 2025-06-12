* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings.DecreaseLevel.html

#  [QualitySettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings.html).DecreaseLevel
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
## Declaration
public static void DecreaseLevel(bool applyExpensiveChanges = false); 
### Parameters
Parameter | Description  
---|---  
applyExpensiveChanges | Should expensive changes be applied (Anti-aliasing etc).  
### Description
Decrease the current quality level.
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        QualitySettings.DecreaseLevel[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings.DecreaseLevel.html)(false);
    }
}

```

[IncreaseLevel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings.IncreaseLevel.html) and [DecreaseLevel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings.DecreaseLevel.html) functions only apply anti-aliasing if applyExpensiveChanges is true.  
  
Additional resources: [IncreaseLevel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings.IncreaseLevel.html), [Quality Settings](https://docs.unity3d.com/6000.0/Documentation/Manual/class-QualitySettings.html).
* * *
