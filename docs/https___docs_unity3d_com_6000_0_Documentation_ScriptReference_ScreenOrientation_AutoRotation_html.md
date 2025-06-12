* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScreenOrientation.AutoRotation.html

#  [ScreenOrientation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScreenOrientation.html).AutoRotation
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
### Description
Autorotates the screen as necessary toward any of the enabled orientations.
When you assign ScreenOrientation.AutoRotation to the [Screen.orientation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Screen-orientation.html) property, the screen autorotates so that the bottom of the image points downwards. To set permitted orientations, use the following properties: 
  * [Screen.autorotateToLandscapeLeft](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Screen-autorotateToLandscapeLeft.html)
  * [Screen.autorotateToLandscapeRight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Screen-autorotateToLandscapeRight.html)
  * [Screen.autorotateToPortrait](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Screen-autorotateToPortrait.html)
  * [Screen.autorotateToPortraitUpsideDown](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Screen-autorotateToPortraitUpsideDown.html)


You can set a combination of orientations. For example, you can set [Screen.autorotateToPortrait](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Screen-autorotateToPortrait.html) and [Screen.autorotateToPortraitUpsideDown](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Screen-autorotateToPortraitUpsideDown.html) to true whilst setting [Screen.autorotateToLandscapeLeft](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Screen-autorotateToLandscapeLeft.html) and [Screen.autorotateToLandscapeRight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Screen-autorotateToLandscapeRight.html) to false. In this case, the autorotation never chooses either of the landscape options.  
  
**Note** : On Android and iOS platforms, you must set at least one orientation property for autorotation to true. Make sure to set the remaining properties to false.  
  
WebGL builds only support autorotation on the mobile Chrome browser, and only allows orienting to a subset of combinations, these are: 
  * Individual orientations
  * Opposite pairs of orientations
  * All four of the above orientations.


If another combination is set, autorotation defaults to all four orientations.  
**Note:** Autorotation on WebGL only works in full-screen mode. 
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        Screen.autorotateToPortrait[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Screen-autorotateToPortrait.html) = true;  
  
        Screen.autorotateToPortraitUpsideDown[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Screen-autorotateToPortraitUpsideDown.html) = true;  
  
        Screen.autorotateToLandscapeLeft[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Screen-autorotateToLandscapeLeft.html) = false;  
  
        Screen.autorotateToLandscapeRight[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Screen-autorotateToLandscapeRight.html) = false;  
  
        Screen.orientation[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Screen-orientation.html) = ScreenOrientation.AutoRotation[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScreenOrientation.AutoRotation.html);
    }
}

```

Additional resources: [Screen.orientation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Screen-orientation.html).
* * *
