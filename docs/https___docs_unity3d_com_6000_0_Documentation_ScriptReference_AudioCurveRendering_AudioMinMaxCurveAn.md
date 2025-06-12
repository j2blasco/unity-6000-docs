* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioCurveRendering.AudioMinMaxCurveAndColorEvaluator.html

#  [AudioCurveRendering](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioCurveRendering.html).AudioMinMaxCurveAndColorEvaluator
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
public delegate void AudioMinMaxCurveAndColorEvaluator(float x, out [Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) col, out float minValue, out float maxValue); 
### Parameters
Parameter | Description  
---|---  
x | Normalized x-position in the range [0; 1] at which the min- and max-curves should be evaluated.  
col | Color of the curve at the specified evaluation point.  
minValue | Returned value of the minimum curve. Clamped to [-1; 1].  
maxValue | Returned value of the maximum curve. Clamped to [-1; 1].  
### Description
Curve evaluation function that allows simultaneous evaluation of the min- and max-curves. The returned minValue and maxValue values are expected to be in the range [-1; 1] and a value of 0 corresponds to the vertical center of the rectangle that is drawn into. Values outside of this range will be clamped. Additionally the color of the curve at this point is evaluated.
* * *
