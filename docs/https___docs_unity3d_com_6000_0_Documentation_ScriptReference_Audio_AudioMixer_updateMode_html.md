* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Audio.AudioMixer-updateMode.html

#  [AudioMixer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Audio.AudioMixer.html).updateMode
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
[Audio.AudioMixerUpdateMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Audio.AudioMixerUpdateMode.html) updateMode; 
### Description
How time should progress for this AudioMixer. Used during Snapshot transitions.
During update of AudioMixers and Snapshot transitions, this property defines how those transitions should progress. 
  * AudioMixerUpdateMode.Normal updates the AudioMixer with scaled game time progression.
  * AudioMixerUpdateMode.UnscaledTime ignores [Time.timeScale](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-timeScale.html) changes and updates the AudioMixer in realtime.


* * *
