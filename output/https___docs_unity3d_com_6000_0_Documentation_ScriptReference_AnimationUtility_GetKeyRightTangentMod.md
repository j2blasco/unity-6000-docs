* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationUtility.GetKeyRightTangentMode.html

#  [AnimationUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationUtility.html).GetKeyRightTangentMode
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
public static [AnimationUtility.TangentMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationUtility.TangentMode.html) GetKeyRightTangentMode([AnimationCurve](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationCurve.html) curve, int index); 
### Parameters
Parameter | Description  
---|---  
curve | Curve to query.  
index | Keyframe index.  
### Returns
**TangentMode** Returns the tangent mode. 
### Description
Retrieves the right tangent mode of the keyframe at a specific index.
The Curve Editor uses the keyframe tangent mode to automatically generate tangents.  
  
Additional resources: [AnimationUtility.GetKeyLeftTangentMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationUtility.GetKeyLeftTangentMode.html), [AnimationUtility.GetKeyBroken](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationUtility.GetKeyBroken.html).
* * *
