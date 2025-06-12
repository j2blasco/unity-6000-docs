* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BoxCollider-size.html

#  [BoxCollider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BoxCollider.html).size
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-BoxCollider.html "Go to BoxCollider Component in the Manual")
[Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) size; 
### Description
The size of the box, measured in the object's local space.
Use this to return or set the size of the BoxCollider component of a GameObject. Unity measures the size in the GameObject's local space. Changing the BoxCollider size scales it by the Transform’s scale.
```
//Attach this script to a GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html). Make sure the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) has a BoxCollider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BoxCollider.html) component (Unity Cubes have these automatically as long as they weren’t removed).
//Create three Sliders ( **Create**>**UI**>**Slider**). These are for manipulating the x, y, and z values of the size.
//Click on the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) and attach each of the Sliders to the fields in the Inspector.
//In Play Mode[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Scripting.GarbageCollector.Mode.html), click the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) and enable Gizmos[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gizmos.html) to visualize the BoxCollider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BoxCollider.html).  
  
using UnityEngine;
using UnityEngine.UI;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    //Make sure there is a BoxCollider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BoxCollider.html) component attached to your GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)
    BoxCollider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BoxCollider.html) m_Collider;
    float m_ScaleX, m_ScaleY, m_ScaleZ;
    public Slider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Slider.html) m_SliderX, m_SliderY, m_SliderZ;  
  

    void Start()
    {
        //Fetch the Collider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html) from the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)
        m_Collider = GetComponent<BoxCollider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BoxCollider.html)>();
        //These are the starting sizes for the Collider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html) component
        m_ScaleX = 1.0f;
        m_ScaleY = 1.0f;
        m_ScaleZ = 1.0f;  
  
        //Set all the sliders max values to 20 so the size values don't go above 20
        m_SliderX.maxValue = 20;
        m_SliderY.maxValue = 20;
        m_SliderZ.maxValue = 20;  
  
        //Set all the sliders min values to 1 so the size don't go below 1
        m_SliderX.minValue = 1;
        m_SliderY.minValue = 1;
        m_SliderZ.minValue = 1;
    }  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        m_ScaleX = m_SliderX.value;
        m_ScaleY = m_SliderY.value;
        m_ScaleZ = m_SliderZ.value;  
  
        m_Collider.size = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(m_ScaleX, m_ScaleY, m_ScaleZ);
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Current BoxCollider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BoxCollider.html) Size : " + m_Collider.size);
    }
}

```

* * *
