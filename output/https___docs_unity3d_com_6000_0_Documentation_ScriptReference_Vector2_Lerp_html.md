* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.Lerp.html

#  [Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html).Lerp
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
public static [Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) Lerp([Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) a, [Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) b, float t); 
### Description
Linearly interpolates between vectors `a` and `b` by `t`.
The parameter `t` is clamped to the range [0, 1].  
  
When `t` = 0 returns `a`.   
When `t` = 1 return `b`.   
When `t` = 0.5 returns the midpoint of `a` and `b`.  
  
Additional resources: [LerpUnclamped](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.LerpUnclamped.html).
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) destination;  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        //Moves the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) from it's current position to destination over time
        transform.position = Vector2.Lerp[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.Lerp.html)(transform.position, destination, Time.deltaTime[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-deltaTime.html));
    }
}

```

* * *
