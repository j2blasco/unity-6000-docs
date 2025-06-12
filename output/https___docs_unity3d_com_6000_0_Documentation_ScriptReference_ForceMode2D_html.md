* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ForceMode2D.html

# ForceMode2D
enumeration
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
Option for how to apply a force using [Rigidbody2D.AddForce](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.AddForce.html).
Use this to apply a certain type of force to a 2D RigidBody. There are two types of forces to apply: Force mode and Impulse Mode. For a 3D Rigidbody see [ForceMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ForceMode.html).
```
//This script adds force to a Rigidbody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html). The kind of force is determined by which buttons you click.  
  
//Create a Sprite[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite.html) and attach a Rigidbody2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html) component to it
//Attach this script to the Sprite[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite.html)  
  
using UnityEngine;
using UnityEngine.EventSystems;  
  
public class AddingForce : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    //Use to switch between Force Modes
    enum ModeSwitching { Start, Impulse, Force };
    ModeSwitching m_ModeSwitching;  
  
    //Use this to change the different kinds of force
    ForceMode2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ForceMode2D.html) m_ForceMode;
    //Start position of the RigidBody, use to reset
    Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) m_StartPosition;  
  
    //Use to apply force to RigidBody
    Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) m_NewForce;  
  
    //Use to manipulate the RigidBody of a GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)
    Rigidbody2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html) m_Rigidbody;  
  
    void Start()
    {
        //Fetch the RigidBody component attached to the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)
        m_Rigidbody = GetComponent<Rigidbody2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html)>();
        //Start at first mode (nothing happening yet)
        m_ModeSwitching = ModeSwitching.Start;  
  
        //Initialising the force to use on the RigidBody in various ways
        m_NewForce = new Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html)(-5.0f, 1.0f);  
  
        //This is the RigidBody's starting position
        m_StartPosition = m_Rigidbody.transform.position;
    }  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        //Switching modes depending on button presses
        switch (m_ModeSwitching)
        {
            //This is the starting mode which resets the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)
            case ModeSwitching.Start:  
  
                //Reset to starting position of RigidBody
                m_Rigidbody.transform.position = m_StartPosition;
                //Reset the velocity of the RigidBody
                m_Rigidbody.velocity = new Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html)(0f, 0f);
                break;  
  
            //This is the Force Mode[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Scripting.GarbageCollector.Mode.html)
            case ModeSwitching.Force:
                //Make the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) travel upwards
                m_NewForce = new Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html)(0, 1.0f);
                //Use Force mode as force on the RigidBody
                m_Rigidbody.AddForce(m_NewForce, ForceMode2D.Force[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ForceMode2D.Force.html));
                break;  
  
            //This is the Impulse Mode[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Scripting.GarbageCollector.Mode.html)
            case ModeSwitching.Impulse:
                //Make the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) travel upwards
                m_NewForce = new Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html)(0f, 1.0f);
                //Use Impulse mode as a force on the RigidBody
                m_Rigidbody.AddForce(m_NewForce, ForceMode2D.Impulse[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ForceMode2D.Impulse.html));
                break;
        }
    }  
  
    //These are the Buttons for telling what Force to apply as well as resetting
    void OnGUI()
    {
        //If reset button pressed
        if (GUI.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Button.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(100, 0, 150, 30), "Reset"))
        {
            //Switch[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.Switch.html) to start/reset case  
  
            m_ModeSwitching = ModeSwitching.Start;
        }  
  
        //Impulse button pressed
        if (GUI.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Button.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(100, 60, 150, 30), "Apply Impulse"))
        {
            //Switch[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.Switch.html) to Impulse mode (apply impulse forces to GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html))  
  
            m_ModeSwitching = ModeSwitching.Impulse;
        }  
  
        //Force Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Button.html) Pressed
        if (GUI.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Button.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(100, 90, 150, 30), "Apply Force"))
        {
            //Switch[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.Switch.html) to Force mode (apply force to GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html))
            m_ModeSwitching = ModeSwitching.Force;
        }
    }
}

```

### Properties
Property | Description  
---|---  
[Force](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ForceMode2D.Force.html) | Add a force to the Rigidbody2D, using its mass.  
[Impulse](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ForceMode2D.Impulse.html) | Add an instant force impulse to the rigidbody2D, using its mass.  
* * *
