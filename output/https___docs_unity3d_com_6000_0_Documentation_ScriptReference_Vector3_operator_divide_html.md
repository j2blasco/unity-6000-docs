* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-operator_divide.html

#  [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html).operator /
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
[Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) operator /([Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) a, float d); 
### Description
Divides a vector by a number.
Divides each component of `a` by a number `d`.
```
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Example()
    {
        // make the vector twice shorter: prints (0.5,1.0,1.5)
        print(new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(1, 2, 3) / 2.0F);
    }
}

```

* * *
