* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody-maxLinearVelocity.html

#  [ArticulationBody](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody.html).maxLinearVelocity
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
maxLinearVelocity; 
### Description
The maximum linear velocity of the articulation body measured in meters per second.
The linear velocity of articulation bodies is clamped to maxLinearVelocity to avoid numerical instability with fast moving bodies. The maxLinearVelocity is applied to the body before the simulation step. This means that after the simulation frame, the linear velocity might exceed the set maximum. You can override this value per articulation body.   
Unit of measurement - m/s (meters per second).
* * *
