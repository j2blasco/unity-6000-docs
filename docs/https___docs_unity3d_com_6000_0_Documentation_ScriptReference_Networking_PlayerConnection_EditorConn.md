* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.PlayerConnection.EditorConnection.Initialize.html

#  [EditorConnection](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.PlayerConnection.EditorConnection.html).Initialize
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
public void Initialize(); 
### Description
Initializes the EditorConnection.
Starts listening for Players. If all the Players disconnect, the socket gets cleaned up, so you need to reinitialize the socket if you expect more connections.
* * *
