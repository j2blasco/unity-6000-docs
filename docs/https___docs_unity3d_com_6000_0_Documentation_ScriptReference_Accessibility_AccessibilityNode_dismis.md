* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Accessibility.AccessibilityNode-dismissed.html

#  [AccessibilityNode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Accessibility.AccessibilityNode.html).dismissed
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
Called when the user of the screen reader dismisses this node. 
Return an appropriate `bool` value to indicate if the node was successfully dismissed.  
  
On Android, subscribing to this event enables the Dismiss custom action, which is available in the TalkBack local context menu. This is not the same as the Back system gesture, which activates the Back button. 
* * *
