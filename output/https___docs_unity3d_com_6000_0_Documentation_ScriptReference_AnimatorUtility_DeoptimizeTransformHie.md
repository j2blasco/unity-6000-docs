* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimatorUtility.DeoptimizeTransformHierarchy.html

#  [AnimatorUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimatorUtility.html).DeoptimizeTransformHierarchy
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
public static void DeoptimizeTransformHierarchy([GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) go); 
### Parameters
Parameter | Description  
---|---  
go | GameObject to Deoptimize.  
### Description
This function will recreate all transform hierarchy under GameObject.
A call to this function at runtime will re-initialize the animator.  
  
Additional resources: [AnimatorUtility.OptimizeTransformHierarchy](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimatorUtility.OptimizeTransformHierarchy.html), [Animator.hasTransformHierarchy](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator-hasTransformHierarchy.html).
* * *
