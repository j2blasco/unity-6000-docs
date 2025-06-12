* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Accessibility.AssistiveSupport.html

# AssistiveSupport
class in UnityEngine.Accessibility
/
Implemented in:[UnityEngine.AccessibilityModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.AccessibilityModule.html)
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
Access point to assistive technology support APIs. 
The currently supported platforms are: 
  * [RuntimePlatform.Android](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RuntimePlatform.Android.html) (requires at least API level 26)
  * [RuntimePlatform.IPhonePlayer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RuntimePlatform.IPhonePlayer.html)


This class contains static methods that allow users to support assistive technologies in the operating system (for example, the screen reader). 
### Static Properties
Property | Description  
---|---  
[activeHierarchy](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Accessibility.AssistiveSupport-activeHierarchy.html) |  The active AccessibilityHierarchy for the screen reader. May be null if no hierarchy is active. You need an active accessibility hierarchy to present any content to the user through the screen reader.If the screen reader is off, there is no active hierarchy. If the screen reader is turned off on the device while an active hierarchy is set, the active hierarchy is automatically set to null.For all the supported platforms, refer to AssistiveSupport.  
[isScreenReaderEnabled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Accessibility.AssistiveSupport-isScreenReaderEnabled.html) |  Whether the screen reader is enabled on the operating system. For all the supported platforms, refer to AssistiveSupport.  
[notificationDispatcher](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Accessibility.AssistiveSupport-notificationDispatcher.html) |  Service used to send accessibility notifications to the screen reader. For all the supported platforms, refer to AssistiveSupport.  
### Events
Event | Description  
---|---  
[nodeFocusChanged](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Accessibility.AssistiveSupport-nodeFocusChanged.html) |  Event that is invoked on the main thread when the screen reader focus changes. For all the supported platforms, refer to AssistiveSupport.  
[screenReaderStatusChanged](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Accessibility.AssistiveSupport-screenReaderStatusChanged.html) |  Event that is invoked on the main thread when the screen reader is enabled or disabled. For all the supported platforms, refer to AssistiveSupport.  
* * *
