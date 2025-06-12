* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioListener-velocityUpdateMode.html

#  [AudioListener](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioListener.html).velocityUpdateMode
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
[AudioVelocityUpdateMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioVelocityUpdateMode.html) velocityUpdateMode; 
### Description
This lets you set whether the Audio Listener should be updated in the fixed or dynamic update.
Make sure this is set to update in the same update loop as the Audio Listener is moved in if you are experiencing problems with Doppler effect simulation. The default setting will automatically set the listener to be updated in the fixed update loop if it is attached to a rigidbody, and dynamic otherwise.
* * *
