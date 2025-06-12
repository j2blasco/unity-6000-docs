* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource-priority.html

#  [AudioSource](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.html).priority
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
priority; 
### Description
Sets the priority of the [AudioSource](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.html).
Unity virtualizes AudioSources when the number of active AudioSources exceeds the limit set by your project's maximum real voices. Real voices are audio sources that are audible in the scene.   
  
Virtualization is when Unity makes the AudioSource inaudible, but still keeps track of the audio's playback position and state so it's ready to be a real voice when their priority or volume overtakes another sound. Unity virtualizes AudioSources with the lowest priority first, followed by volume if two sounds have the same priority. Priority is an integer between 0 (high priority) and 255 (low priority).  
  
To change the value of the maximum number of real or virtual voices: 
  1. In the menu go to **Edit** > **Project Settings** > **Audio**.
  2. Set **Maximum Real Voices** and **Maximum Virtual Voices** to your preferred values


**WebGL:** This setting doesn't affect WebGL because there is no limit on the number of audio channels in the WebGL platform.
* * *
