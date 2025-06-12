* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TouchScreenKeyboard-isInPlaceEditingAllowed.html

#  [TouchScreenKeyboard](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TouchScreenKeyboard.html).isInPlaceEditingAllowed
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
isInPlaceEditingAllowed; 
### Returns
**bool** Returns true when you are able to select and modify the input field, returns false otherwise. 
### Description
Checks if the text within an input field can be selected and modified while [TouchScreenKeyboard](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TouchScreenKeyboard.html) is open.
Usually, when [TouchScreenKeyboard](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TouchScreenKeyboard.html) is open, the text within an input field cannot be selected and modified. For example, copy and paste is disabled. For Windows Store Apps on some devices, it is still possible to select and edit text when the on-screen keyboard is active.
* * *
