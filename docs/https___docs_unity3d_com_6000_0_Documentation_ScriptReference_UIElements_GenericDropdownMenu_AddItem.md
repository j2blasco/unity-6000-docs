* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.GenericDropdownMenu.AddItem.html

#  [GenericDropdownMenu](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.GenericDropdownMenu.html).AddItem
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
public void AddItem(string itemName, bool isChecked, [Unity.Android.Gradle.Manifest.Action](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Manifest.Action.html) action); 
### Parameters
Parameter | Description  
---|---  
itemName | The text to display to the user.  
isChecked | Indicates whether a checkmark next to the item is displayed.  
action | The callback to invoke when the item is selected by the user.  
### Description
Adds an item to this menu using a default VisualElement. 
* * *
## Declaration
public void AddItem(string itemName, bool isChecked, Action<object> action, object data); 
### Parameters
Parameter | Description  
---|---  
itemName | The text to display to the user.  
isChecked | Indicates whether a checkmark next to the item is displayed.  
action | The callback to invoke when the item is selected by the user.  
data | The object to pass to the callback as a parameter.  
### Description
Adds an item to this menu using a default VisualElement. 
This overload of the method accepts an arbitrary object that's passed as a parameter to your callback. 
* * *
