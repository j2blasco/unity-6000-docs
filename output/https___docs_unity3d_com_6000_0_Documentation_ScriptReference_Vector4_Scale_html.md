* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector4.Scale.html

#  [Vector4](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector4.html).Scale
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
public static [Vector4](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector4.html) Scale([Vector4](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector4.html) a, [Vector4](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector4.html) b); 
### Description
Multiplies two vectors component-wise.
Every component in the result is a component of `a` multiplied by the same component of `b`.
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        // prints (2.0,6.0,12.0,20.0)
        print(Vector4.Scale[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector4.Scale.html)(new Vector4[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector4.html)(1, 2, 3, 4), new Vector4[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector4.html)(2, 3, 4, 5)));
    }
}

```

* * *
## Declaration
public void Scale([Vector4](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector4.html) scale); 
### Description
Multiplies every component of this vector by the same component of `scale`.
* * *
