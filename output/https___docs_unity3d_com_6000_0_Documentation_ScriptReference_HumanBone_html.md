* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HumanBone.html

# HumanBone
struct in UnityEngine
/
Implemented in:[UnityEngine.AnimationModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.AnimationModule.html)
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
The mapping between a bone in the model and the conceptual bone in the Mecanim human anatomy.
The names of the Mecanim human bone and the bone in the model are stored along with the limiting muscle values that constrain the bone's rotation during animation.
```
using UnityEngine;
using System.Collections.Generic;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        Dictionary<string, string> boneName = new System.Collections.Generic.Dictionary<string, string>();
        boneName["Chest"] = "Bip001 Spine2";
        boneName["Head"] = "Bip001 Head";
        boneName["Hips"] = "Bip001 Pelvis";
        boneName["LeftFoot"] = "Bip001 L Foot";
        boneName["LeftHand"] = "Bip001 L Hand[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.Hand.html)";
        boneName["LeftLowerArm"] = "Bip001 L Forearm";
        boneName["LeftLowerLeg"] = "Bip001 L Calf";
        boneName["LeftShoulder"] = "Bip001 L Clavicle";
        boneName["LeftUpperArm"] = "Bip001 L UpperArm";
        boneName["LeftUpperLeg"] = "Bip001 L Thigh";
        boneName["RightFoot"] = "Bip001 R Foot";
        boneName["RightHand"] = "Bip001 R Hand[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.Hand.html)";
        boneName["RightLowerArm"] = "Bip001 R Forearm";
        boneName["RightLowerLeg"] = "Bip001 R Calf";
        boneName["RightShoulder"] = "Bip001 R Clavicle";
        boneName["RightUpperArm"] = "Bip001 R UpperArm";
        boneName["RightUpperLeg"] = "Bip001 R Thigh";
        boneName["Spine"] = "Bip001 Spine1";
        string[] humanName = HumanTrait.BoneName[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HumanTrait.BoneName.html);
        HumanBone[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HumanBone.html)[] humanBones = new HumanBone[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HumanBone.html)[boneName.Count];
        int j = 0;
        int i = 0;
        while (i < humanName.Length)
        {
            if (boneName.ContainsKey(humanName[i]))
            {
                HumanBone[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HumanBone.html) humanBone = new HumanBone[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HumanBone.html)();
                humanBone.humanName = humanName[i];
                humanBone.boneName = boneName[humanName[i]];
                humanBone.limit.useDefaultValues = true;
                humanBones[j++] = humanBone;
            }
            i++;
        }
    }
}

```

Additional resources: [HumanDescription](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HumanDescription.html), [AvatarBuilder](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AvatarBuilder.html).
### Properties
Property | Description  
---|---  
[boneName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HumanBone-boneName.html) | The name of the bone to which the Mecanim human bone is mapped.  
[humanName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HumanBone-humanName.html) | The name of the Mecanim human bone to which the bone from the model is mapped.  
[limit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HumanBone-limit.html) | The rotation limits that define the muscle for this bone.  
* * *
