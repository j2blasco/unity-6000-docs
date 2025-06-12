* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.SetInteger.html

#  [Animator](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html).SetInteger
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
public void SetInteger(string name, int value); 
## Declaration
public void SetInteger(int id, int value); 
### Parameters
Parameter | Description  
---|---  
name | The parameter name.  
id | The parameter ID.  
value | The new parameter value.  
### Description
Sets the value of the given integer parameter.
Use this as a way to trigger transitions between Animator states. One way of using Integers instead of Floats or Booleans is to use it for something that has multiple states, for example directions (turn left, turn right etc.). Each direction could correspond to a number instead of having multiple Booleans that have to be reset each time.  
  
See documentation on [Animation](https://docs.unity3d.com/6000.0/Documentation/Manual/Animator.html) for more information on setting up Animators.  
  
Note: You can identify the parameter by name or by ID number, but the name or ID number must be the same as the parameter you want to change in the Animator.
```
//This script sends messages to an Animator[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html) component to tell it to make transitions based on an integer named “States[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Asset.States.html)”. You change and send this integer to the Animator[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html) by pressing the space and arrow keys.  
  
//In order for this script to work, you have to set up your Animator[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html) Controller so the script can interact with it.
//Create a new Animator[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html) Controller if you do not already have one you want to use. To do this, click on the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) you want to animate and go to its Inspector window. Click the **Add Component** button and go to **Miscellaneous**>**Animator**).
//Double click the Animator[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html) to see the Animator[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html) Controller window.  Open the **Parameters** tab and click the plus icon to add a new parameter. Choose Int from the dropdown. Name the new Integer (for this script, call it “States[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Asset.States.html)”).
//Create a few animation states (right click the grid and choose **Create State**>**Empty**) and choose an Animation[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animation.html) for each in the **Motion** field.
//Next create transitions between each of the states (right click the state, choose **Make Transition** and click on the state you want it to transition to).
//Finally, click on one of the arrows to bring up its Inspector. Click the + icon under the Conditions section and choose the parameter you made (“States[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Asset.States.html)”). Change **Greater** to **Equals** and choose a number that you want to represent this state. Do the same with any other states.
//You may want to set up transitions back to the first animation state so that when the button is let go, it will return to the first state. You may also want to uncheck the **Has Exit Time** box for each transition. Otherwise transitions will wait for an animation to finish before proceeding.  
  
using UnityEngine;  
  
public class AnimatorSetIntExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    Animator[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html) m_Animator;  
  
    void Start()
    {
        //Fetch the Animator[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html) from the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) you attached the script to
        m_Animator = GetComponent<Animator[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html)>();
    }  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        //Check if the horizontal buttons (A,D, left and right arrow keys) are being pressed
        if (Input.GetAxis[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetAxis.html)("Horizontal") > 0 || Input.GetAxis[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetAxis.html)("Horizontal") < 0)
            //Set the integer named "States[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Asset.States.html)" in your Animator[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html) to 1. If the Animator[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html) is set up properly, this should trigger an animation.
            m_Animator.SetInteger("States[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Asset.States.html)", 1);
        //Press the down arrow key to start another animation transition
        else if (Input.GetKey[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetKey.html)(KeyCode.DownArrow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.DownArrow.html)))
            //Set the "States[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Asset.States.html)" integer to 2. This triggers the animation that should start when "States[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Asset.States.html)" is equal to 2
            m_Animator.SetInteger("States[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Asset.States.html)", 2);
        //Press the space key to set the "States[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Asset.States.html) integer to 3
        else if (Input.GetKey[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetKey.html)(KeyCode.Space[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Space.html)))
            m_Animator.SetInteger("States[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Asset.States.html)", 3);
        else
            //If all the other keys are let go, set the "States[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Asset.States.html)" integer to 0.
            m_Animator.SetInteger("States[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Asset.States.html)", 0);
    }
}

```

* * *
