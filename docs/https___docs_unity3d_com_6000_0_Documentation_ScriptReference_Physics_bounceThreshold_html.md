* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics-bounceThreshold.html

#  [Physics](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.html).bounceThreshold
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
bounceThreshold; 
### Description
Two colliding objects with a relative velocity below this will not bounce (default 2). Must be positive.
This value is usually changed in `Edit->Project Settings->Physics` inspector instead of from scripts.
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        Physics.bounceThreshold[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics-bounceThreshold.html) = 1;
    }
}

```

* * *
