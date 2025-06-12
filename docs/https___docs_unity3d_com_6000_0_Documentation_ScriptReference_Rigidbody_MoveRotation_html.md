* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.MoveRotation.html

#  [Rigidbody](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html).MoveRotation
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Rigidbody.html "Go to Rigidbody Component in the Manual")
## Declaration
public void MoveRotation([Quaternion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html) rot); 
### Parameters
Parameter | Description  
---|---  
rot | The new rotation for the Rigidbody.  
### Description
Rotates the rigidbody to `rotation`.
Use [Rigidbody.MoveRotation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.MoveRotation.html) to rotate a [Rigidbody](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html), complying with the Rigidbody's interpolation setting.  
  
If Rigidbody interpolation is enabled on the [Rigidbody](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html), calling [Rigidbody.MoveRotation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.MoveRotation.html) will resulting in a smooth transition between the two rotations in any intermediate frames rendered. This should be used if you want to continuously rotate a rigidbody in each [FixedUpdate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.FixedUpdate.html).  
  
Set [Rigidbody.rotation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody-rotation.html) instead, if you want to teleport a rigidbody from one rotation to another, with no intermediate positions being rendered.
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    Rigidbody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html) m_Rigidbody;
    Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) m_EulerAngleVelocity;  
  
    void Start()
    {
        //Fetch the Rigidbody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html) from the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) with this script attached
        m_Rigidbody = GetComponent<Rigidbody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html)>();  
  
        //Set the angular velocity of the Rigidbody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html) (rotating around the Y axis, 100 deg/sec)
        m_EulerAngleVelocity = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(0, 100, 0);
    }  
  
    void FixedUpdate[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.FixedUpdate.html)()
    {
        Quaternion[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html) deltaRotation = Quaternion.Euler[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.Euler.html)(m_EulerAngleVelocity * Time.fixedDeltaTime[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-fixedDeltaTime.html));
        m_Rigidbody.MoveRotation(m_Rigidbody.rotation * deltaRotation);
    }
}

```

* * *
