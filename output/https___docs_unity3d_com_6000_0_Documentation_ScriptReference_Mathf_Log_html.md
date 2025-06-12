* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.Log.html

#  [Mathf](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.html).Log
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
public static float Log(float f, float p); 
### Description
Returns the logarithm of a specified number in a specified base.
```
using UnityEngine;  
  
public class ScriptExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        // logarithm of 6 in base 2
        // prints 2.584963
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(Mathf.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.Log.html)(6, 2));
    }
}

```

* * *
## Declaration
public static float Log(float f); 
### Description
Returns the natural (base e) logarithm of a specified number.
```
using UnityEngine;  
  
public class ScriptExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        // natural logarithm of 100
        // prints 4.60517
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(Mathf.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.Log.html)(100));
    }
}

```

* * *
