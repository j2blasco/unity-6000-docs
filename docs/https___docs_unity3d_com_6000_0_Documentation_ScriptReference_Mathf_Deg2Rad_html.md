* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.Deg2Rad.html

#  [Mathf](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.html).Deg2Rad
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Mathf.html "Go to Mathf Component in the Manual")
Deg2Rad; 
### Description
Degrees-to-radians conversion constant (Read Only).
This is equal to _(PI * 2) / 360_.  
  
Additional resources: [Rad2Deg](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.Rad2Deg.html) constant.
```
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public float deg = 30.0F;  
  
    void Start()
    {
        float rad = deg * Mathf.Deg2Rad[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.Deg2Rad.html);
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(deg + " degrees are equal to " + rad + " radians.");
    }
}

```

* * *
