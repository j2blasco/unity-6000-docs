* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.ShowAsDropDown.html

#  [EditorWindow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html).ShowAsDropDown
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
public void ShowAsDropDown([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) buttonRect, [Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) windowSize); 
### Parameters
Parameter | Description  
---|---  
buttonRect | The button from which the position of the window will be determined (see description).  
windowSize | The initial size of the window.  
### Description
Shows a window with dropdown behaviour and styling.
The window is styled in the same way as a [PopupWindow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PopupWindow.html). The window is automatically closed when it loses focus. Note this function auto-fits the window to screen while trying to place it first below then above the button it was triggered from. This means the windowSize might change when fitting it to screen, so you should make sure you read the 'position' afterwards to check whether the size was cropped.
* * *
