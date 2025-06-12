* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-stereoTargetEye.html

#  [Camera](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html).stereoTargetEye
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
[StereoTargetEyeMask](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/StereoTargetEyeMask.html) stereoTargetEye; 
### Description
Defines which eye of a VR display the Camera renders into.
This property is only used when Virtual Reality is enabled. The default is to render into both eyes.  
  
The values passed to stereoTargetEye are found in the [StereoTargetEyeMask](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/StereoTargetEyeMask.html) enum. Every Camera renders to the Main Game Window by default. If you do not want to see the content from this Camera in the Main Game Window, use a Camera with a higher depth value than this Camera, or set the Camera's showDeviceView value to false.  
  
This API is only available with the Built-in renderer.  
  
Additional resources: [StereoTargetEyeMask](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/StereoTargetEyeMask.html).
```
using UnityEngine;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        Camera.main.stereoTargetEye = StereoTargetEyeMask.Both[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/StereoTargetEyeMask.Both.html);
    }
}

```

* * *
