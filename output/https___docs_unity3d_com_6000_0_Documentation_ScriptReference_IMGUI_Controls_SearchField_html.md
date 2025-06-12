* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.SearchField.html

# SearchField
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
The SearchField control creates a text field for a user to input text that can be used for searching.
It comes in two UI styles: one for normal usage and one for toolbars.
### Properties
Property | Description  
---|---  
[autoSetFocusOnFindCommand](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.SearchField-autoSetFocusOnFindCommand.html) | Changes the keyboard focus to the search field when the user presses ‘Ctrl/Cmd + F’ when set to true. It is true by default.  
[searchFieldControlID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.SearchField-searchFieldControlID.html) | This is the controlID used for the text field to obtain keyboard focus.  
### Public Methods
Method | Description  
---|---  
[HasFocus](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.SearchField.HasFocus.html) | This function returns true if the search field has keyboard focus.  
[OnGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.SearchField.OnGUI.html) | This function displays the search field with the default UI style and uses the GUILayout class to automatically calculate the position and size of the Rect it is rendered to. Pass an optional list to specify extra layout properties.  
[OnToolbarGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.SearchField.OnToolbarGUI.html) | This function displays the search field with the toolbar UI style and uses the GUILayout class to automatically calculate the position and size of the Rect it is rendered to. Pass an optional list to specify extra layout properties.  
[SetFocus](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.SearchField.SetFocus.html) | This function changes keyboard focus to the search field so a user can start typing.  
### Events
Event | Description  
---|---  
[downOrUpArrowKeyPressed](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.SearchField-downOrUpArrowKeyPressed.html) | This event is dispatched when the focused search field detects that the down or up key is pressed and can be used to change keyboard focus to another control, such as the TreeView.  
### Delegates
Delegate | Description  
---|---  
[SearchFieldCallback](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.SearchField.SearchFieldCallback.html) | This is a generic callback delegate for SearchField events and does not take any parameters.  
* * *
