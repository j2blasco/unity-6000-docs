* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HumanTrait.GetBoneDefaultHierarchyMass.html

#  [HumanTrait](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HumanTrait.html).GetBoneDefaultHierarchyMass
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
public static float GetBoneDefaultHierarchyMass(int i); 
### Parameters
Parameter | Description  
---|---  
i | The humanoid bone index.  
### Returns
**float** The bone hierarchy mass. 
### Description
Gets the bone hierarchy mass.
The default bone mass is used to compute the mass center. The default bone mass is an approximation based on the weight of a human with normal proportions. Additional resources: [Animator.bodyPosition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator-bodyPosition.html) [AnimationHumanStream.bodyPosition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationHumanStream-bodyPosition.html) [AnimationHumanStream.bodyLocalPosition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationHumanStream-bodyLocalPosition.html).
* * *
