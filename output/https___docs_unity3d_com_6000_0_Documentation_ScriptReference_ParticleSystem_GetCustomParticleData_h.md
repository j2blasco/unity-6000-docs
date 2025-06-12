* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.GetCustomParticleData.html

#  [ParticleSystem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html).GetCustomParticleData
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
public int GetCustomParticleData(List<Vector4> customData, [ParticleSystemCustomData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemCustomData.html) streamIndex); 
### Parameters
Parameter | Description  
---|---  
customData | The array of per-particle data.  
streamIndex | Which stream to retrieve the data from.  
### Returns
**int** The amount of valid per-particle data. 
### Description
Get a stream of custom per-particle data.
Additional resources: [ParticleSystem.SetCustomParticleData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.SetCustomParticleData.html).
* * *
