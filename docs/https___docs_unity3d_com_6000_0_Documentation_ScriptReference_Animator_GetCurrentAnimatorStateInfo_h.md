* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.GetCurrentAnimatorStateInfo.html

#  [Animator](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html).GetCurrentAnimatorStateInfo
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
public [AnimatorStateInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimatorStateInfo.html) GetCurrentAnimatorStateInfo(int layerIndex); 
### Parameters
Parameter | Description  
---|---  
layerIndex | The layer index.  
### Returns
**AnimatorStateInfo** An [AnimatorStateInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimatorStateInfo.html) with the information on the current state. 
### Description
Returns an [AnimatorStateInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimatorStateInfo.html) with the information on the current state.
Fetches the data from the current state in the Animator. Use this to get details from the state, including accessing the state’s speed, length, name and other variables. For gathering information from the clips that the states hold, see [Animator.GetCurrentAnimatorClipInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.GetCurrentAnimatorClipInfo.html).
```
//Create a GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) and attach an Animator[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html) component (Click the **Add Component** button in the Inspector window, go to **Miscellaneous**>**Animator**).
//Create an Animator[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html) by going to **Assets** >  **Create** > **Animator Controller**. Attach this Controller to the Animator[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html) attached to your GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)
//In the Animator[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html) Controller, create a Trigger parameter in the **Parameters** tab and name it “Jump”. Then create states and transition arrows that use this parameter.  
  
//This script triggers an Animation[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animation.html) parameter when you press the space key.  
  
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    Animator[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html) m_Animator;
    //Use to output current speed of the state to the screen
    float m_CurrentSpeed;  
  
    void Start()
    {
        //Get the Animator[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html), which you attach to the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) you intend to animate.
        m_Animator = gameObject.GetComponent<Animator[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html)>();
        //The current speed of the first Animator[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html) state
        m_CurrentSpeed = m_Animator.GetCurrentAnimatorStateInfo(0).speed;
    }  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        //Press the space bar to tell the Animator[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html) to trigger the Jump Animation[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animation.html)
        if (Input.GetKeyDown[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetKeyDown.html)(KeyCode.Space[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Space.html)))
        {
            m_Animator.SetTrigger("Jump");
        }  
  
        //When entering the Jump state in the Animator[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html), output the message in the console
        if (m_Animator.GetCurrentAnimatorStateInfo(0).IsName("Jump"))
        {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Jumping");
        }
    }  
  
    void OnGUI()
    {
        //Output the first Animation[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animation.html) speed to the screen
        GUI.Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Label.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(25, 25, 200, 20),  "Speed of State[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Random.State.html) : " + m_CurrentSpeed);
    }
}

```

* * *
