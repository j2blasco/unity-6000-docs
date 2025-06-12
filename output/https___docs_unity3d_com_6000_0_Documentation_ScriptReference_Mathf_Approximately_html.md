* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.Approximately.html

#  [Mathf](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.html).Approximately
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
public static bool Approximately(float a, float b); 
### Description
Compares two floating point values and returns true if they are similar.
Floating point imprecision makes comparing floats using the equals operator inaccurate. For example, `(1.0 == 10.0 / 10.0)` might not return true every time. Approximately() compares two floats and returns true if they are within a small value ([Epsilon](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.Epsilon.html)) of each other.
```
using UnityEngine;  
  
public class ScriptExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        if (Mathf.Approximately[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.Approximately.html)(1.0f, 10.0f / 10.0f))
        {
            print("The values are approximately the same");
        }
    }
}

```

* * *
