* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationUtility.SetEditorCurve.html

#  [AnimationUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationUtility.html).SetEditorCurve
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
public static void SetEditorCurve([AnimationClip](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationClip.html) clip, [EditorCurveBinding](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorCurveBinding.html) binding, [AnimationCurve](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationCurve.html) curve); 
### Parameters
Parameter | Description  
---|---  
clip | The animation clip to modify.  
binding | The binding that defines the path and the properties of the curve.  
curve | The curve to add. Set to null to remove the curve.  
### Description
Adds, modifies, or removes an editor float curve in an animation clip.
Unity internally combines position curves, scale curves, and rotation curves. When curves are combined, keyframes are set at the union of all keyframes points. In the Editor AnimationClip, you can specify special editor curves that are not combined and allows the user to edit curves in a more intuitive way.  
  
Unity has two types of animation: float curve and object reference curve. A float curve is a classic curve that animates a float property over time. An object reference curve is a construct that animates an object reference property over time.  
  
This method is used for float curves. For object reference curves, see: [AnimationUtility.SetObjectReferenceCurve](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationUtility.SetObjectReferenceCurve.html).
* * *
