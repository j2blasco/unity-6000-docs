* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorStateTransition-hasFixedDuration.html

#  [AnimatorStateTransition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorStateTransition.html).hasFixedDuration
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
hasFixedDuration; 
### Description
Determines whether the duration of the transition is reported in a fixed duration in seconds or as a normalized time.
If `hasFixedDuration` is true, the transition duration is in seconds.  
  
If `hasFixedDuration` is false, the transition duration is in normalized time.  
  
**Note:** In normalized time, a duration of 1 makes the transition the same length as the state that triggered it. A value of 2, for instance, would make the transition twice as long as the state that triggered it.
* * *
