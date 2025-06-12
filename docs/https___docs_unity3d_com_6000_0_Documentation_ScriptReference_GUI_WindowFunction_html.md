* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.WindowFunction.html

#  [GUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.html).WindowFunction
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
public delegate void WindowFunction(int id); 
### Description
Callback to draw GUI within a window (used with [GUI.Window](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Window.html)).
This function takes the ID number of the window to be drawn. Its body should contain GUI calls to display the window, much like a standard OnGUI function. This function can then be passed as a parameter to [GUI.Window](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Window.html) to draw the appropriate contents.
* * *
