* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationUtility.SetKeyLeftTangentMode.html

#  [AnimationUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationUtility.html).SetKeyLeftTangentMode
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
public static void SetKeyLeftTangentMode([AnimationCurve](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationCurve.html) curve, int index, [AnimationUtility.TangentMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationUtility.TangentMode.html) tangentMode); 
### Parameters
Parameter | Description  
---|---  
curve | The curve to modify.  
index | Keyframe index.  
tangentMode | Tangent mode.  
### Description
Change the specified keyframe tangent mode.
The keyframe tangent mode will be used by the Curve Editor to generate tangents automatically. Changing the tangent mode here will also recalculate [Keyframe.inTangent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Keyframe-inTangent.html) and [Keyframe.outTangent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Keyframe-outTangent.html).  
  
Additional resources: [AnimationUtility.SetKeyRightTangentMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationUtility.SetKeyRightTangentMode.html), [AnimationUtility.SetKeyBroken](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationUtility.SetKeyBroken.html).
* * *
