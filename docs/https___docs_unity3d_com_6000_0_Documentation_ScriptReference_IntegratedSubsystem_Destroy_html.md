* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IntegratedSubsystem.Destroy.html

#  [IntegratedSubsystem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IntegratedSubsystem.html).Destroy
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
public void Destroy(); 
### Description
Destroys this instance of a subsystem.
Also unloads all resources acquired during initialization step. Should be called when this instance of a subsystem is no longer needed.  
  
Note: Once a Subsystem is Destroyed, script can still hold a reference but calling a method on it will result in a NullArgumentException.
* * *
