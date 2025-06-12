* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gyroscope-gravity.html

#  [Gyroscope](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gyroscope.html).gravity
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
[Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) gravity; 
### Description
Returns the gravity acceleration vector expressed in the device's reference frame.
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    float movementScale;  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        // A "spirit level" - the dot product of the gravity and the Y axis (ie, Vector3.up[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-up.html))
        // is a measure of how far the device is from level on that axis (it will be zero
        // if the device is perfectly level). This value can be used to position an object
        // to act as the "bubble".
        Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) pos = transform.position;
        pos.y = Vector3.Dot[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.Dot.html)(Input.gyro.gravity, Vector3.up[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-up.html)) * movementScale;
        transform.position = pos;
    }
}

```

* * *
