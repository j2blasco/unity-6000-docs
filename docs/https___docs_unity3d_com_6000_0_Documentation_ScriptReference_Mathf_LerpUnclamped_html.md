* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.LerpUnclamped.html

#  [Mathf](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.html).LerpUnclamped
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Mathf.html "Go to Mathf Component in the Manual")
## Declaration
public static float LerpUnclamped(float a, float b, float t); 
### Parameters
Parameter | Description  
---|---  
a | The start value.  
b | The end value.  
t | The interpolation between the two floats.  
### Returns
**float** The float value as a result from the linear interpolation. 
### Description
Linearly interpolates between `a` and `b` by `t` with no limit to `t`.
The parameter `t` is not clamped and a value based on `a` and `b` is supported. If `t` is less than zero, or greater than one, then [LerpUnclamped](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.LerpUnclamped.html) will result in a return value outside the range `a` to `b`.  
  
Suppose parameter `a` = 0.33f, and `b` = 1.5f. If interpolator `t` = -0.25f then the return value is 0.0375f.  
  
**Details:** The calculation (`b` - `a`) is 1.17f. This is scaled by 0.25f and a result of 0.2925f is obtained. Subtracting this from `a` (because the interpolant `t` is negative) results in 0.0375f.  
  
Additional resources: [Lerp](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.Lerp.html).
* * *
