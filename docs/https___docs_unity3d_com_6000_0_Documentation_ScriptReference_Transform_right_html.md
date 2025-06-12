* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform-right.html

#  [Transform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html).right
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
[Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) right; 
### Description
The red axis of the transform in world space.
Manipulate a GameObject’s position on the X axis (red axis) of the transform in world space. Unlike [Vector3.right](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-right.html), [Transform.right](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform-right.html) moves the GameObject while also considering its rotation.  
  
When a GameObject is rotated, the red arrow representing the X axis of the GameObject also changes direction. [Transform.right](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform-right.html) moves the GameObject in the red arrow’s axis (X).  
  
For moving the GameObject on the X axis while ignoring rotation, see [Vector3.right](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-right.html).
```
//Attach this script to a GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) with a Rigidbody2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html) component. Use the left and right arrow keys to see the transform in action.
//Use the up and down keys to change the rotation, and see how using Transform.right[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform-right.html) differs from using Vector3.right[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-right.html)  
  
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    Rigidbody2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html) m_Rigidbody;
    float m_Speed;  
  
    void Start()
    {
        //Fetch the Rigidbody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html) component you attach from your GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)
        m_Rigidbody = GetComponent<Rigidbody2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html)>();
        //Set the speed of the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)
        m_Speed = 10.0f;
    }  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        if (Input.GetKey[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetKey.html)(KeyCode.RightArrow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.RightArrow.html)))
        {
            //Move the Rigidbody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html) to the right constantly at speed you define (the red arrow axis in Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) view)
            m_Rigidbody.velocity = transform.right * m_Speed;
        }  
  
        if (Input.GetKey[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetKey.html)(KeyCode.LeftArrow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.LeftArrow.html)))
        {
            //Move the Rigidbody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html) to the left constantly at the speed you define (the red arrow axis in Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) view)
            m_Rigidbody.velocity = -transform.right * m_Speed;
        }  
  
        if (Input.GetKey[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetKey.html)(KeyCode.UpArrow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.UpArrow.html)))
        {
            //rotate the sprite about the Z axis in the positive direction
            transform.Rotate(new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(0, 0, 1) * Time.deltaTime[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-deltaTime.html) * m_Speed, Space.World[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Space.World.html));
        }  
  
        if (Input.GetKey[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetKey.html)(KeyCode.DownArrow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.DownArrow.html)))
        {
            //rotate the sprite about the Z axis in the negative direction
            transform.Rotate(new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(0, 0, -1) * Time.deltaTime[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-deltaTime.html) * m_Speed, Space.World[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Space.World.html));
        }
    }
}

```

* * *
