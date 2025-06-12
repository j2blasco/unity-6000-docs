* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform-forward.html

#  [Transform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html).forward
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Transform.html "Go to Transform Component in the Manual")
[Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) forward; 
### Description
Returns a normalized vector representing the blue axis of the transform in world space.
The example below shows how to manipulate a GameObject’s position on the Z axis (blue axis) of the transform in world space. Unlike [Vector3.forward](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-forward.html), [Transform.forward](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform-forward.html) moves the GameObject while also considering its rotation.  
  
When a GameObject is rotated, the blue arrow representing the Z axis of the GameObject also changes direction. [Transform.forward](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform-forward.html) moves the GameObject in the blue arrow’s axis (Z).  
  
For moving the GameObject on the Z axis while ignoring rotation, see [Vector3.forward](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-forward.html).
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    Rigidbody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html) m_Rigidbody;
    float m_Speed;  
  
    void Start()
    {
        //Fetch the Rigidbody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html) component you attach from your GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)
        m_Rigidbody = GetComponent<Rigidbody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html)>();
        //Set the speed of the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)
        m_Speed = 10.0f;
    }  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        if (Input.GetKey[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetKey.html)(KeyCode.UpArrow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.UpArrow.html)))
        {
            //Move the Rigidbody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html) forwards constantly at speed you define (the blue arrow axis in Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) view)
            m_Rigidbody.velocity = transform.forward * m_Speed;
        }  
  
        if (Input.GetKey[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetKey.html)(KeyCode.DownArrow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.DownArrow.html)))
        {
            //Move the Rigidbody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html) backwards constantly at the speed you define (the blue arrow axis in Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) view)
            m_Rigidbody.velocity = -transform.forward * m_Speed;
        }  
  
        if (Input.GetKey[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetKey.html)(KeyCode.RightArrow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.RightArrow.html)))
        {
            //Rotate[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Rotate.html) the sprite about the Y axis in the positive direction
            transform.Rotate(new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(0, 1, 0) * Time.deltaTime[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-deltaTime.html) * m_Speed, Space.World[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Space.World.html));
        }  
  
        if (Input.GetKey[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetKey.html)(KeyCode.LeftArrow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.LeftArrow.html)))
        {
            //Rotate[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Rotate.html) the sprite about the Y axis in the negative direction
            transform.Rotate(new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(0, -1, 0) * Time.deltaTime[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-deltaTime.html) * m_Speed, Space.World[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Space.World.html));
        }
    }
}

```

Another example:
```
using UnityEngine;  
  
// Computes the angle between the target transform and this object  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public float angleBetween = 0.0f;
    public Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) target;  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) targetDir = target.position - transform.position;
        angleBetween = Vector3.Angle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.Angle.html)(transform.forward, targetDir);
    }
}

```

* * *
