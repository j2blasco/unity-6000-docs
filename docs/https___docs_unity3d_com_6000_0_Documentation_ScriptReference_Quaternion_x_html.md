* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion-x.html

#  [Quaternion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html).x
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Quaternion.html "Go to Quaternion Component in the Manual")
x; 
### Description
X component of the Quaternion. Don't modify this directly unless you know quaternions inside out.
```
//Create three Sliders (**Create**>**UI**>**Slider**) and three Text GameObjects (**Create**>**UI**>**Text**). These are for manipulating the x, y, and z values of the Quaternion[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html). The text will act as a label for each Slider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Slider.html), so position them appropriately.
//Attach this script to a GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html).
//Click on the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) and attach each of the Sliders and Texts to the fields in the Inspector.  
  
//This script shows how the numbers placed into the x, y, and z components of a Quaternion[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html) effect the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) when the w component is left at 1.
//Use the Sliders to see the effects.  
  
using UnityEngine;
using UnityEngine.UI;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    //These are the floats for the x, y, and z components of the quaternion
    float m_MyX, m_MyY, m_MyZ;
    //These are the Sliders that set the rotation. Remember to assign these in the Inspector
    public Slider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Slider.html) m_SliderX, m_SliderY, m_SliderZ;
    //These are the Texts that output the current value of the rotations. Remember to assign these in the Inspector
    public Text m_TextX, m_TextY, m_TextZ;  
  
    // Use this for initialization
    void Start()
    {
        //Initialise the x, y, and z components of the future Quaternion[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html)
        m_MyX = 0;
        m_MyY = 0;
        m_MyZ = 0;  
  
        //Set all the sliders max values to 1 so the Quaternion[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html) values don't go over 1
        m_SliderX.maxValue = 1;
        m_SliderY.maxValue = 1;
        m_SliderZ.maxValue = 1;  
  
        //Set all the sliders min values to -1 so the Quaternion[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html) values don't go under 1
        m_SliderX.minValue = -1;
        m_SliderY.minValue = -1;
        m_SliderZ.minValue = -1;
    }  
  
    //Change the Quaternion[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html) values depending on the values of the Sliders
    private static Quaternion[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html) Change(float x, float y, float z)
    {
        //Return the new Quaternion[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html)
        return new Quaternion[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html)(x, y , z, 1);
    }  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        //Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html) the x, y and z values to that of the sliders
        m_MyX = m_SliderX.value;
        m_MyY = m_SliderY.value;
        m_MyZ = m_SliderZ.value;
        //Output the current values of x, y, and z
        m_TextX.text = " X : " + m_MyX;
        m_TextY.text = " Y : " + m_MyY;
        m_TextZ.text = " Z : " + m_MyZ;  
  
        //Rotate[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Rotate.html) the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) by the new Quaternion[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html)
        transform.rotation = Change(m_MyX, m_MyY, m_MyZ);
    }
}

```

* * *
