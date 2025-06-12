* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector4-operator_subtract.html

#  [Vector4](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector4.html).operator -
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
[Vector4](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector4.html) operator -([Vector4](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector4.html) a, [Vector4](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector4.html) b); 
### Description
Subtracts one vector from another.
Subtracts each component of `b` from `a`.
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        // prints (-5.0,-3.0,-1.0,1.0)
        print(new Vector4[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector4.html)(1, 2, 3, 4) - new Vector4[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector4.html)(6, 5, 4, 3));
    }
}

```

* * *
[Vector4](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector4.html) operator -([Vector4](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector4.html) a); 
### Description
Negates a vector.
Each component in the result is negated.
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        // prints (-1.0,-2.0,-3.0,-4.0)
        print(-new Vector4[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector4.html)(1, 2, 3, 4));
    }
}

```

* * *
