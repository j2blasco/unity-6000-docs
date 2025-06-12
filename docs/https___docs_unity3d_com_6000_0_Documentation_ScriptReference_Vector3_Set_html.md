* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.Set.html

#  [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html).Set
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
## Declaration
public void Set(float newX, float newY, float newZ); 
### Description
Set x, y and z components of an existing Vector3.
```
// Attach this script to a GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html). Create an empty GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) that will act as your "New Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html)". Assign this in the Inspector.
// Press the "Set" button in the game to set the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)'s position to the "New Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html)" position.  
  
using UnityEngine;
using UnityEngine.EventSystems;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // Use this to set the new position of the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)
    Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) m_MyPosition;  
  
    // Set an external Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) in the Inspector which is the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)’s starting point
    public Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) m_NewTransform;  
  
    void Start()
    {
        // Set the new Vector to be that of the Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) you attach in the Inspector
        m_MyPosition.Set(m_NewTransform.position.x, m_NewTransform.position.y, 0);
    }  
  
    void OnGUI()
    {
        // Press the Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Button.html) to set the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) to this new position
        if (GUI.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Button.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(0, 0, 100, 40), "Set"))
        {
            transform.position = m_MyPosition;
        }
    }
}

```

* * *
