* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Screen-brightness.html

#  [Screen](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Screen.html).brightness
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
brightness; 
### Description
Indicates the current brightness of the screen.
The value of this property is a number between 0.0 and 1.0, where 0 represents the minimum and 1.0 represents the maximum brightness of the screen.  
  
**iOS:** The screen brightness changes that your application makes remain in effect until the device is locked, regardless of whether the application is closed. The system brightness is restored the next time the display is turned on.  
  
**Android:** Screen brightness is set by adjusting '[screenBrightness](https://developer.android.com/reference/android/view/WindowManager.LayoutParams#screenBrightness)' in layout parameters of a window. This does not affect the brightness level set in the **Display Brightness** setting of the device.
* * *
