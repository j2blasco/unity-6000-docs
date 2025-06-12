* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.Abs.html

#  [Mathf](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.html).Abs
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
public static float Abs(float f); 
### Description
Returns the absolute value of `f`.
```
using UnityEngine;  
  
public class ScriptExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        // prints 10.5
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(Mathf.Abs[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.Abs.html)(-10.5f));
    }
}

```

* * *
## Declaration
public static int Abs(int value); 
### Description
Returns the absolute value of `value`.
```
using UnityEngine;  
  
public class MathAbsExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        // prints 10
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(Mathf.Abs[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.Abs.html)(-10));
    }
}

```

* * *
