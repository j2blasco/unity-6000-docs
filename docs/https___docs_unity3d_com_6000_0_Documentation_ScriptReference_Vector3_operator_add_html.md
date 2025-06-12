* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-operator_add.html

#  [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html).operator +
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
[Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) operator +([Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) a, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) b); 
### Description
Adds two vectors.
Adds corresponding components together.
```
// prints (5.0,7.0,9.0)  
  
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        print(new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(1, 2, 3) + new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(4, 5, 6));
    }
}

```

* * *
