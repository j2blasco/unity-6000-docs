* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody-maxLinearVelocity.html

#  [Rigidbody](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html).maxLinearVelocity
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Rigidbody.html "Go to Rigidbody Component in the Manual")
maxLinearVelocity; 
### Description
The maximum linear velocity of the rigidbody measured in meters per second.
The linear velocity of Rigidbody components is clamped to maxLinearVelocity to avoid numerical instability with fast moving bodies. The maxLinearVelocity is applied to the body before the simulation step. This means that after the simulation frame, the linear velocity might exceed the set maximum. You can override this value per Rigidbody.
* * *
