* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-usePhysicalProperties.html

#  [Camera](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html).usePhysicalProperties
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Camera.html "Go to Camera Component in the Manual")
usePhysicalProperties; 
### Description
Enable `usePhysicalProperties` to use physical camera properties to compute the field of view and the frustum.
The physical properties include the sensor size, lens shift, and focal length.
```
using UnityEngine;  
  
public class ExampleScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        Camera[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html) cam = gameObject.GetComponent<Camera[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html)>();
        cam.usePhysicalProperties = true;
        cam.focalLength = 60f;
    }  
  
}

```

* * *
