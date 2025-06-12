* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.GetBool.html

#  [Animator](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html).GetBool
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
public bool GetBool(string name); 
## Declaration
public bool GetBool(int id); 
### Parameters
Parameter | Description  
---|---  
name | The parameter name.  
id | The parameter ID.  
### Returns
**bool** The value of the parameter. 
### Description
Returns the value of the given boolean parameter.
Return the current state of a bool parameter within the Animator Controller. Use the parameter’s name or ID to search for the appropriate one.
```
//Attach this script to a GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) with an Animator[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html) component attached.
//For this example, create parameters in the Animator[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html) and name them “Crouch” and “Jump”
//Apply these parameters to your transitions between states  
  
//This script allows you to set a Boolean Animator[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html) parameter on and set another Boolean parameter to off if it is currently playing. Press the space key to do this.  
  
using UnityEngine;  
  
public class AnimatorGetBool : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    //Fetch the Animator[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html)
    Animator[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html) m_Animator;
    // Use this to decide if the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) can jump or not
    bool m_Jump;  
  
    void Start()
    {
        //This gets the Animator[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html), which should be attached to the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) you are intending to animate.
        m_Animator = gameObject.GetComponent<Animator[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html)>();
        // The GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) cannot jump
        m_Jump = false;
    }  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        //Press the space bar to enable the "Jump" parameter in the Animator[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html) Controller
        if (Input.GetKey[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetKey.html)(KeyCode.Space[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Space.html)))
        {
            //Set the "Jump" parameter in the Animator[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html) Controller to true
            m_Animator.SetBool("Jump", true);
            //Check to see if the "Crouch" parameter is enabled
            if (m_Animator.GetBool("Crouch"))
            {
                //If the "Crouch" parameter is enabled, disable it as the Animation[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animation.html) should no longer be crouching
                m_Animator.SetBool("Crouch", false);
            }
        }
        //Otherwise the "Jump" parameter should be false
        else m_Animator.SetBool("Jump", false);  
  
        //Press the down arrow key to enable the "Crouch" parameter
        if (Input.GetKey[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetKey.html)(KeyCode.DownArrow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.DownArrow.html)))
            m_Animator.SetBool("Crouch", true);
        else
            m_Animator.SetBool("Crouch", false);
    }
}

```

* * *
