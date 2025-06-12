* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/iOS.Device-deferSystemGesturesMode.html

#  [Device](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/iOS.Device.html).deferSystemGesturesMode
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
[iOS.SystemGestureDeferMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/iOS.SystemGestureDeferMode.html) deferSystemGesturesMode; 
### Description
Defer system gestures until the second swipe on specific edges.
Select one or more edges that users must swipe twice to enact system gestures.  
  
On iOS devices, users can perform actions by swiping from different edges of the screen. For example, you can naviagte home by swiping up from the bottom of the screen. This can cause issues with games that use swiping for interaction.   
  
Use `deferSystemGesturesMode` to control which screen edge gestures the system waits for before responding to the second swipe. The first swipe is ignored to help prevent unintentional actions in the app. The iOS Human Interface Guidelines do not recommend turning on this setting, as it could confuse users.  
  
**Note** : The initial value of this setting is defined by the [PlayerSettings.iOS.deferSystemGesturesMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.iOS-deferSystemGesturesMode.html) property.
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine.iOS;  
  
public class Sample_deferSystemGesturesMode  
{  
  
    void DeferSystemGesturesRuntimeExample()
    {
        // Print current deferSystemGesturesMode value to the console
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(Device.deferSystemGesturesMode.ToString());  
  
        // Set up settings to always prioritize system gestures
        Device.deferSystemGesturesMode[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/iOS.Device-deferSystemGesturesMode.html) = SystemGestureDeferMode.None[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/iOS.SystemGestureDeferMode.None.html);  
  
        // Set up settings to defer all system gestures and prioritize your game input
        Device.deferSystemGesturesMode[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/iOS.Device-deferSystemGesturesMode.html) = SystemGestureDeferMode.All[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/iOS.SystemGestureDeferMode.All.html);  
  
        // Set up settings to defer system gesture from the top edge of the screen (Control Center, Notifications, etc)
        Device.deferSystemGesturesMode[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/iOS.Device-deferSystemGesturesMode.html) = SystemGestureDeferMode.TopEdge[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/iOS.SystemGestureDeferMode.TopEdge.html);  
  
        // Set up settings to defer system gesture from multiple edges of the screen
        Device.deferSystemGesturesMode[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/iOS.Device-deferSystemGesturesMode.html) = SystemGestureDeferMode.TopEdge[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/iOS.SystemGestureDeferMode.TopEdge.html) | SystemGestureDeferMode.BottomEdge[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/iOS.SystemGestureDeferMode.BottomEdge.html);  
  
    }
}

```

* * *
