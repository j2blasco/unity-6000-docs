* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRDisplaySubsystem.ReprojectionMode.html

# ReprojectionMode
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
The kind of reprojection the app requests to stabilize its holographic rendering relative to the user's head motion.
### Properties
Property | Description  
---|---  
[Unspecified](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRDisplaySubsystem.ReprojectionMode.Unspecified.html) | Does not specify the type of reprojection mode to use.  
[PositionAndOrientation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRDisplaySubsystem.ReprojectionMode.PositionAndOrientation.html) | Stabilizes the image for changes to both the user's head position and orientation. This is best for world-locked content that you want to remain stationary as the user walks around.  
[OrientationOnly](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRDisplaySubsystem.ReprojectionMode.OrientationOnly.html) | Stabilizes the image only for changes to the user's head orientation, ignores changes in position. This is best for body-locked content that you want to move with the user as they walk around, such as a 360-degree video.  
[None](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRDisplaySubsystem.ReprojectionMode.None.html) | Does not stabilize the image for the user's head motion and instead fixes it in the display. Note that this is only comfortable for users when you use it sparingly, for example when the only visible content is a small cursor.  
* * *
