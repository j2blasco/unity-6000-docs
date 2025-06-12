* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableTraversalMode.html

# PlayableTraversalMode
enumeration
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
### Description
Traversal mode for [Playable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.Playable.html)s.
### Properties
Property | Description  
---|---  
[Mix](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableTraversalMode.Mix.html) | Causes the Playable to prepare and process it's inputs when demanded by an output.  
[Passthrough](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableTraversalMode.Passthrough.html) | Causes the Playable to act as a passthrough for PrepareFrame and ProcessFrame. If the PlayableOutput being processed is connected to the n-th input port of the Playable, the Playable only propagates the n-th output port. Use this enum value in conjunction with PlayableOutput SetSourceOutputPort.  
* * *
