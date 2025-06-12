* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AvatarBuilder.BuildGenericAvatar.html

#  [AvatarBuilder](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AvatarBuilder.html).BuildGenericAvatar
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
public static [Avatar](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Avatar.html) BuildGenericAvatar([GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) go, string rootMotionTransformName); 
### Parameters
Parameter | Description  
---|---  
go | Root object of your transform hierarchy.  
rootMotionTransformName | Transform name of the root motion transform. If empty no root motion is defined and you must take care of avatar movement yourself.  
### Description
Create a new generic avatar.
All transforms under the root game object will be part of this generic avatar.
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) activeGameObject = Selection.activeGameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection-activeGameObject.html);  
  
        if (activeGameObject != null &&
            activeGameObject.GetComponent<Animator[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html)>() != null)
        {
            Avatar[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Avatar.html) avatar = AvatarBuilder.BuildGenericAvatar[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AvatarBuilder.BuildGenericAvatar.html)(activeGameObject, "");
            avatar.name = "InsertYourName";
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(avatar.isHuman ? "is human" : "is generic");  
  
            Animator[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html) animator = activeGameObject.GetComponent<Animator[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html)>() as Animator[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html);
            animator.avatar = avatar;
        }
    }
}

```

* * *
