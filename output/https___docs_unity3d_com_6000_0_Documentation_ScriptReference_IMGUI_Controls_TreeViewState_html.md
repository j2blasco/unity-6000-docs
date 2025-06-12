* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.TreeViewState.html

# TreeViewState
class in UnityEditor.IMGUI.Controls
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
### Description
The TreeViewState contains serializable state information for the TreeView.
This is primarily state that the user could have changed by interacting with the TreeView, for example the selection state, expanded state, navigation state and scroll state.  
  
The TreeViewState is the only state that should be serialized/deserialized in the TreeView. The TreeView itself is not serializable and should be reconstructed from the tree data it is representing.  
  
All the state contained in this class is updated by the TreeView itself. Access to this state can also be done through the TreeView API.
### Properties
Property | Description  
---|---  
[expandedIDs](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.TreeViewState-expandedIDs.html) | This is the list of currently expanded TreeViewItem IDs.  
[lastClickedID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.TreeViewState-lastClickedID.html) | The ID for the TreeViewItem that currently is being used for multi selection and key navigation.  
[scrollPos](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.TreeViewState-scrollPos.html) | The current scroll values of the TreeView's scroll view.  
[searchString](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.TreeViewState-searchString.html) | Search string state that can be used in the TreeView to filter the tree data when creating the TreeViewItems.  
[selectedIDs](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.TreeViewState-selectedIDs.html) | Selected TreeViewItem IDs. Use of the SetSelection and IsSelected API will access this state.  
* * *
