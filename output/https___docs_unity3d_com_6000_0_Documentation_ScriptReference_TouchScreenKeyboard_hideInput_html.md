* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TouchScreenKeyboard-hideInput.html

#  [TouchScreenKeyboard](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TouchScreenKeyboard.html).hideInput
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
hideInput; 
### Description
Will text input field above the keyboard be hidden when the keyboard is on screen?
This property is applicable for single line text fields that have assigned keyboard with alphanumeric keys. When TouchScreenKeyboard.hideInputs is set to true, the only type of keyboard that can be opened is [TouchScreenKeyboardType.Default](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TouchScreenKeyboardType.Default.html). This type of keyboard will be opened even if other types are specified to be opened.  
  
  
**Android:** There is no reliable way of hiding input field. Unity provides this property which, when you enable it, renders the input field outside of the screen. This gives the illusion of a hidden input field.
* * *
