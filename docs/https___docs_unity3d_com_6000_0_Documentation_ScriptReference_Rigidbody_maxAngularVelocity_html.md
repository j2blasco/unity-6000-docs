* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody-maxAngularVelocity.html

#  [Rigidbody](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html).maxAngularVelocity
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
maxAngularVelocity; 
### Description
The maximum angular velocity of the rigidbody measured in radians per second. (Default 7) range { 0, infinity }.
The angular velocity of rigidbodies is clamped to maxAngularVelocity to avoid numerical instability with fast rotating bodies. The maxAngularVelocity is applied to the body before the simulation step. This means that after the simulation frame, the angular velocity might exceed the set maximum. You can override this value per Rigidbody to enable faster rotations on objects such as wheels.
* * *
