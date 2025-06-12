* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.ResetTrigger.html

#  [Animator](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html).ResetTrigger
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
public void ResetTrigger(string name); 
## Declaration
public void ResetTrigger(int id); 
### Parameters
Parameter | Description  
---|---  
name | The parameter name.  
id | The parameter ID.  
### Description
Resets the value of the given trigger parameter.
Use this to reset a Trigger [parameter](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimationParameters.html) in an Animator Controller that could still be active. Make sure to create a parameter in the Animator Controller with the same name. See [Animator.SetTrigger](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.SetTrigger.html) for more information about how to set a Trigger.
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
