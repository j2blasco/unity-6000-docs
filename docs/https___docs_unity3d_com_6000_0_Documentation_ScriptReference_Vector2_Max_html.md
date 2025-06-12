* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.Max.html

#  [Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html).Max
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
public static [Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) Max([Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) lhs, [Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) rhs); 
### Description
Returns a vector that is made from the largest components of two vectors.
Additional resources: [Min](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.Min.html) function.
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) a = new Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html)(1, 3);
        Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) b = new Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html)(4, 2);
        print(Vector2.Max[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.Max.html)(a, b)); // prints (4.0,3.0)
    }
}

```

* * *
