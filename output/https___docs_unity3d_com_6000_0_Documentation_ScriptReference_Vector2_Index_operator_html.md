* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.Index_operator.html

#  [Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html).this[int]
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
this[int]; 
### Description
Access the `x` or `y` component using [0] or [1] respectively.
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) p = new Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html)();
        p[1] = 5; // the same as p.y = 5
    }
}

```

* * *
