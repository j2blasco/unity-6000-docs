* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator-speed.html

#  [Animator](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html).speed
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
speed; 
### Description
The playback speed of the Animator. 1 is normal playback speed.
Use [Animator.speed](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator-speed.html) to manipulate the playback speed of the Animator. Any animations currently being played by the Animator are slowed down or sped up depending on how the speed is altered. Set speed to 1 for normal playback. Negative playback speed is only supported when the recorder is enabled. For more details refer to [Animator.recorderMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator-recorderMode.html).
```
using System.Collections;
using System.Collections.Generic;
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    Animator[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html) m_Animator;
    //Value from the slider, and it converts to speed level
    float m_MySliderValue;  
  
    void Start()
    {
        //Get the animator, attached to the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) you are intending to animate.
        m_Animator = gameObject.GetComponent<Animator[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html)>();
    }  
  
    void OnGUI()
    {
        //Create a Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Label.html) in Game view for the Slider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Slider.html)
        GUI.Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Label.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(0, 25, 40, 60), "Speed");
        //Create a horizontal Slider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Slider.html) to control the speed of the Animator[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html). Drag the slider to 1 for normal speed.  
  
        m_MySliderValue = GUI.HorizontalSlider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.HorizontalSlider.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(45, 25, 200, 60), m_MySliderValue, 0.0F, 1.0F);
        //Make the speed of the Animator[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html) match the Slider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Slider.html) value
        m_Animator.speed = m_MySliderValue;
    }
}

```

* * *
