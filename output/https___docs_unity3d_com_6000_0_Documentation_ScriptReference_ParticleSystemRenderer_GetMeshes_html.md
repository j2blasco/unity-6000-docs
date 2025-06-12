* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemRenderer.GetMeshes.html

#  [ParticleSystemRenderer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemRenderer.html).GetMeshes
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
## Declaration
public int GetMeshes(out Mesh[] meshes); 
### Parameters
Parameter | Description  
---|---  
meshes | An array this function populates with the list of Meshes the ParticleSystemRenderer uses for particle Mesh selection. If the array is smaller than the number of Meshes, this function cannot populate it with every Mesh. If the array is larger than the number of Meshes, this function ignores indices greater than the number of Meshes. Use [ParticleSystemRenderer.meshCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemRenderer-meshCount.html) to get the number of Meshes the ParticleSystemRenderer has.  
### Returns
**int** The number of Meshes this function wrote to the destination array. 
### Description
Gets the array of Meshes to use when selecting particle meshes.
Additional resources: [ParticleSystemRenderer.renderMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemRenderer-renderMode.html).
* * *
