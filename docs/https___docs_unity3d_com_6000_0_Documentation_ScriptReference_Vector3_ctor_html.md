* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-ctor.html

# Vector3 Constructor
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
public Vector3(float x, float y, float z); 
### Description
Creates a new vector with given x, y, z components.
```
//Attach this script to a GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html).
//Attach a Rigidbody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html) component to the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) (Click **Add Component** button in the Inspector window and go to **Physics**<**Rigidbody**)
//This script moves a GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) upwards using a Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)
using UnityEngine;  
  
public class Vector3CtorExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) myVector;
    Rigidbody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html) m_Rigidbody;
    float m_Speed = 2.0f;  
  
    void Start()
    {
        //Set the vector, which you use to move the RigidBody upwards straight away
        myVector = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(0.0f, 1.0f, 0.0f);
        //Fetch the RigidBody you attach to the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)
        m_Rigidbody = GetComponent<Rigidbody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html)>();
    }  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        //Move the RigidBody upwards at the speed you define
        m_Rigidbody.velocity = myVector * m_Speed;
    }
}

```

* * *
## Declaration
public Vector3(float x, float y); 
### Description
Creates a new vector with given x, y components and sets `z` to zero.
* * *
