* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cloth.GetSelfAndInterCollisionIndices.html

#  [Cloth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cloth.html).GetSelfAndInterCollisionIndices
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
public void GetSelfAndInterCollisionIndices(List<uint> indices); 
### Parameters
Parameter | Description  
---|---  
indices | List to be populated with cloth particle indices that are used for self and/or inter collision.  
### Description
Get list of particles to be used for self and inter collision.
This allows you to access the cloth indices used for self and inter collision. The same set of indices is used in both situations if necessary. To enable self-collision, both self-collision distance and self-collision stiffness should be set to to non-zero values. To enable inter-collision, both inter-collision distance and inter-collision stiffness should be set to to non-zero values.
* * *
