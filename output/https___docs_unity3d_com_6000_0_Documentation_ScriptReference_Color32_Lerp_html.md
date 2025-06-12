* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color32.Lerp.html

#  [Color32](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color32.html).Lerp
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
public static [Color32](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color32.html) Lerp([Color32](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color32.html) a, [Color32](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color32.html) b, float t); 
### Description
Linearly interpolates between colors `a` and `b` by `t`.
`t` is clamped between 0 and 1. When `t` is 0 returns `a`. When `t` is 1 returns `b`.
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    Color32[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color32.html) lerpedColor = Color.white[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-white.html);
    Color32[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color32.html) white32 = Color.white[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-white.html);
    Color32[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color32.html) black32 = Color.black[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-black.html);  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        lerpedColor = Color32.Lerp[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color32.Lerp.html)(white32, black32, Time.time[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-time.html));
    }
}

```

Additional resources: [LerpUnclamped](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color32.LerpUnclamped.html).
* * *
