* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Screen-orientation.html

#  [Screen](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Screen.html).orientation
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
[ScreenOrientation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScreenOrientation.html) orientation; 
### Description
Specifies logical orientation of the screen.
The default value is taken from the [Default Orientation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings-defaultInterfaceOrientation.html) property in [Player Settings](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PlayerSettings.html). Currently screen orientation is only relevant on mobile platforms. For example, if a mobile device has a resolution of 480x320, the horizontal orientation is treated as 480x320 resolution and vertical orientation is 320x480.  
  
**Note:** The logical orientation affects not only screen orientation, but also touch coordinates. You should expect drastic changes in the touch positions after changing logical orientation, because touch positions are rotated clockwise or counter-clockwise to match screen coordinates. 
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // Start in landscape mode
    void Start()
    {
        Screen.orientation[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Screen-orientation.html) = ScreenOrientation.LandscapeLeft[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScreenOrientation.LandscapeLeft.html);
    }
}

```

If the value is set to [ScreenOrientation.AutoRotation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScreenOrientation.AutoRotation.html) then the screen selects from any of the options (enabled by [autorotateToPortrait](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Screen-autorotateToPortrait.html), etc) automatically as the device orientation changes.  
  
Additional resources: [ScreenOrientation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScreenOrientation.html).
* * *
