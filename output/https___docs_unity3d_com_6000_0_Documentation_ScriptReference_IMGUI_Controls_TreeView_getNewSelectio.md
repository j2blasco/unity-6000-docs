* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.TreeView.GetNewSelectionFunction.html

#  [TreeView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.TreeView.html).GetNewSelectionFunction
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
public delegate List<int> GetNewSelectionFunction([IMGUI.Controls.TreeViewItem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.TreeViewItem.html) clickedItem, bool keepMultiSelection, bool useActionKeyAsShift); 
### Parameters
Parameter | Description  
---|---  
clickedItem | The item clicked, or selected via keyboard.  
keepMultiSelection | Should existing selection be kept? This is used to support dragging or right-clicking one item in a multi-selection.  
useShiftAsActionKey | Should the action key be treated like the shift key? If so, the action key also indicates a range selection.  
### Description
A callback which determines how TreeView handles selection changes in response to keys and mouse clicks.
Additional resources: [getNewSelectionOverride](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.TreeView-getNewSelectionOverride.html).
* * *
