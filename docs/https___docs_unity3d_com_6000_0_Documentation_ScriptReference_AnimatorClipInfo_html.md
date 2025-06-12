* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimatorClipInfo.html

# AnimatorClipInfo
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
Information about clip being played and blended by the Animator.
Additional resources: [Animator.GetCurrentAnimatorClipInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.GetCurrentAnimatorClipInfo.html) and [Animator.GetNextAnimatorClipInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.GetNextAnimatorClipInfo.html).
```
//Create a GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) and attach an Animator[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html) component (Click the Add Component[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.html) button in the Inspector of the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) and go to Miscellaneous>Animator[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html)). Set up the Animator[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html) how you would like.
//Attach this script to the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)  
  
//This script outputs the current clip from the Animator[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html) to the console
using UnityEngine;  
  
public class AnimationClipInfoClipExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    Animator[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html) m_Animator;
    AnimatorClipInfo[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimatorClipInfo.html)[] m_AnimatorClipInfo;  
  
    // Use this for initialization
    void Start()
    {
        //Fetch the Animator[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html) component from the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)
        m_Animator = GetComponent<Animator[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html)>();
        //Get the animator clip information from the Animator[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html) Controller
        m_AnimatorClipInfo = m_Animator.GetCurrentAnimatorClipInfo(0);
        //Output the name of the starting clip
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Starting clip : " + m_AnimatorClipInfo[0].clip);
    }
}

```

### Properties
Property | Description  
---|---  
[clip](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimatorClipInfo-clip.html) | Returns the animation clip played by the Animator.  
[weight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimatorClipInfo-weight.html) | Returns the blending weight used by the Animator to blend this clip.  
* * *
