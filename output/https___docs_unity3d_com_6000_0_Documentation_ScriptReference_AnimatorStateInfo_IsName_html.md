* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimatorStateInfo.IsName.html

#  [AnimatorStateInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimatorStateInfo.html).IsName
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
public bool IsName(string name); 
### Description
Does `name` match the name of the active state in the statemachine?
The name should be in the form _Layer.Name_ or _Layer.SubStateMachine.Name_. For example, `Base.Idle` or `Base.RunSM.JogForward`.
* * *
