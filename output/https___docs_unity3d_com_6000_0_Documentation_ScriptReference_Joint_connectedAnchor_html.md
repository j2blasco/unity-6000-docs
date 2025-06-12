* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Joint-connectedAnchor.html

#  [Joint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Joint.html).connectedAnchor
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
[Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) connectedAnchor; 
### Description
Position of the anchor relative to the connected Rigidbody.
If `Joint.autoConfigureConnectedAnchor` is not enabled, then this will be used to set the position of the anchor on the connected rigidbody. The position is given in local coordinates of the connected rigidbody, or in world coordinates if there is no connected rigidbody.
* * *
