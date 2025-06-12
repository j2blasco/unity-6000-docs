* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationUtility.SetEditorCurves.html

#  [AnimationUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationUtility.html).SetEditorCurves
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
public static void SetEditorCurves([AnimationClip](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationClip.html) clip, EditorCurveBinding[] bindings, AnimationCurve[] curves); 
### Parameters
Parameter | Description  
---|---  
clip | The animation clip to modify.  
binding | The binding that defines the path and the properties of each curve.  
curves | The curves to add. Setting curves in the array to null will remove these curves from the clip.  
### Description
Adds, modifies, or removes multiple editor float curves in an animation clip.
This method is the equivalent of calling [AnimationUtility.SetEditorCurve](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationUtility.SetEditorCurve.html) for each individual curve, but applies relevant post-processing operations only once. This method is used for float curves. For object reference curves, see: [AnimationUtility.SetObjectReferenceCurves](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationUtility.SetObjectReferenceCurves.html).
* * *
