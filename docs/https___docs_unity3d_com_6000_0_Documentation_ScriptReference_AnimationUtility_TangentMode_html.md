* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationUtility.TangentMode.html

# TangentMode
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
The TangentMode option for each [Keyframe](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Keyframe.html).
The Curve Editor uses the TangentMode to calculate [Keyframe.inTangent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Keyframe-inTangent.html) and [Keyframe.outTangent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Keyframe-outTangent.html).  
  
Additional resources: [AnimationUtility.SetKeyRightTangentMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationUtility.SetKeyRightTangentMode.html), [AnimationUtility.SetKeyLeftTangentMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationUtility.SetKeyLeftTangentMode.html), [AnimationUtility.SetKeyBroken](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationUtility.SetKeyBroken.html).
### Properties
Property | Description  
---|---  
[Free](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationUtility.TangentMode.Free.html) | The tangent can be freely set by dragging the tangent handle.  
[Auto](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationUtility.TangentMode.Auto.html) | The tangents are automatically set to make the curve go smoothly through the key.  
[Linear](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationUtility.TangentMode.Linear.html) | The tangent points towards the neighboring key.  
[Constant](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationUtility.TangentMode.Constant.html) | The curve retains a constant value between two keys.  
[ClampedAuto](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationUtility.TangentMode.ClampedAuto.html) | The tangents are automatically set to make the curve go smoothly through the key.  
* * *
