* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.NextPowerOfTwo.html

#  [Mathf](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.html).NextPowerOfTwo
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
public static int NextPowerOfTwo(int value); 
### Description
Returns the next power of two that is equal to, or greater than, the argument.
```
using UnityEngine;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        //Prints 8 to the console
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(Mathf.NextPowerOfTwo[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.NextPowerOfTwo.html)(7));  
  
        //Prints 256 to the console
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(Mathf.NextPowerOfTwo[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.NextPowerOfTwo.html)(139));  
  
        //Prints 256 to the console
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(Mathf.NextPowerOfTwo[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.NextPowerOfTwo.html)(256));
    }
}

```

* * *
