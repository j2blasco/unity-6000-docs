* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-operator_multiply.html

#  [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html).operator *
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
[Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) operator *([Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) a, float d); 
### Description
Multiplies a vector by a number.
Multiplies each component of `a` by a number `d`.
```
// make the vector twice longer: prints (2.0,4.0,6.0)
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Example()
    {
        print(new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(1.0f, 2.0f, 3.0f) * 2.0f);
    }
}

```

* * *
[Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) operator *(float d, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) a); 
### Description
Multiplies a vector by a number.
Multiplies each component of `a` by a number `d`.
```
// make the vector twice longer: prints (2.0f, 4.0f, 6.0f)  
  
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Example()
    {
        print(2.0f * new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(1.0f, 2.0f, 3.0f));
    }
}

```

* * *
