* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioListener-pause.html

#  [AudioListener](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioListener.html).pause
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioListener.html "Go to AudioListener Component in the Manual")
pause; 
### Description
The paused state of the audio system.
If set to true, all AudioSources playing will be paused. This works in the same way as pausing the game in the editor. While the pause-state is true, the [AudioSettings.dspTime](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSettings-dspTime.html) will be frozen and further AudioSource play requests will start off paused. If you want certain sounds to still play during the pause, you need to set the ignoreListenerPause property on the AudioSource to true for these. This is typically menu item sounds or background music for the menu. Any scheduled play requests will be frozen in time, so that if you scheduled a sound to play after 3 seconds and paused the audio system 1 second after this, the scheduled sounds will start playing 2 seconds after unpausing.
* * *
