* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.GetCurrentAnimatorClipInfo.html

#  [Animator](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html).GetCurrentAnimatorClipInfo
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Animator.html "Go to Animator Component in the Manual")
## Declaration
public AnimatorClipInfo[] GetCurrentAnimatorClipInfo(int layerIndex); 
### Parameters
Parameter | Description  
---|---  
layerIndex | The layer index.  
### Returns
**AnimatorClipInfo[]** An array of all the [AnimatorClipInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimatorClipInfo.html) in the current state. 
### Description
Returns an array of all the [AnimatorClipInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimatorClipInfo.html) in the current state of the given layer.
```
//This script outputs the name and length of the Animation[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animation.html) clip played at start-up.  
  
using UnityEngine;  
  
public class GetCurrentAnimatorClipInfoExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    Animator[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html) m_Animator;
    string m_ClipName;
    AnimatorClipInfo[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimatorClipInfo.html)[] m_CurrentClipInfo;  
  
    float m_CurrentClipLength;  
  
    void Start()
    {
        //Get them_Animator, which you attach to the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) you intend to animate.
        m_Animator = gameObject.GetComponent<Animator[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html)>();
        //Fetch the current Animation[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animation.html) clip information for the base layer
        m_CurrentClipInfo = this.m_Animator.GetCurrentAnimatorClipInfo(0);
        //Access the current length of the clip
        m_CurrentClipLength = m_CurrentClipInfo[0].clip.length;
        //Access the Animation[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animation.html) clip name
        m_ClipName = m_CurrentClipInfo[0].clip.name;
    }  
  
    void OnGUI()
    {
        //Output the current Animation[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animation.html) name and length to the screen
        GUI.Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Label.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(0, 0, 200, 20),  "Clip Name : " + m_ClipName);
        GUI.Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Label.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(0, 30, 200, 20),  "Clip Length[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Length.html) : " + m_CurrentClipLength);
    }
}

```

* * *
## Declaration
public void GetCurrentAnimatorClipInfo(int layerIndex, List<AnimatorClipInfo> clips); 
### Parameters
Parameter | Description  
---|---  
layerIndex | The layer index.  
clips | The list of [AnimatorClipInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimatorClipInfo.html) to fill.  
### Description
Fills `clips` with the list of all the [AnimatorClipInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimatorClipInfo.html) in the current state of the given layer.
Additional resources: [GetCurrentAnimatorClipInfoCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.GetCurrentAnimatorClipInfoCount.html).
* * *
