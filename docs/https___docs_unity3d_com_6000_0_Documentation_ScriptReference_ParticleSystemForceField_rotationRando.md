* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemForceField-rotationRandomness.html

#  [ParticleSystemForceField](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemForceField.html).rotationRandomness
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ParticleSystemForceField.html "Go to ParticleSystemForceField Component in the Manual")
[Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) rotationRandomness; 
### Description
Apply randomness to the Force Field axis that particles will travel around.
When applying rotational forces to particles, the particles will spin around the Z axis of the Force Field's Transform component by default.  
  
Using rotationRandomness allows each particle to deviate from this default axis by the specified amount. A value of 1 allows each particle to choose a completely random axis to spin around, whereas smaller values will constrain the movement more closely to the default axis.  
  
Additional resources: [ParticleSystemForceField](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemForceField.html).
* * *
