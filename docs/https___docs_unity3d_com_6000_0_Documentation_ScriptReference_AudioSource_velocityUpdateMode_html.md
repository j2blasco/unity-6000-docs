* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource-velocityUpdateMode.html

#  [AudioSource](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.html).velocityUpdateMode
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
[AudioVelocityUpdateMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioVelocityUpdateMode.html) velocityUpdateMode; 
### Description
Whether the Audio Source should be updated in the fixed or dynamic update.
Make sure this is set to update in the same update loop as the Audio Source is moved in if you are experiencing problems with Doppler effect simulation for this source. The default setting will automatically set the source to be updated in the fixed update loop if it is attached to a rigidbody, and dynamic otherwise.
* * *
