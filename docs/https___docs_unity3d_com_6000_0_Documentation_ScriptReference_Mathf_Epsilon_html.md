* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.Epsilon.html

#  [Mathf](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.html).Epsilon
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
Epsilon; 
### Description
A tiny floating point value (Read Only).
The smallest value that a float can have different from zero.  
  
With the following rules: 
  * anyValue + Epsilon = anyValue
  * anyValue - Epsilon = anyValue
  * 0 + Epsilon = Epsilon
  * 0 - Epsilon = -Epsilon


A value Between any number and Epsilon will result in an arbitrary number due to truncating errors.  
  
Additional resources: [Mathf.Approximately](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.Approximately.html).
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // Compares two floating point numbers and return true if they are the same number.
    // See also Mathf.Approximately[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.Approximately.html), which compares floating point numbers so you dont have
    // to create a function to compare them.  
  
    bool isEqual(float a, float b)
    {
        if (a >= b - Mathf.Epsilon[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.Epsilon.html) && a <= b + Mathf.Epsilon[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.Epsilon.html))
        {
            return true;
        }
        else
        {
            return false;
        }
    }
}

```

* * *
