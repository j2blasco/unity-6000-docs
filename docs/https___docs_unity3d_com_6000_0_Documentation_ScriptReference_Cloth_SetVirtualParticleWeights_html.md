* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cloth.SetVirtualParticleWeights.html

#  [Cloth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cloth.html).SetVirtualParticleWeights
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Cloth.html "Go to Cloth Component in the Manual")
## Declaration
public void SetVirtualParticleWeights(List<Vector3> weights); 
### Parameters
Parameter | Description  
---|---  
weights | List of weights to be used when setting virutal particles for cloth.  
### Description
Sets weights to be used when generating virtual particles for cloth.
Virtual particles provide more robust and accurate collision handling against collision spheres and capsules. More virtual particles will generally increase the accuracy of collision handling, and thus a sufficient number of virtual particles can mimic triangle-based collision handling. Virtual particles are specified as barycentric interpolation of real particles: The position of a virtual particle is w0 * P0 + w1 * P1 + w2 * P2, where P1, P2, P3 real particle positions. The barycentric weights w0, w1, w2 are stored in a separate table so they can be shared across multiple virtual particles.
* * *
