* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UserAuthorization.Microphone.html

#  [UserAuthorization](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UserAuthorization.html).Microphone
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
Request permission to use any audio input sources attached to the device.
Access to microphones is required especially for the following features: 
  * Communication between players or users in the application
  * Voice commands - especially useful for accessibility
  * Voice-based game mechanics- for example the loudness of the user attracts enemies
  * Apps that analyze speech or noise, such as in language or karaoke apps
  * Playback of user’s voice
  * Voice filters


**Note** : Web doesn’t support the Microphone API. Therefore, if your application has the Web build target, the microphone permissions automatically return `false`.
* * *
