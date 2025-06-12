* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.SetFromToRotation.html

#  [Quaternion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html).SetFromToRotation
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
## Declaration
public void SetFromToRotation([Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) fromDirection, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) toDirection); 
### Description
Creates a rotation which rotates from `fromDirection` to `toDirection`.
Use this to create a rotation which starts at the first Vector (fromDirection) and rotates to the second Vector (toDirection). These Vectors must be set up in a script.
```
//This example shows how the rotation works between two GameObjects. Attach this to a GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html).
//Make sure to assign the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) you would like your GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) to rotate towards in the Inspector  
  
using UnityEngine;  
  
public class SetFromToRotationExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    //This is the Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) of the second GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)
    public Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) m_NextPoint;
    Quaternion[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html) m_MyQuaternion;
    float m_Speed = 1.0f;  
  
    void Start()
    {
        m_MyQuaternion = new Quaternion[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html)();
    }  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        //Set the Quaternion[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html) rotation from the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)'s position to the next GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)'s position
        m_MyQuaternion.SetFromToRotation(transform.position, m_NextPoint.position);
        //Move the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) towards the second GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)
        transform.position = Vector3.Lerp[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.Lerp.html)(transform.position, m_NextPoint.position, m_Speed * Time.deltaTime[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-deltaTime.html));
        //Rotate[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Rotate.html) the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) towards the second GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)
        transform.rotation = m_MyQuaternion * transform.rotation;
    }
}

```

```
//In this example your GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) rotates towards the position of the mouse  
  
using UnityEngine;  
  
public class Example2 : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    Quaternion[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html) m_MyQuaternion;
    float m_Speed = 1.0f;
    Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) m_MousePosition;  
  
    void Start()
    {
        m_MyQuaternion = new Quaternion[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html)();
    }  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        //Fetch the mouse's position
        m_MousePosition = Input.mousePosition[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input-mousePosition.html);
        //Fix how far into the Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) the mouse should be
        m_MousePosition.z = 50.0f;
        //Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) the mouse position into world space
        m_MousePosition = Camera.main.ScreenToWorldPoint(m_MousePosition);  
  
        //Set the Quaternion[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html) rotation from the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)'s position to the mouse position
        m_MyQuaternion.SetFromToRotation(transform.position, m_MousePosition);
        //Move the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) towards the mouse position
        transform.position = Vector3.Lerp[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.Lerp.html)(transform.position, m_MousePosition, m_Speed * Time.deltaTime[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-deltaTime.html));
        //Rotate[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Rotate.html) the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) towards the mouse position
        transform.rotation = m_MyQuaternion * transform.rotation;
    }
}

```

* * *
