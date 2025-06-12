* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.SetParticles.html

#  [ParticleSystem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html).SetParticles
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
## Declaration
public void SetParticles(out Particle[] particles); 
## Declaration
public void SetParticles(out Particle[] particles, int size); 
## Declaration
public void SetParticles(out Particle[] particles, int size, int offset); 
## Declaration
public void SetParticles(out NativeArray<Particle> particles); 
## Declaration
public void SetParticles(out NativeArray<Particle> particles, int size); 
## Declaration
public void SetParticles(out NativeArray<Particle> particles, int size, int offset); 
### Parameters
Parameter | Description  
---|---  
particles | Input particle buffer, containing the desired particle state.  
size | The number of elements in the particles array that is written to the Particle System.  
offset | The offset into the destination particle list, to assign these particles.  
### Description
Sets the particles of this Particle System.
Setting the lifetime of a particle to a negative value will result in that particle being removed from the Particle System. Additional resources: [GetParticles](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.GetParticles.html).
* * *
