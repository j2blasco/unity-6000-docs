* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimatorTransitionInfo-duration.html

#  [AnimatorTransitionInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimatorTransitionInfo.html).duration
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
duration; 
### Description
Duration of the transition.
Depending on [AnimatorTransitionInfo.durationUnit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimatorTransitionInfo-durationUnit.html) the duration can either be expressed in seconds (i.e. [DurationUnit.Fixed](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DurationUnit.Fixed.html)) or in percentage (i.e. [DurationUnit.Normalized](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DurationUnit.Normalized.html)). A normalized duration is based on the source state duration.  
  
Note: a normalized duration converted in seconds can change from frame to frame, since the source state duration can change depending on varying factors, like the weights in a blendtree.
* * *
