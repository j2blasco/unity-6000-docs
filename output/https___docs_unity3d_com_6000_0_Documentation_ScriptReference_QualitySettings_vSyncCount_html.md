* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings-vSyncCount.html

#  [QualitySettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings.html).vSyncCount
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-QualitySettings.html "Go to QualitySettings Component in the Manual")
vSyncCount; 
### Description
Represents the number of vertical syncs that should pass between each frame.
An integer in the range of 0-4. By default, it is set to 1.  
  
**Desktop and Web**  
  
`vSyncCount` specifies the number of screen refreshes your game allows to pass between frames. In the Unity Editor, this corresponds to the **VSync Count** property under **Project Settings > Quality > Other**.  
  
- If `vSyncCount > 0`, then the field [Application.targetFrameRate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-targetFrameRate.html) is ignored, and the effective frame rate is the native refresh rate of the display divided by `vSyncCount`. If `vSyncCount == 1`, rendering is synchronized to the vertical refresh rate of the display.  
  
- If `vSyncCount` is set to 0, Unity does not synchronize rendering to vertical sync, and the field [Application.targetFrameRate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-targetFrameRate.html) is instead used to pace the rendered frames.  
  
For example, if you're running the Editor on a 60 Hz display and `vSyncCount == 2`, then the target frame rate is 30 frames per second.  
  
**Android and iOS:** The `vSyncCount` field is always ignored because mobile devices do not allow unsynchronized rendering. Use the [Application.targetFrameRate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-targetFrameRate.html) field instead to control the frame rate.  
  
**VR platforms:** Both `vSyncCount` and [Application.targetFrameRate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-targetFrameRate.html) are ignored. Instead, the VR SDK controls the frame rate.   
  
**Note** : You can use [Resolution.refreshRateRatio](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Resolution-refreshRateRatio.html) in the [Screen.currentResolution](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Screen-currentResolution.html) property to query the screen's refresh rate for most platforms.  
  
**Varying display native refresh rate**  
  
While historically the native refresh rate for displays often stayed fixed, the new generation mobile devices, laptops, and desktop devices today can influence the native refresh rate of the display to change dynamically at runtime. For example: 
  * **Desktop** : When user drags a game window from primary monitor over to a secondary monitor, or changes the monitor refresh rate in Display Properties while the game is running, the native display refresh rate can change on the fly.
  * **Laptops** : A gaming laptop with a high refresh rate display might only run at 144 H, for example, when the laptop is powered to a wall charger. When unplugged, the display caps to 60 Hz.
  * **Mobile** : A mobile phone might restrict the display refresh rate to 60 Hz when the mobile phone battery is being charged, to throttle and prevent overheating due to simultaneous heat buildup from the battery being recharged.
  * **Web** : Any of the above conditions might occur, depending on which form factor device the user is browsing on.


Therefore, it is recommended to not hardcode anywhere in the game logic with an assumption that the display refresh rate that is seen at the game startup will persist throughout the lifetime of the application.  
  
Additional resources: [Application.targetFrameRate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-targetFrameRate.html)
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        // Render at half the refresh rate of the display (Desktop and Web platforms)
        QualitySettings.vSyncCount[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings-vSyncCount.html) = 2;
    }
}

```

Additional resources: [Quality Settings](https://docs.unity3d.com/6000.0/Documentation/Manual/class-QualitySettings.html).
* * *
