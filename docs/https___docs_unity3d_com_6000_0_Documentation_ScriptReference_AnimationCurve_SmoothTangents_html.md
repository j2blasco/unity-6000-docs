* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationCurve.SmoothTangents.html

#  [AnimationCurve](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationCurve.html).SmoothTangents
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
public void SmoothTangents(int index, float weight); 
### Parameters
Parameter | Description  
---|---  
index | The index of the keyframe to be smoothed.  
weight | The smoothing weight to apply to the keyframe's tangents.  
### Description
Smooth the in and out tangents of the keyframe at `index`.
A weight of 0 evens out tangents.
* * *
