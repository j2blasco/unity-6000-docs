* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/iOS.SystemGestureDeferMode.html

# SystemGestureDeferMode
enumeration
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
Bit-mask used to control the deferring of system gestures on iOS.
On iPhone X the home button is implemented as a system gesture (swipe up from the lower edge of the screen). Other gestures are implemented as swipes from other screen edges. Note, this may interfere with games that use swipes as an interaction method. This bit-mask specifies which screen edge gestures the system defers to the second swipe. If deferring is enabled on a specific screen edge, the first swipe is ignored and provides a way to reduce unwanted interactions with the App. Note that iOS Human interface guidelines do not recommend enabling this behavior as it may confuse users.
### Properties
Property | Description  
---|---  
[None](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/iOS.SystemGestureDeferMode.None.html) | Disables gesture deferring on all edges.  
[TopEdge](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/iOS.SystemGestureDeferMode.TopEdge.html) | Identifies top screen edge.  
[LeftEdge](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/iOS.SystemGestureDeferMode.LeftEdge.html) | Identifies left screen edge.  
[BottomEdge](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/iOS.SystemGestureDeferMode.BottomEdge.html) | Identifies bottom screen edge.  
[RightEdge](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/iOS.SystemGestureDeferMode.RightEdge.html) | Identifies right screen edge.  
[All](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/iOS.SystemGestureDeferMode.All.html) | Identifies all screen edges.  
* * *
