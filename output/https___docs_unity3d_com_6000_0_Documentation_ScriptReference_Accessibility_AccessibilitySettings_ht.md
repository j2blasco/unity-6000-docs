* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Accessibility.AccessibilitySettings.html

# AccessibilitySettings
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
Provides access to the accessibility settings for the current platform. 
The currently supported platforms are: 
  * [RuntimePlatform.Android](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RuntimePlatform.Android.html)
  * [RuntimePlatform.IPhonePlayer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RuntimePlatform.IPhonePlayer.html)


This class also provides events that are invoked when the user changes accessibility settings. 
### Static Properties
Property | Description  
---|---  
[fontScale](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Accessibility.AccessibilitySettings-fontScale.html) |  Gets the font scale set by the user in the system settings.   
[isBoldTextEnabled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Accessibility.AccessibilitySettings-isBoldTextEnabled.html) |  Checks whether or not bold text is enabled in the system settings.   
[isClosedCaptioningEnabled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Accessibility.AccessibilitySettings-isClosedCaptioningEnabled.html) |  Checks whether or not closed captioning is enabled in the system settings.   
### Events
Event | Description  
---|---  
[boldTextStatusChanged](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Accessibility.AccessibilitySettings-boldTextStatusChanged.html) |  Event that is invoked on the main thread when the user changes the bold text setting in the system settings.   
[closedCaptioningStatusChanged](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Accessibility.AccessibilitySettings-closedCaptioningStatusChanged.html) |  Event that is invoked on the main thread when the user changes the closed captioning setting in the system settings.   
[fontScaleChanged](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Accessibility.AccessibilitySettings-fontScaleChanged.html) |  Event that is invoked on the main thread when the user changes the font scale in the system settings.   
* * *
