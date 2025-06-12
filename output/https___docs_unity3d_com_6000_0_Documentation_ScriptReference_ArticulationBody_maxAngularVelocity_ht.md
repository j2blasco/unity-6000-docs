* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody-maxAngularVelocity.html

#  [ArticulationBody](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody.html).maxAngularVelocity
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ArticulationBody.html "Go to ArticulationBody Component in the Manual")
maxAngularVelocity; 
### Description
The maximum angular velocity of the articulation body measured in radians per second.
The angular velocity of articulation bodies is clamped to maxAngularVelocity to avoid numerical instability with fast rotating bodies. The maxAngularVelocity is applied to the body before the simulation step. This means that after the simulation frame, the angular velocity might exceed the set maximum. You can override this value per articulation body to enable faster rotations on objects such as wheels. (Default 7) range { 0, infinity }.   
Unit of measurement - rad/s (radians per second).
* * *
