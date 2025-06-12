* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimatorUtility.OptimizeTransformHierarchy.html

#  [AnimatorUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimatorUtility.html).OptimizeTransformHierarchy
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
public static void OptimizeTransformHierarchy([GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) go, string[] exposedTransforms); 
### Parameters
Parameter | Description  
---|---  
go | GameObject to Optimize.  
exposedTransforms | List of transform name to expose.  
### Description
This function will remove all transform hierarchy under GameObject, the animator will write directly transform matrices into the skin mesh matrices saving many CPU cycles.
You can optionally provide a list of transform name, this function will create a flattened hierarchy of these transform under GameObject.  
  
A call to this function at runtime will re-initialize the animator.  
  
Additional resources: [AnimatorUtility.OptimizeTransformHierarchy](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimatorUtility.OptimizeTransformHierarchy.html), [Animator.hasTransformHierarchy](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator-hasTransformHierarchy.html).
* * *
