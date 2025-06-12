* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D-interpolation.html

#  [Rigidbody2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html).interpolation
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
[RigidbodyInterpolation2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RigidbodyInterpolation2D.html) interpolation; 
### Description
Physics interpolation used between updates.
Interpolation is used to estimate the position of the Rigidbody between physics updates. It can be useful to switch this on when the graphics update is much more frequent than the physics update because the object can appear to move along in jerky "hops" rather than having smooth motion. With _interpolate_ mode, motion is smoothed based on the object's positions in previous frames. _Extrapolate_ mode smooths motion based on an estimate of its position in the next frame. The choice of mode depends of the dynamics of the object during gameplay.  
  
Additional resources: [Rigidbody.interpolation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody-interpolation.html).
* * *
