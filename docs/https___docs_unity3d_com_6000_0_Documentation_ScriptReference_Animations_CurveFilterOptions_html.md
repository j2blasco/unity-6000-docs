* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.CurveFilterOptions.html

# CurveFilterOptions
struct in UnityEditor.Animations
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
The keyframe reduction settings for compressing animation curves.
Use the CurveFilterOptions when saving a recording to a clip. A value of 0.5 gives a light compression. Additional resources: [GameObjectRecorder.SaveToClip](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.GameObjectRecorder.SaveToClip.html).
### Properties
Property | Description  
---|---  
[floatError](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.CurveFilterOptions-floatError.html) | The amount the float animation curve is allowed to deviate from its original curve. This amount is expressed as a percentage: a positive value between 0 and 100.  
[keyframeReduction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.CurveFilterOptions-keyframeReduction.html) | Whether to apply keyframe reduction.  
[positionError](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.CurveFilterOptions-positionError.html) | The amount the position animation curve is allowed to deviate from its original curve. This amount is expressed as a percentage: a positive value between 0 and 100.  
[rotationError](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.CurveFilterOptions-rotationError.html) | The amount the rotation animation curve is allowed to deviate from its original curve. This amount is expressed as a number of degrees. It should be a positive value between 0 and 180.  
[scaleError](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.CurveFilterOptions-scaleError.html) | The amount the scale animation curve is allowed to deviate from its original curve. This amount is expressed as a percentage: a positive value between 0 and 100.  
[unrollRotation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.CurveFilterOptions-unrollRotation.html) | Whether to apply rotation unrolling. This option is enabled by default.  
* * *
