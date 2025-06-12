* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioCurveRendering.AudioCurveAndColorEvaluator.html

#  [AudioCurveRendering](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioCurveRendering.html).AudioCurveAndColorEvaluator
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
public delegate float AudioCurveAndColorEvaluator(float x, out [Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) col); 
### Parameters
Parameter | Description  
---|---  
x | Normalized x-position in the range [0; 1] at which the curve should be evaluated.  
col | Color of the curve at the evaluated point.  
### Description
Curve evaluation function that allows simultaneous evaluation of the curve y-value and a color of the curve at that point.
* * *
