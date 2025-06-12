* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Accessibility.AccessibilityNode-frameGetter.html

#  [AccessibilityNode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Accessibility.AccessibilityNode.html).frameGetter
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
frameGetter; 
### Description
Optional delegate that can be set to calculate the frame for the node instead of setting a flat value. If the frame of the node may change over time, this delegate should be set instead of giving a one time value for the frame. 
If [AccessibilityHierarchy.RefreshNodeFrames](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Accessibility.AccessibilityHierarchy.RefreshNodeFrames.html) is called, the value of the frame is set to [Rect.zero](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect-zero.html) if frameGetter is not set.
* * *
