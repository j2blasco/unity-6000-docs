* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorState-timeParameter.html

#  [AnimatorState](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorState.html).timeParameter
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
timeParameter; 
### Description
If timeParameterActive is true, the value of this Parameter will be used instead of normalized time.
Parametrized Time and Root motion are not compatible. Root motion relies on previous and current time to compute a delta displacement. When you activate parametrized time, root motion is not computed anymore when this state is playing.
* * *
