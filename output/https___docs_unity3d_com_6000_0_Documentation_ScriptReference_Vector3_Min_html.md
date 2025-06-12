* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.Min.html

#  [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html).Min
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
public static [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) Min([Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) lhs, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) rhs); 
### Description
Returns a vector that is made from the smallest components of two vectors.
Additional resources: [Max](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.Max.html) function.
```
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) a = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(1, 2, 3);
    public Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) b = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(4, 3, 2);  
  
    void Example()
    {
        print(Vector3.Min[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.Min.html)(a, b));     // prints (1.0f, 2.0f, 2.0f)
    }
}

```

* * *
