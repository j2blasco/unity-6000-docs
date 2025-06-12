* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Accessibility.AccessibilityHierarchy.RefreshNodeFrames.html

#  [AccessibilityHierarchy](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Accessibility.AccessibilityHierarchy.html).RefreshNodeFrames
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
## Declaration
public void RefreshNodeFrames(); 
### Description
Refreshes all the node frames (i.e. the screen elements' positions) for the hierarchy. 
Calling this method sends a notification to the operating system that the layout has changed, by calling [IAccessibilityNotificationDispatcher.SendLayoutChanged](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Accessibility.IAccessibilityNotificationDispatcher.SendLayoutChanged.html) (with a `null` parameter).   
  
Additional resources: [AccessibilityNode.frame](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Accessibility.AccessibilityNode-frame.html), [AccessibilityNode.frameGetter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Accessibility.AccessibilityNode-frameGetter.html)
* * *
