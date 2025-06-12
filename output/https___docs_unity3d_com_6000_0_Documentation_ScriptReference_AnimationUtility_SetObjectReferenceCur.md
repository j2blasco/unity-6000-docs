* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationUtility.SetObjectReferenceCurve.html

#  [AnimationUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationUtility.html).SetObjectReferenceCurve
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
public static void SetObjectReferenceCurve([AnimationClip](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationClip.html) clip, [EditorCurveBinding](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorCurveBinding.html) binding, ObjectReferenceKeyframe[] keyframes); 
### Parameters
Parameter | Description  
---|---  
clip | The animation clip to modify.  
binding | The bindings that define the paths and the properties of each curve.  
keyframes | Array of Object reference values over time. Setting this to null will remove the curve.  
### Description
Adds, modifies, or removes an object reference curve in an animation clip.
Unity has two types of animation: float curve and object reference curve. A float curve is a classic curve that animates a float property over time. An object reference curve is a construct that animates an object reference property over time.  
  
This method modifies object reference curves. For float curves, see [AnimationUtility.SetEditorCurve](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationUtility.SetEditorCurve.html).
* * *
