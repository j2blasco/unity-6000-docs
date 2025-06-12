* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.Distance.html

#  [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html).Distance
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
public static float Distance([Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) a, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) b); 
### Description
Returns the distance between `a` and `b`.
`Vector3.Distance(a,b)` is the same as `(a-b).magnitude`.
```
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) other;  
  
    void Example()
    {
        if (other)
        {
            float dist = Vector3.Distance[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.Distance.html)(other.position, transform.position);
            print("Distance to other: " + dist);
        }
    }
}

```

* * *
