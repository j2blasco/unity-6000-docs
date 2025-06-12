* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationUtility.SetKeyBroken.html

#  [AnimationUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationUtility.html).SetKeyBroken
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
public static void SetKeyBroken([AnimationCurve](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationCurve.html) curve, int index, bool broken); 
### Parameters
Parameter | Description  
---|---  
curve | The curve to modify.  
index | Keyframe index.  
broken | Broken flag.  
### Description
Change the specified keyframe broken tangent flag.
The keyframe broken flag will be used by the Curve Editor to generate tangents automatically. Changing the broken flag here will also recalculate [Keyframe.inTangent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Keyframe-inTangent.html) and [Keyframe.outTangent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Keyframe-outTangent.html).  
  
Additional resources: [AnimationUtility.SetKeyLeftTangentMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationUtility.SetKeyLeftTangentMode.html), [AnimationUtility.SetKeyRightTangentMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationUtility.SetKeyRightTangentMode.html).
* * *
