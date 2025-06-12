* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.Rad2Deg.html

#  [Mathf](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.html).Rad2Deg
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
Rad2Deg; 
### Description
Radians-to-degrees conversion constant (Read Only).
This is equal to _360 / (PI * 2)_.  
  
Additional resources: [Deg2Rad](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.Deg2Rad.html) constant.
```
using UnityEngine;  
  
public class MathfRad2Deg : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // convert 1 radian to degrees  
  
    float rad = 1.0f;  
  
    void Start()
    {
        float deg = rad * Mathf.Rad2Deg[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.Rad2Deg.html);
        //This will output 1 radians are equal to 57.29578 degrees
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(rad + " radians are equal to " + deg + " degrees.");
    }
}

```

* * *
