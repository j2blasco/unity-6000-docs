* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.CurveFilterOptions-unrollRotation.html

#  [CurveFilterOptions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.CurveFilterOptions.html).unrollRotation
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
unrollRotation; 
### Description
Whether to apply rotation unrolling. This option is enabled by default.
Enable this option to unroll rotation curves. This results in rotation curves with keys set to all values rather than being set between -180 and 180 degrees. Unrolling rotation curves may apply keyframe reduction. Use [CurveFilterOptions.floatError](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.CurveFilterOptions-floatError.html) to set the keyframe reduction tolerance. Note that the unroll filter is applied to curves with the bindings localEulerAngles, localEulerAnglesBaked and localEulerAnglesRaw bound to transforms. The unroll filter is only applied to rotations with curves present on all three axes (x, y, and z).
* * *
