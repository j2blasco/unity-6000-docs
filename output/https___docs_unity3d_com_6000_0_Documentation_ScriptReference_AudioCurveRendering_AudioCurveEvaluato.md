* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioCurveRendering.AudioCurveEvaluator.html

#  [AudioCurveRendering](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioCurveRendering.html).AudioCurveEvaluator
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
public delegate float AudioCurveEvaluator(float x); 
### Parameters
Parameter | Description  
---|---  
x | Normalized x-position in the range [0; 1] at which the curve should be evaluated.  
### Description
Curve evaluation function used to evaluate the curve y-value and at the specified point.
* * *
