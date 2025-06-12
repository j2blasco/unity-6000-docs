* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Accessibility.AccessibilityNode-frame.html

#  [AccessibilityNode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Accessibility.AccessibilityNode.html).frame
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
[Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) frame; 
### Description
The [Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) represents the position in screen coordinates of the node in the UI. This can be set directly but it is recommended that frameGetter is set instead, so that the value can be recalculated when necessary. 
If [AccessibilityHierarchy.RefreshNodeFrames](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Accessibility.AccessibilityHierarchy.RefreshNodeFrames.html) is called, the value of the frame is set to [Rect.zero](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect-zero.html) if frameGetter is not set.
* * *
