* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderSettings-ambientLight.html

#  [RenderSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderSettings.html).ambientLight
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
[Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) ambientLight; 
### Description
Flat ambient lighting color.
Flat ambient lighting mode uses color. It has the same value as [ambientSkyColor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderSettings-ambientSkyColor.html).
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void  Start()
    {
        // Make the ambient lighting red
        RenderSettings.ambientLight[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderSettings-ambientLight.html) = Color.red[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-red.html);
    }
}

```

Additional resources: [ambientMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderSettings-ambientMode.html), [The Lighting window](https://docs.unity3d.com/6000.0/Documentation/Manual/lighting-window.html).
* * *
