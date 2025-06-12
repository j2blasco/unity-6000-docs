* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemMeshDistribution.html

# ParticleSystemMeshDistribution
enumeration
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
### Description
Sets which method Unity uses to randomly assign Meshes to particles.
The [ParticleSystemRenderer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemRenderer.html) uses this to determine how often to randomly select each Mesh.
### Properties
Property | Description  
---|---  
[UniformRandom](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemMeshDistribution.UniformRandom.html) | Use a uniform random value to give each Mesh an equal chance to appear.  
[NonUniformRandom](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemMeshDistribution.NonUniformRandom.html) | Use per-Mesh weights to make some Meshes appear more often than others. A higher weight value increases the chance of choosing the associated Mesh.  
* * *
