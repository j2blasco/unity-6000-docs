* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.PlayOnGamepad.html

#  [AudioSource](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.html).PlayOnGamepad
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
public bool PlayOnGamepad(int slot); 
### Parameters
Parameter | Description  
---|---  
slot | Slot number of the gamepad (0-3).  
### Returns
**bool** Returns TRUE if enabling audio output through this users controller was successful. 
### Description
Enable the audio source to play through a specific gamepad.
Set your current [BuildTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildTarget.html) to **PS4** or **PS5** to avoid a build error in the Windows Editor.
* * *
