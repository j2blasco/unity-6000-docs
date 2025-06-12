* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FingerDof.LastFingerDof.html

#  [FingerDof](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FingerDof.html).LastFingerDof
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
### Description
The last value of the [FingerDof](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FingerDof.html) enum.
This value can be used in `for` loops.
```
using UnityEngine;  
  
using UnityEngine.Animations;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        for (int i = 0; i < (int)FingerDof.LastFingerDof[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FingerDof.LastFingerDof.html); ++i)
        {
            var handle = new MuscleHandle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.MuscleHandle.html)(HumanPartDof.LeftThumb[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HumanPartDof.LeftThumb.html), (FingerDof[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FingerDof.html))i);
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(handle.name);
        }
    }
}

```

* * *
