* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationUtility.CalculateTransformPath.html

#  [AnimationUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationUtility.html).CalculateTransformPath
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
public static string CalculateTransformPath([Transform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) targetTransform, [Transform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) root); 
### Returns
**string** Returns a string that represents the path from the root Transform to the target Transform. 
### Description
Retrieves the path from the root Transform to the target Transform.
The root Transform does not need to be an actual root, but it must be higher in the hierarchy than the target Transform. The target and root may also be the same Transform.
* * *
