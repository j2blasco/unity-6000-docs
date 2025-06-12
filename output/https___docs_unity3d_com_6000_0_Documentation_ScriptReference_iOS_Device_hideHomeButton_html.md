* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/iOS.Device-hideHomeButton.html

#  [Device](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/iOS.Device.html).hideHomeButton
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
hideHomeButton; 
### Description
Specifies whether the home button should be hidden in the iOS build of this application.
On iPhone X the home button is implemented as a system gesture (swipe up from the bottom edge of the screen). The location of this virtual button is indicated by a white bar. If this setting is enabled, the home button is hidden from view whenever the user has not touched the screen for several seconds. Note that iOS Human interface guidelines do not recommend enabling this behavior for applications not containing passive viewing experiences such as viewing a video or a photo slideshow. The initial value of this setting is defined by `PlayerSettings.iOS.hideHomeButton`.
* * *
