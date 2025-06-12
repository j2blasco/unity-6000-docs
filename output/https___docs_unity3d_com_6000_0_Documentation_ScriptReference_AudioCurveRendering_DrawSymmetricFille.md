* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioCurveRendering.DrawSymmetricFilledCurve.html

#  [AudioCurveRendering](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioCurveRendering.html).DrawSymmetricFilledCurve
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
public static void DrawSymmetricFilledCurve([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) r, [AudioCurveRendering.AudioCurveAndColorEvaluator](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioCurveRendering.AudioCurveAndColorEvaluator.html) eval); 
### Parameters
Parameter | Description  
---|---  
r | Rectangle determining the size of the graph.  
eval | Normalized x-position in the range [0; 1] at which the curve should be evaluated. The returned value is expected to be in the range [0; 1] and a value of 0 corresponds to the vertical center of the rectangle that is drawn into. Values outside of this range will be clamped.  
### Description
Fills the area between the curve evaluated by the AudioCurveAndColorEvaluator provided and its vertical mirror image with smooth gradients along the edges. Useful for drawing amplitude plots of audio signals.
* * *
