* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2-operator_divide.html

#  [Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html).operator /
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
[Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) operator /([Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) a, float d); 
### Description
Divides a vector by a number.
Divides each component of `a` by a number `d`.
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        // make the vector twice shorter: prints (0.5,1.0)
        print(new Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html)(1, 2) / 2.0f);
    }
}

```

* * *
[Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) operator /([Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) a, [Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) b); 
### Description
Divides a vector by another vector.
Divides each component of `a` by its matching component from `b`.
* * *
