* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector4.Max.html

#  [Vector4](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector4.html).Max
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
public static [Vector4](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector4.html) Max([Vector4](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector4.html) lhs, [Vector4](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector4.html) rhs); 
### Description
Returns a vector that is made from the largest components of two vectors.
Additional resources: [Min](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector4.Min.html) function.
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        Vector4[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector4.html) a = new Vector4[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector4.html)(1, 2, 3, 5);
        Vector4[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector4.html) b = new Vector4[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector4.html)(4, 3, 2, 0);
        print(Vector4.Max[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector4.Max.html)(a, b)); // prints (4.0,3.0,3.0,5.0)
    }
}

```

* * *
