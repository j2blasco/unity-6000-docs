* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider-bounds.html

#  [Collider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html).bounds
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
[Bounds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Bounds.html) bounds; 
### Description
The world space bounding volume of the collider (Read Only).
Note that this will be an empty bounding box if the collider is disabled or the game object is inactive.
```
using UnityEngine;  
  
public class ColliderBounds : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    Collider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html) m_Collider;
    Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) m_Center;
    Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) m_Size, m_Min, m_Max;  
  
    void Start()
    {
        //Fetch the Collider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html) from the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)
        m_Collider = GetComponent<Collider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html)>();
        //Fetch the center of the Collider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html) volume
        m_Center = m_Collider.bounds.center;
        //Fetch the size of the Collider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html) volume
        m_Size = m_Collider.bounds.size;
        //Fetch the minimum and maximum bounds of the Collider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html) volume
        m_Min = m_Collider.bounds.min;
        m_Max = m_Collider.bounds.max;
        //Output this data into the console
        OutputData();
    }  
  
    void OutputData()
    {
        //Output to the console the center and size of the Collider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html) volume
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Collider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html) Center : " + m_Center);
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Collider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html) Size : " + m_Size);
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Collider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html) bound Minimum : " + m_Min);
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Collider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html) bound Maximum : " + m_Max);
    }
}

```

* * *
