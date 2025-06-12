* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.SetTrigger.html

#  [Animator](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html).SetTrigger
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
public void SetTrigger(string name); 
## Declaration
public void SetTrigger(int id); 
### Parameters
Parameter | Description  
---|---  
name | The parameter name.  
id | The parameter ID.  
### Description
Sets the value of the given trigger parameter.
This method allows you to set (i.e. activate) an animation trigger, to cause a change in flow in the state machine of an animator controller. The [Animation Parameters](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimationParameters.html) page describes the purpose of the Animator Controller Parameters window. `Trigger` is one of the 4 selectable options. Selecting this adds a `Trigger` to the list of chosen parameters. Once this is added to the selected list it can be named. Unlike `bool`s which have the same `true/false` option, `Trigger`s have a `true` option which automatically returns back to `false`. A typical example might be to have a Jump option. If this option is entered during run-time the character will jump. At the end of the Jump the previous motion (perhaps a walk or run state) will be returned to.  
  
In the example script below, pressing `UpArrow` or `DownArrow` activates the Jump or Crouch triggers using [SetTrigger](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.SetTrigger.html).
```
//Attach this script to a GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) with an Animator[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html) component attached.
//For this example, create parameters in the Animator[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html) and name them “Crouch” and “Jump”
//Apply these parameters to your transitions between states  
  
//This script allows you to trigger an Animator[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html) parameter and reset the other that could possibly still be active. Press the up and down arrow keys to do this.  
  
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    Animator[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html) m_Animator;  
  
    void Start()
    {
        //Get the Animator[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html) attached to the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) you are intending to animate.
        m_Animator = gameObject.GetComponent<Animator[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html)>();
    }  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        //Press the up arrow button to reset the trigger and set another one
        if (Input.GetKey[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetKey.html)(KeyCode.UpArrow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.UpArrow.html)))
        {
            //Reset the "Crouch" trigger
            m_Animator.ResetTrigger("Crouch");  
  
            //Send the message to the Animator[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html) to activate the trigger parameter named "Jump"
            m_Animator.SetTrigger("Jump");
        }  
  
        if (Input.GetKey[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetKey.html)(KeyCode.DownArrow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.DownArrow.html)))
        {
            //Reset the "Jump" trigger
            m_Animator.ResetTrigger("Jump");  
  
            //Send the message to the Animator[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html) to activate the trigger parameter named "Crouch"
            m_Animator.SetTrigger("Crouch");
        }
    }
}

```

* * *
