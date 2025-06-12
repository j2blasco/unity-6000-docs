* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.SetBool.html

#  [Animator](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html).SetBool
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
public void SetBool(string name, bool value); 
## Declaration
public void SetBool(int id, bool value); 
### Parameters
Parameter | Description  
---|---  
name | The parameter name.  
id | The parameter ID.  
value | The new parameter value.  
### Description
Sets the value of the given boolean parameter.
Use Animator.SetBool to pass Boolean values to an [Animator Controller](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AnimatorController.html) via script.  
  
Use this to trigger transitions between Animator states. For example, triggering a death animation by setting an “alive” boolean to false. See documentation on [Animation](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimatorControllerCreation.html) for more information on setting up Animators.  
  
Note: You can identify the parameter by name or by ID number, but the name or ID number must be the same as the parameter you want to change in the Animator.
```
//Set up a new Boolean parameter in the Unity Animator[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html) and name it, in this case “Jump”.
//Set up transitions between each state that the animation could follow. For example, the player could be running or idle before they jump, so both would need transitions into the animation.
//If the “Jump” boolean is set to true at any point, the m_Animator plays the animation. However, if it is ever set to false, the animation would return to the appropriate state (“Idle”).
//This script enables and disables this boolean in this case by listening for the mouse click or a tap of the screen.  
  
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    //Fetch the Animator[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html)
    Animator[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html) m_Animator;
    // Use this for deciding if the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) can jump or not
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
        //Click the mouse or tap the screen to change the animation
        if (Input.GetMouseButtonDown[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetMouseButtonDown.html)(0))
            m_Jump = true;  
  
        //Otherwise the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) cannot jump.
        else m_Jump = false;  
  
        //If the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) is not jumping, send that the Boolean “Jump” is false to the Animator[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html). The jump animation does not play.
        if (m_Jump == false)
            m_Animator.SetBool("Jump", false);  
  
        //The GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) is jumping, so send the Boolean as enabled to the Animator[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html). The jump animation plays.
        if (m_Jump == true)
            m_Animator.SetBool("Jump", true);
    }
}

```

* * *
