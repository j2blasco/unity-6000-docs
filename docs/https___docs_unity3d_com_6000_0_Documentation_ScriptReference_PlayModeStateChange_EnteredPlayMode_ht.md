* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayModeStateChange.EnteredPlayMode.html

#  [PlayModeStateChange](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayModeStateChange.html).EnteredPlayMode
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
Occurs during the next update of the Editor application if it is in play mode and was previously in edit mode.
In this condition both [EditorApplication.isPlaying](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorApplication-isPlaying.html) and [EditorApplication.isPlayingOrWillChangePlaymode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorApplication-isPlayingOrWillChangePlaymode.html) are `true`.  
  
Because this event is synchronized with the editor application's update loop, it may occur after the game's update loop has already executed one or more times.
* * *
