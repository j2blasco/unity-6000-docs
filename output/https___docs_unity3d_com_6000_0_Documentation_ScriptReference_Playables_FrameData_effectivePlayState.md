* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.FrameData-effectivePlayState.html

#  [FrameData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.FrameData.html).effectivePlayState
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
[Playables.PlayState](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayState.html) effectivePlayState; 
### Description
The accumulated play state of this playable.
The effective play state is the accumulated play state of the playable and its ancestors. For example, a playable can be set to the Playing play state, but if its parent is Paused, then its effective play state is Paused.
* * *
