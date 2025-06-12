* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationUtility.GetEditorCurve.html

#  [AnimationUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationUtility.html).GetEditorCurve
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
**Obsolete** This overload is deprecated. Use the one with EditorCurveBinding instead.
## Declaration
public static [AnimationCurve](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationCurve.html) GetEditorCurve([AnimationClip](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationClip.html) clip, string relativePath, Type type, string propertyName); 
## Declaration
public static [AnimationCurve](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationCurve.html) GetEditorCurve([AnimationClip](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationClip.html) clip, [EditorCurveBinding](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorCurveBinding.html) binding); 
### Description
Retrieves the float curve that the binding points to.
Unity internally combines position curves, scale curves, and rotation curves. When curves are combined, keyframes are set at the union of all keyframes points. In the Editor AnimationClip, you can specify special editor curves that are not combined and allows the user to edit curves in a more intuitive way.  
  
See also: [AnimationUtility.GetObjectReferenceCurve](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationUtility.GetObjectReferenceCurve.html).
* * *
