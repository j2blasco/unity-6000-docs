* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Screen-safeArea.html

#  [Screen](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Screen.html).safeArea
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
[Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) safeArea; 
### Description
Returns the safe area of the screen in pixels (Read Only).
On some displays, certain areas of the screen might not be visible to the user. This might be because the display's shape is non-rectangular or in the case of TV displays, it can be caused by overscan. Avoid placing user interface elements in areas outside the safe area rectangle. The maximum size of the safe area is the screen resolution in pixels and is defined as `Rect(0, 0, Screen.width, Screen.height)`.
* * *
