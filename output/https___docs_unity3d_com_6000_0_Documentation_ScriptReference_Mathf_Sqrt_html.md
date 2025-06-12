* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.Sqrt.html

#  [Mathf](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.html).Sqrt
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
public static float Sqrt(float f); 
### Description
Returns square root of `f`.
```
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // The formula made famous by Pythagoras, also used internally by
    // Vector3.Distance[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.Distance.html) and several other standard functions.
    float HypotenuseLength(float sideALength, float sideBLength)
    {
        return Mathf.Sqrt[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.Sqrt.html)(sideALength * sideALength + sideBLength * sideBLength);
    }
}

```

* * *
