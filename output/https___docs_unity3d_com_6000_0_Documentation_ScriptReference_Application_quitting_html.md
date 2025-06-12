* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-quitting.html

#  [Application](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application.html).quitting
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
Unity raises this event when the Player application is quitting.
Add an event handler to this event to receive a notification that the application is quitting.  
  
**Notes** : The `Application.quitting` event is raised when the quitting process cannot be cancelled. Examples of when this event is not raised are: when the Player is forced to quit or if there is a crash. `Application.quitting` is invoked when exiting Play mode.  
  
**Android** : When an Android application is paused, the `Application.quitting` event doesn't get detected. This is because in the [paused state](https://developer.android.com/guide/components/activities/activity-lifecycle#onpause), the `activity` is no longer visible. As an alternative approach, consider using [OnApplicationFocus(bool)](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.OnApplicationFocus.html) or [OnApplicationPause(bool)](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.OnApplicationPause.html). `OnApplicationFocus(bool)` is called when the application loses or gains focus. `OnApplicationPause(bool)` is called when the application pauses on losing focus or resumes on regaining focus.   
  
**iOS** : iOS applications are usually suspended as they don't quit like applications on other platforms. Use `OnApplicationPause` to capture these events.  
  
**UWP** : On UWP apps, there's no application quit event; therefore, consider using `OnApplicationFocus` event when `focusStatus` equals false.  
  
To prevent the Player application from quitting, refer to the [Application.wantsToQuit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-wantsToQuit.html) event.  
  
Additional resources: [The activity lifecycle](https://developer.android.com/guide/components/activities/activity-lifecycle)
```
using UnityEngine;  
  
public class PlayerQuitExample
{
    static void Quit()
    {
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Quitting the Player");
    }  
  
    [RuntimeInitializeOnLoadMethod]
    static void RunOnStart()
    {
        Application.quitting[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-quitting.html) += Quit;
    }
}

```

Additional resources: [Application.wantsToQuit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-wantsToQuit.html).
* * *
