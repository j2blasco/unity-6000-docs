* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.PlayDelayed.html

#  [AudioSource](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.html).PlayDelayed
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioSource.html "Go to AudioSource Component in the Manual")
## Declaration
public void PlayDelayed(float delay); 
### Parameters
Parameter | Description  
---|---  
delay | Delay time specified in seconds.  
### Description
Plays the [clip](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource-clip.html) with a delay specified in seconds. Users are advised to use this function instead of the old Play(delay) function that took a delay specified in samples relative to a reference rate of 44.1 kHz as an argument.
**Note:** This function replaces the Play(delay) function when called with the delay-argument. In that function the delay had to be specified as samples relative to a reference rate of 44100. This is inconvenient when the engine is running on a different sample rate and the source sound has an even different rate. Working with delays specified in seconds makes this independent of these.
* * *
