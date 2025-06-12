* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.Stop.html

#  [VideoPlayer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.html).Stop
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
public void Stop(); 
### Description
Stops the playback and sets the current time to 0.
This also destroys all internal resources such as textures or buffered content. After calling /Stop()/, [VideoPlayer.isPrepared](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer-isPrepared.html) becomes `false`.
* * *
