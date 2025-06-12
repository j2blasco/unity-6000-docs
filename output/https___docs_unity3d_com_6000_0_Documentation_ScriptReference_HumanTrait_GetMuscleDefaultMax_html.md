* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HumanTrait.GetMuscleDefaultMax.html

#  [HumanTrait](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HumanTrait.html).GetMuscleDefaultMax
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
## Declaration
public static float GetMuscleDefaultMax(int i); 
### Parameters
Parameter | Description  
---|---  
i | Muscle index.  
### Description
Get the default maximum value of rotation for a muscle in degrees.
The default maximum applies to all three axes of rotation for the muscle. The indexing order for the muscles is the same as that of the [MuscleName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HumanTrait.MuscleName.html) array.
```
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        string[] muscleName = HumanTrait.MuscleName[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HumanTrait.MuscleName.html);
        for (int i = 0; i < HumanTrait.BoneCount[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HumanTrait.BoneCount.html); ++i)
        {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(muscleName[i] + " min: " + HumanTrait.GetMuscleDefaultMin[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HumanTrait.GetMuscleDefaultMin.html)(i) + " max: " + HumanTrait.GetMuscleDefaultMax[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HumanTrait.GetMuscleDefaultMax.html)(i));
        }
    }
}

```

Additional resources: [HumanLimit.max](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HumanLimit-max.html), [HumanTrait.GetMuscleDefaultMin](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HumanTrait.GetMuscleDefaultMin.html).
* * *
