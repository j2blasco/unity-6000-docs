* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform-localRotation.html

#  [Transform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html).localRotation
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
[Quaternion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html) localRotation; 
### Description
The rotation of the transform relative to the transform rotation of the parent.
Unity stores rotations as Quaternions internally. To rotate an object, use [Transform.Rotate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.Rotate.html). Use [Transform.localEulerAngles](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform-localEulerAngles.html) for modifying the rotation as euler angles.
```
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Example()
    {
        transform.localRotation = Quaternion.identity[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion-identity.html);
    }
}

```

Another example:
```
using System.Collections;
using System.Collections.Generic;
using UnityEngine;  
  
// Rotate[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Rotate.html) a cylinder around the x and z axes. Switch[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.Switch.html) from one to the other
// when the rotation in the current axis reaches 360 degrees.  
  
public class ExampleScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    private float x;
    private float z;
    private bool rotateX;
    private float rotationSpeed;  
  
    void Start()
    {
        x = 0.0f;
        z = 0.0f;
        rotateX = true;
        rotationSpeed = 75.0f;
    }  
  
    void FixedUpdate[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.FixedUpdate.html)()
    {
        if (rotateX == true)
        {
            x += Time.deltaTime[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-deltaTime.html) * rotationSpeed;  
  
            if (x > 360.0f)
            {
                x = 0.0f;
                rotateX = false;
            }
        }
        else
        {
            z += Time.deltaTime[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-deltaTime.html) * rotationSpeed;  
  
            if (z > 360.0f)
            {
                z = 0.0f;
                rotateX = true;
            }
        }  
  
        transform.localRotation = Quaternion.Euler[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.Euler.html)(x, 0, z);
    }
}

```

* * *
