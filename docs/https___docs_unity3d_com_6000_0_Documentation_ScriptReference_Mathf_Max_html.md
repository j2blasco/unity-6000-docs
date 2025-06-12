* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.Max.html

#  [Mathf](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.html).Max
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
public static float Max(float a, float b); 
## Declaration
public static float Max(params float[] values); 
### Description
Returns the largest of two or more values. When comparing negative values, values closer to zero are considered larger.
```
using UnityEngine;  
  
public class ScriptExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        // prints 2.4
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(Mathf.Max[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.Max.html)(1.2f, 2.4f));
    }
}

```

* * *
## Declaration
public static int Max(int a, int b); 
## Declaration
public static int Max(params int[] values); 
### Description
Returns the largest value. When comparing negative values, values closer to zero are considered larger.
```
using UnityEngine;  
  
public class ScriptExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        // prints 2
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(Mathf.Max[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.Max.html)(1, 2));  
  
        // prints -1.2
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(Mathf.Max[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.Max.html)(-5.6f, -1.2f));
    }
}

```

* * *
