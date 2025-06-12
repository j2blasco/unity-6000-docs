* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.RoundToInt.html

#  [Mathf](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.html).RoundToInt
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
public static int RoundToInt(float f); 
### Description
Returns `f` rounded to the nearest integer.
If the number ends in .5 so it is halfway between two integers, one of which is even and the other odd, the even number is returned.
```
using UnityEngine;  
  
public class ExampleScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        // Prints 10
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(Mathf.RoundToInt[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.RoundToInt.html)(10.0f));
        // Prints 10
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(Mathf.RoundToInt[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.RoundToInt.html)(10.2f));
        // Prints 11
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(Mathf.RoundToInt[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.RoundToInt.html)(10.7f));
        // Prints 10
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(Mathf.RoundToInt[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.RoundToInt.html)(10.5f));
        // Prints 12
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(Mathf.RoundToInt[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.RoundToInt.html)(11.5f));  
  
        // Prints -10
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(Mathf.RoundToInt[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.RoundToInt.html)(-10.0f));
        // Prints -10
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(Mathf.RoundToInt[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.RoundToInt.html)(-10.2f));
        // Prints -11
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(Mathf.RoundToInt[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.RoundToInt.html)(-10.7f));
        // Prints -10
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(Mathf.RoundToInt[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.RoundToInt.html)(-10.5f));
        // Prints -12
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(Mathf.RoundToInt[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.RoundToInt.html)(-11.5f));
    }
}

```

* * *
