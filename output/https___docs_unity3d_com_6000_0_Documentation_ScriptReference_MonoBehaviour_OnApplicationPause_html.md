* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.OnApplicationPause.html

#  [MonoBehaviour](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html).OnApplicationPause(bool)
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-MonoBehaviour.html "Go to MonoBehaviour Component in the Manual")
### Parameters
Parameter | Description  
---|---  
pauseStatus | True if the application is paused, False if playing.  
### Description
Sent to all GameObjects when the playing application pauses or resumes on losing or regaining focus.
When [Run In Background](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings-runInBackground.html) (**Edit > Project Settings > Player > Resolution and Presentation**) is disabled, a game running in the Editor's Play mode or in a standalone Player will pause any time the Editor or Player application loses focus. In these cases Unity sends `OnApplicationPause(true)` to all MonoBehaviours.  
  
The `pauseStatus` parameter is either `true` (paused) or `false` (running). All MonoBehaviours receive this event while they are initializing, just after `Awake`, so it will be called (with status `false`) on first entering Play mode. They receive it again whenever the application pauses or unpauses on losing or regaining focus.  
  
**Note** : Unity does **not** call `OnApplicationPause` in response to toggling the Pause button in the [Editor toolbar](https://docs.unity3d.com/6000.0/Documentation/Manual/Toolbar.html). The status of the pause button in the Editor is tracked by the [PauseState](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PauseState.html) enum.  
  
For `OnApplicationPause` to trigger in a Player application running separately from the Editor, the running Player must be windowed and smaller than the full screen. If the game is hidden (fully or partly) by another application then it pauses and Unity calls `OnApplicationPause` with `true`. When the game regains focus, Unity calls `OnApplicationPause` with `false`.  
  
`OnApplicationPause` can be a co-routine; to do this use the `yield` statement in the function. Implemented this way, it is evaluated twice during the initial frame: first as an early notification, and secondly during the normal co-routine update step.  
  
On **Android** , enabling the on-screen keyboard causes an [OnApplicationFocus](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.OnApplicationFocus.html) event with the value `false`. However, if you press "Home" at the moment the keyboard is enabled, the `OnApplicationFocus` event is not called and `OnApplicationPause` is called instead. 
```
using UnityEngine;  
  
public class AppPaused : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    bool isPaused = false;  
  
    void OnGUI()
    {
        if (isPaused)
            GUI.Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Label.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(100, 100, 50, 30), "Game paused");
    }  
  
    void OnApplicationFocus(bool hasFocus)
    {
        isPaused = !hasFocus;
    }  
  
    void OnApplicationPause(bool pauseStatus)
    {
        isPaused = pauseStatus;
    }
}

```

* * *
