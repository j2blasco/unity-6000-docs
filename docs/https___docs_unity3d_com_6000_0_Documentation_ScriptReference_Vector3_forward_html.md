* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-forward.html

#  [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html).forward
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
[Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) forward; 
### Description
Shorthand for writing `Vector3(0, 0, 1)`.
```
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Example()
    {
        transform.position += Vector3.forward[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-forward.html) * Time.deltaTime[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-deltaTime.html);
    }
}

```

* * *
