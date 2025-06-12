* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Space.Self.html

#  [Space](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Space.html).Self
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
The local coordinate system of a GameObject relative to its parent, including orientation.
Use `Space.Self` to transform a GameObject relative to its [Transform.localPosition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform-localPosition.html) and its own local axes, taking its orientation into account. For example, `                     Transform.Translate(Vector3.forward, Space.Self)` adds one unit to the object's [Transform.localPosition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform-localPosition.html) on the z-axis of the object, which may differ from the z-axis of the scene depending on the object's orientation.  
  
To transform a GameObject relative to its [Transform.position](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform-position.html) and along the scene axes, use [Space.World](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Space.World.html). 
```
//Attach this script to a GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html).
//This example demonstrates the difference between Space.World[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Space.World.html) and Space.Self[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Space.Self.html) in rotation.
//The m_WorldSpace field will be automatically exposed as a checkbox in the Inspector window labelled World Space[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Space.html). Enable or disable the checkbox in the Inspector to start in world or self respectively.
//Press play to see the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) rotating appropriately. Press space or toggle the World Space[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Space.html) checkbox to switch between World and Self.  
  
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    float m_Speed;
    public bool m_WorldSpace;  
  
    void Start()
    {
        //Set the speed of the rotation
        m_Speed = 20.0f;
        //Rotate[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Rotate.html) the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) a little at the start to show the difference between Space[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Space.html) and Local
        transform.Rotate(60, 0, 60);
    }  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        //Rotate[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Rotate.html) the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) in World Space[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Space.html) if in the m_WorldSpace state
        if (m_WorldSpace)
            transform.Rotate(Vector3.up[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-up.html) * m_Speed * Time.deltaTime[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-deltaTime.html), Space.World[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Space.World.html));
        //Otherwise, rotate the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) in local space
        else
            transform.Rotate(Vector3.up[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-up.html) * m_Speed * Time.deltaTime[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-deltaTime.html), Space.Self[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Space.Self.html));  
  
        //Press the Space[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Space.html) button to switch between world and local space states
        if (Input.GetKeyDown[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetKeyDown.html)(KeyCode.Space[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Space.html)))
        {
            //Make the current state switch to the other state
            m_WorldSpace = !m_WorldSpace;
            //Output the Current state to the console
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("World Space[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Space.html) : " + m_WorldSpace.ToString());
        }
    }
}

```

* * *
