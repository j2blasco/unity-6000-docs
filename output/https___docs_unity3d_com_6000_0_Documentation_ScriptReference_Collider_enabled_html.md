* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider-enabled.html

#  [Collider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html).enabled
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
enabled; 
### Description
Enabled Colliders will collide with other Colliders, disabled Colliders won't.
This is shown as the small checkbox in the inspector of the Colliders. It decides if a GameObject can collide with other Colliders.
```
//This example enables and disables the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)'s Collider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html) when the space bar is pressed.
//Attach this to a GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) and attach a Collider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html) to the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)  
  
using UnityEngine;  
  
public class ColliderEnabled : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    Collider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html) m_Collider;  
  
    void Start()
    {
        //Fetch the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)'s Collider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html) (make sure it has a Collider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html) component)
        m_Collider = GetComponent<Collider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html)>();
    }  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        if (Input.GetKeyDown[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetKeyDown.html)(KeyCode.Space[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Space.html)))
        {
            //Toggle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Toggle.html) the Collider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html) on and off when pressing the space bar
            m_Collider.enabled = !m_Collider.enabled;  
  
            //Output to console whether the Collider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html) is on or not
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Collider.enabled[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider-enabled.html) = " + m_Collider.enabled);
        }
    }
}

```

* * *
