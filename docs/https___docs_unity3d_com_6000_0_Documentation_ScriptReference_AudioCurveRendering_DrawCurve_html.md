* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioCurveRendering.DrawCurve.html

#  [AudioCurveRendering](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioCurveRendering.html).DrawCurve
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
public static void DrawCurve([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) r, [AudioCurveRendering.AudioCurveEvaluator](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioCurveRendering.AudioCurveEvaluator.html) eval, [Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) curveColor); 
### Parameters
Parameter | Description  
---|---  
r | Rectangle determining the size of the graph.  
eval | Curve evaluation function.  
curveColor | Solid fill color of the curve. The alpha-channel determines the amount of opacity.  
### Description
Renders a thin curve determined by the curve evaluation function. The solid color of the curve is set by the curveColor argument.
* * *
