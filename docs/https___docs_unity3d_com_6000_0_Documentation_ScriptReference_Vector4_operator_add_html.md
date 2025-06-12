* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector4-operator_add.html

#  [Vector4](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector4.html).operator +
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
[Vector4](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector4.html) operator +([Vector4](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector4.html) a, [Vector4](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector4.html) b); 
### Description
Adds two vectors.
Adds corresponding components together.
```
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        print(new Vector4[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector4.html)(1, 2, 3, 4) + new Vector4[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector4.html)(5, 6, 7, 8));
    }
}

```

* * *
