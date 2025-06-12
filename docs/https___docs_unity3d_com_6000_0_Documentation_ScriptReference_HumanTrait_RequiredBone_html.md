* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HumanTrait.RequiredBone.html

#  [HumanTrait](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HumanTrait.html).RequiredBone
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
public static bool RequiredBone(int i); 
### Parameters
Parameter | Description  
---|---  
i | Index of the bone to test.  
### Description
Is the bone a member of the minimal set of bones that Mecanim requires for a human model?
The indexing order of the bones is the same as that used for the [BoneName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HumanTrait.BoneName.html) array.
```
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        string[] boneName = HumanTrait.BoneName[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HumanTrait.BoneName.html);
        for (int i = 0; i < HumanTrait.BoneCount[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HumanTrait.BoneCount.html); ++i)
        {
            if (HumanTrait.RequiredBone[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HumanTrait.RequiredBone.html)(i))
                Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(boneName[i]);
        }
    }
}

```

* * *
