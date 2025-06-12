* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.Sign.html

#  [Mathf](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.html).Sign
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
## Declaration
public static float Sign(float f); 
### Description
Returns the sign of `f`.
Returns a value of 1 when `f` is 0 or greater. Returns a value of -1 when `f` is negative.
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(Mathf.Sign[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.Sign.html)(-10));
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(Mathf.Sign[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.Sign.html)(10));
    }
}

```

* * *
