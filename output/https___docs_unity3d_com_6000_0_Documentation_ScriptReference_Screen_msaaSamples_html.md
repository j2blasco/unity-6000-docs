* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Screen-msaaSamples.html

#  [Screen](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Screen.html).msaaSamples
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
msaaSamples; 
### Description
Get the requested MSAA sample count of the screen buffer.
Gets the sample count last requested by [SetMSAASamples](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Screen.SetMSAASamples.html). This value might be different from the actual sample count that Unity uses for the render target during this frame, since Unity does not update the number of samples immediately. Depending on when in the frame you access this property, it might return the sample count of the current frame or the next frame. If the graphics API does not support the value provided, it uses the next highest supported value.
* * *
