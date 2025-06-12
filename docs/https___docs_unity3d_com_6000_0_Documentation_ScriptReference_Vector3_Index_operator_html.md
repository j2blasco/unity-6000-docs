* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.Index_operator.html

#  [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html).this[int]
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
this[int]; 
### Description
Access the x, y, z components using [0], [1], [2] respectively.
```
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) p;  
  
    void Example()
    {
        // set p.y as 5.0f
        p[1] = 5.0f;
    }
}

```

* * *
