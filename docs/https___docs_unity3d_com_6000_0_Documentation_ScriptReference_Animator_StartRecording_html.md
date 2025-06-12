* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.StartRecording.html

#  [Animator](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html).StartRecording
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Animator.html "Go to Animator Component in the Manual")
## Declaration
public void StartRecording(int frameCount); 
### Parameters
Parameter | Description  
---|---  
frameCount | The number of frames (updates) that will be recorded. If frameCount is 0, the recording will continue until the user calls [StopRecording](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.StopRecording.html). The maximum value for frameCount is 10000.  
### Description
Sets the animator in recording mode, and allocates a circular buffer of size _frameCount_.
After this call, the recorder starts collecting up to _frameCount_ frames in the buffer. Note it is not possible to start playback until a call to [StopRecording](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.StopRecording.html) is made. Additional resources: [StopRecording](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.StopRecording.html), [recorderStartTime](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator-recorderStartTime.html), [recorderStopTime](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator-recorderStopTime.html), [StartPlayback](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.StartPlayback.html), [StopPlayback](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.StopPlayback.html), [playbackTime](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator-playbackTime.html).
* * *
