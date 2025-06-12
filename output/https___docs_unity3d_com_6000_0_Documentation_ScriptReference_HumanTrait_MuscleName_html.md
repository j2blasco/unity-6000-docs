* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HumanTrait.MuscleName.html

#  [HumanTrait](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HumanTrait.html).MuscleName
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
MuscleName; 
### Description
Array of the names of all human muscle types defined by Mecanim.
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
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(muscleName[i]);
        }
    }
}

```

* * *
