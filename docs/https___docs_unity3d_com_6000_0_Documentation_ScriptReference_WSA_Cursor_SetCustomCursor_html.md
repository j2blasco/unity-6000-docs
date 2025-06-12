* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WSA.Cursor.SetCustomCursor.html

#  [Cursor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WSA.Cursor.html).SetCustomCursor
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
public static void SetCustomCursor(uint id); 
### Parameters
Parameter | Description  
---|---  
id | The cursor resource id.  
### Description
Set a custom cursor.
This creates new CoreCursor(CoreCursorType::Custom, id) and assigns it to CoreIndependentInputSource.PointerCursor if independent input source is enabled, otherwise it's assigned to CoreWindow.PointerCursor. The resource id for cursor is created inside Win32 .RC file. **Note:** Passing 0 will reset cursor to the arrow icon.
* * *
