* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ForceMode.Impulse.html

#  [ForceMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ForceMode.html).Impulse
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
Add an instant force impulse to the rigidbody, using its mass.
Apply the impulse force instantly with a single function call. This mode depends on the mass of rigidbody so more force must be applied to push or twist higher-mass objects the same amount as lower-mass objects. This mode is useful for applying forces that happen instantly, such as forces from explosions or collisions. In this mode, the unit of the force parameter is applied to the rigidbody as mass*distance/time.
```
using UnityEngine;  
  
public class ForceModeExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    //Use to switch between Force Modes
    enum ModeSwitching { Start, Impulse, Acceleration, Force, VelocityChange };
    ModeSwitching m_ModeSwitching;  
  
    Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) m_StartPos, m_StartForce;
    Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) m_NewForce;
    Rigidbody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html) m_Rigidbody;  
  
    string m_ForceXString = string.Empty;
    string m_ForceYString = string.Empty;  
  
    float m_ForceX, m_ForceY;
    float m_Result;  
  

    void Start()
    {
        //You get the Rigidbody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html) component you attach to the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)
        m_Rigidbody = GetComponent<Rigidbody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html)>();  
  
        //This starts at first mode (nothing happening yet)
        m_ModeSwitching = ModeSwitching.Start;  
  
        //Initialising the force which is used on GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) in various ways
        m_NewForce = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(-5.0f, 1.0f, 0.0f);  
  
        //Initialising floats
        m_ForceX = 0;
        m_ForceY = 0;  
  
        //The forces typed in from the text fields (the ones you can manipulate in Game view)
        m_ForceXString = "0";
        m_ForceYString = "0";  
  
        //The GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)'s starting position and Rigidbody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html) position
        m_StartPos = transform.position;
        m_StartForce = m_Rigidbody.transform.position;
    }  
  
    void FixedUpdate[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.FixedUpdate.html)()
    {
        //If the current mode is not the starting mode (or the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) is not reset), the force can change
        if (m_ModeSwitching != ModeSwitching.Start)
        {
            //The force changes depending what you input into the text fields
            m_NewForce = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(m_ForceX, m_ForceY, 0);
        }  
  
        //Here, switching modes depend on button presses in the Game mode
        switch (m_ModeSwitching)
        {
            //This is the starting mode which resets the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)
            case ModeSwitching.Start:
                //This resets the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) and Rigidbody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html) to their starting positions
                transform.position = m_StartPos;
                m_Rigidbody.transform.position = m_StartForce;  
  
                //This resets the velocity of the Rigidbody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html)
                m_Rigidbody.velocity = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(0f, 0f, 0f);
                break;  
  
            //These are the modes ForceMode[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ForceMode.html) can force on a Rigidbody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html)
            //This is Acceleration mode
            case ModeSwitching.Acceleration:
                //The function converts the text fields into floats and updates the Rigidbody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html)’s force
                MakeCustomForce();  
  
                //Use Acceleration as the force on the Rigidbody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html)
                m_Rigidbody.AddForce(m_NewForce, ForceMode.Acceleration[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ForceMode.Acceleration.html));
                break;  
  
            //This is Force Mode[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Scripting.GarbageCollector.Mode.html), using a continuous force on the Rigidbody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html) considering its mass
            case ModeSwitching.Force:
                //Converts the text fields into floats and updates the force applied to the Rigidbody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html)
                MakeCustomForce();  
  
                //Use Force as the force on GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)’s Rigidbody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html)
                m_Rigidbody.AddForce(m_NewForce, ForceMode.Force[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ForceMode.Force.html));
                break;  
  
            //This is Impulse Mode[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Scripting.GarbageCollector.Mode.html), which involves using the Rigidbody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html)’s mass to apply an instant impulse force.
            case ModeSwitching.Impulse:
                //The function converts the text fields into floats and updates the force applied to the Rigidbody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html)
                MakeCustomForce();  
  
                //Use Impulse as the force on GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)
                m_Rigidbody.AddForce(m_NewForce, ForceMode.Impulse[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ForceMode.Impulse.html));
                break;  
  

            //This is VelocityChange which involves ignoring the mass of the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) and impacting it with a sudden speed change in a direction
            case ModeSwitching.VelocityChange:
                //Converts the text fields into floats and updates the force applied to the Rigidbody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html)
                MakeCustomForce();  
  
                //Make a Velocity change on the Rigidbody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html)
                m_Rigidbody.AddForce(m_NewForce, ForceMode.VelocityChange[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ForceMode.VelocityChange.html));
                break;
        }
    }  
  
    //The function outputs buttons, text fields, and other interactable UI elements to the Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) in Game view
    void OnGUI()
    {
        //Getting the inputs from each text field and storing them as strings
        m_ForceXString = GUI.TextField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.TextField.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(300, 10, 200, 20), m_ForceXString, 25);
        m_ForceYString = GUI.TextField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.TextField.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(300, 30, 200, 20), m_ForceYString, 25);  
  
        //Press the button to reset the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) and Rigidbody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html)
        if (GUI.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Button.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(100, 0, 150, 30), "Reset"))
        {
            //This switches to the start/reset case
            m_ModeSwitching = ModeSwitching.Start;
        }  
  
        //When you press the Acceleration button, switch to Acceleration mode
        if (GUI.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Button.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(100, 30, 150, 30), "Apply Acceleration"))
        {
            //Switch[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.Switch.html) to Acceleration (apply acceleration force to GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html))
            m_ModeSwitching = ModeSwitching.Acceleration;
        }  
  
        //If you press the Impulse button
        if (GUI.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Button.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(100, 60, 150, 30), "Apply Impulse"))
        {
            //Switch[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.Switch.html) to impulse (apply impulse forces to GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html))
            m_ModeSwitching = ModeSwitching.Impulse;
        }  
  
        //If you press the Force Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Button.html), switch to Force state
        if (GUI.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Button.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(100, 90, 150, 30), "Apply Force"))
        {
            //Switch[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.Switch.html) to Force (apply force to GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html))
            m_ModeSwitching = ModeSwitching.Force;
        }  
  
        //Press the button to switch to VelocityChange state
        if (GUI.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Button.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(100, 120, 150, 30), "Apply Velocity Change"))
        {
            //Switch[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.Switch.html) to velocity changing
            m_ModeSwitching = ModeSwitching.VelocityChange;
        }
    }  
  
    //Changing strings to floats for the forces
    float ConvertToFloat(string Name)
    {
        float.TryParse(Name, out m_Result);
        return m_Result;
    }  
  
    //Set the converted float from the text fields as the forces to apply to the Rigidbody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html)
    void MakeCustomForce()
    {
        //This converts the strings to floats
        m_ForceX = ConvertToFloat(m_ForceXString);
        m_ForceY = ConvertToFloat(m_ForceYString);
    }
}

```

* * *
