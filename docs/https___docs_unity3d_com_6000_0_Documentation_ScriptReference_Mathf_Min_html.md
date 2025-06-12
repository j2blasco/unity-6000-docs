* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.Min.html

#  [Mathf](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.html).Min
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
public static float Min(float a, float b); 
## Declaration
public static float Min(params float[] values); 
### Description
Returns the smallest of two or more values.
```
using UnityEngine;  
  
public class ScriptExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        // prints 1.2
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(Mathf.Min[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.Min.html)(1.2f, 2.4f));
    }
}

```

* * *
## Declaration
public static int Min(int a, int b); 
## Declaration
public static int Min(params int[] values); 
### Description
Returns the smallest of two or more values.
```
using UnityEngine;  
  
public class ScriptExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        // prints 1
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(Mathf.Min[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.Min.html)(1, 2));
    }
}

```

* * *
