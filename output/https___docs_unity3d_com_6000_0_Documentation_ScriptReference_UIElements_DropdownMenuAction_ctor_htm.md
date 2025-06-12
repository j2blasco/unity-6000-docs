* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.DropdownMenuAction-ctor.html

# DropdownMenuAction Constructor
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
public DropdownMenuAction(string actionName, Action<DropdownMenuAction> actionCallback, Func<DropdownMenuAction,Status> actionStatusCallback, object userData); 
### Parameters
Parameter | Description  
---|---  
actionName | The path and name of the menu item. Use the path, delimited by forward slashes ('/'), to place the menu item within a submenu.  
actionCallback | The action to execute when the menu item is selected.  
actionStatusCallback | The function called to determine if the menu item is enabled.  
userData | The object to store in the <b>userData</b> property.  
### Description
Initializes a menu action with specified parameters. 
* * *
