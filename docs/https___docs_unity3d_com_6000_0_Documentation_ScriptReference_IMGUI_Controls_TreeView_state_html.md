* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.TreeView-state.html

#  [TreeView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.TreeView.html).state
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
[IMGUI.Controls.TreeViewState](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.TreeViewState.html) state; 
### Description
The state of the TreeView (expanded state, selection, scroll etc.)
The TreeViewState contains state information that the user could have changed, for example the selection state, expanded state, and scroll state. The TreeViewState is the only state that should be serialized/deserialized in the TreeView. This object is passed in when creating the TreeView and it is up to the client of the TreeView to decide how it should be persisted. For Editor windows it will usually be a serialized field in the window. The TreeView changes the state in this object when the user interacts with the TreeView.
* * *
