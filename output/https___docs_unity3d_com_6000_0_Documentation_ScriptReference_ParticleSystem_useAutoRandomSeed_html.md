* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem-useAutoRandomSeed.html

#  [ParticleSystem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html).useAutoRandomSeed
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ParticleSystem.html "Go to ParticleSystem Component in the Manual")
useAutoRandomSeed; 
### Description
Controls whether the Particle System uses an automatically-generated random number to seed the random number generator.
If set to true, the Particle System will generate a new random seed each time it is played. If set to false, [ParticleSystem.randomSeed](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem-randomSeed.html) will be used instead, allowing for a constant seed (useful if you want your particles to play in exactly the same way each time) or user-defined random value (for example, you may want to cycle through an array of seeds).
* * *
