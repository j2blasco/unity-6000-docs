* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics2D-gravity.html

#  [Physics2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics2D.html).gravity
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
[Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) gravity; 
### Description
Acceleration due to gravity.
Set this vector to change all 2D gravity in your Scene. The default is (0, -9.8).
```
//Attach this script to a 2D GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) (for example a Sprite[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite.html)).
//Attach a Rigidbody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html) component to the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) (Click the **Add Component** button and go to **Physics 2D**>**Rigidbody 2D**)  
  
//This script allows you to change the direction of gravity in your Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) by pressing the space key in Play Mode[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Scripting.GarbageCollector.Mode.html).  
  
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    enum GravityDirection { Down, Left, Up, Right };
    GravityDirection m_GravityDirection;  
  
    void Start()
    {
        m_GravityDirection = GravityDirection.Down;
    }  
  
    void FixedUpdate[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.FixedUpdate.html)()
    {
        switch (m_GravityDirection)
        {
            case GravityDirection.Down:
                //Change the gravity to be in a downward direction (default)
                Physics2D.gravity[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics2D-gravity.html) = new Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html)(0, -9.8f);
                //Press the space key to switch to the left direction
                if (Input.GetKeyDown[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetKeyDown.html)(KeyCode.Space[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Space.html)))
                {
                    m_GravityDirection = GravityDirection.Left;
                    Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Left");
                }
                break;  
  
            case GravityDirection.Left:
                //Change the gravity to go to the left
                Physics2D.gravity[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics2D-gravity.html) = new Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html)(-9.8f, 0);
                //Press the space key to change the direction of gravity
                if (Input.GetKeyDown[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetKeyDown.html)(KeyCode.Space[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Space.html)))
                {
                    m_GravityDirection = GravityDirection.Up;
                    Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Up");
                }
                break;  
  
            case GravityDirection.Up:
                //Change the gravity to be in a upward direction
                Physics2D.gravity[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics2D-gravity.html) = new Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html)(0, 9.8f);
                //Press the space key to change the direction
                if (Input.GetKeyDown[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetKeyDown.html)(KeyCode.Space[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Space.html)))
                {
                    m_GravityDirection = GravityDirection.Right;
                    Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Right");
                }
                break;  
  
            case GravityDirection.Right:
                //Change the gravity to go in the right direction
                Physics2D.gravity[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics2D-gravity.html) = new Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html)(9.8f, 0);
                //Press the space key to change the direction
                if (Input.GetKeyDown[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetKeyDown.html)(KeyCode.Space[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Space.html)))
                {
                    m_GravityDirection = GravityDirection.Down;
                    Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Down");
                }  
  
                break;
        }
    }
}

```

* * *
