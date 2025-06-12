* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.Lerp.html

#  [Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html).Lerp
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
public static [Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) Lerp([Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) a, [Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) b, float t); 
### Parameters
Parameter | Description  
---|---  
a | Color a.  
b | Color b.  
t | Float for combining a and b.  
### Description
Linearly interpolates between colors `a` and `b` by `t`.
`t` is clamped between 0 and 1. When `t` is 0 returns `a`. When `t` is 1 returns `b`.  
  
The code sample sets the color of a GameObject's material to a value between white and black, based on the amount of time that has elapsed. 
```
using UnityEngine;  
  
public class ColorLerp : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) lerpedColor = Color.white[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-white.html);
    Renderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.html) renderer;  
  
    void Start()
    {
        renderer = GetComponent<Renderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.html)>();
    }  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        lerpedColor = Color.Lerp[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.Lerp.html)(Color.white[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-white.html), Color.black[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-black.html), Mathf.PingPong[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.PingPong.html)(Time.time[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-time.html), 1));
        renderer.material.color = lerpedColor;
    }
}

```

Additional resources: [LerpUnclamped](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.LerpUnclamped.html).
* * *
