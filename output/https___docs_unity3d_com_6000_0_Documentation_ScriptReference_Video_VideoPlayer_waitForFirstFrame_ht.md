* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer-waitForFirstFrame.html

#  [VideoPlayer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.html).waitForFirstFrame
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
waitForFirstFrame; 
### Description
Determines whether the [VideoPlayer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.html) will wait for the first frame to be loaded into the texture before starting playback when [VideoPlayer.playOnAwake](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer-playOnAwake.html) is on.
When set to `true`, drawing into the target will only start once the [VideoPlayer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.html) preparation is done and the first frame is available in texture memory. Otherwise, the playback will start immediately even if frames are not ready, leading to the first few frames possibly being skipped.  
  
**Note:** Depending on how long the preparation takes and the underlying platform capabilities, catching up with current time after preparation completes may result in many consecutive skips.
* * *
