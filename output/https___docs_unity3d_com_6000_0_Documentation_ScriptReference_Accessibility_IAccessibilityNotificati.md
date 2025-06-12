* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Accessibility.IAccessibilityNotificationDispatcher.SendLayoutChanged.html

#  [IAccessibilityNotificationDispatcher](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Accessibility.IAccessibilityNotificationDispatcher.html).SendLayoutChanged
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
public void SendLayoutChanged([Accessibility.AccessibilityNode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Accessibility.AccessibilityNode.html) nodeToFocus); 
### Parameters
Parameter | Description  
---|---  
nodeToFocus | Optional node to be focused by the screen reader.  
### Description
Sends a notification to the screen reader when the layout of a screen changes (for example, when an individual element appears or disappears). An optional parameter can be used to request the screen reader focus on a specific node after processing the notification. 
* * *
