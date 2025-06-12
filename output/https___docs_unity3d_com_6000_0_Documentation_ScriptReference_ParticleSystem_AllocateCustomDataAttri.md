* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.AllocateCustomDataAttribute.html

#  [ParticleSystem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html).AllocateCustomDataAttribute
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
public void AllocateCustomDataAttribute([ParticleSystemCustomData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemCustomData.html) stream); 
### Parameters
Parameter | Description  
---|---  
stream | The custom data stream to allocate.  
### Description
Ensures that the [customData1](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemJobs.ParticleSystemJobData-customData1.html) and [customData2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemJobs.ParticleSystemJobData-customData1.html) particle attribute arrays are allocated.
This is important if you want to use either of these attributes in a job, such as [IJobParticleSystem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemJobs.IJobParticleSystem.html).
* * *
