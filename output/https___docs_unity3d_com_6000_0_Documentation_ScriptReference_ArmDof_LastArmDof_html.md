* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArmDof.LastArmDof.html

#  [ArmDof](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArmDof.html).LastArmDof
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
The last value of the [ArmDof](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArmDof.html) enum.
This value can be used in `for` loops.
```
using UnityEngine;  
  
using UnityEngine.Animations;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        for (int i = 0; i < (int)ArmDof.LastArmDof[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArmDof.LastArmDof.html); ++i)
        {
            var handle = new MuscleHandle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.MuscleHandle.html)(HumanPartDof.LeftArm[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HumanPartDof.LeftArm.html), (ArmDof[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArmDof.html))i);
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(handle.name);
        }
    }
}

```

* * *
