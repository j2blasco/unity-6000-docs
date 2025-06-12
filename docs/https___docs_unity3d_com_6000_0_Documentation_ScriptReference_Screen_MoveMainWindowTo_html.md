* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Screen.MoveMainWindowTo.html

#  [Screen](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Screen.html).MoveMainWindowTo
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
public static [AsyncOperation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AsyncOperation.html) MoveMainWindowTo(ref [DisplayInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DisplayInfo.html) display, [Vector2Int](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2Int.html) position); 
### Parameters
Parameter | Description  
---|---  
display | The target display where the window should move to.  
position | The position the window moves to. Relative to the top left corner of the specified display in pixels.  
### Returns
**AsyncOperation** Returns AsyncOperation that represents moving the window. 
### Description
Moves the main window to the specified position relative to the top left corner of the specified display. Position value is represented in pixels. Moving the window is an asynchronous operation, which can take multiple frames.
Window movement adheres to the current fullscreen mode. If the current fullscreen mode is set to fullscreen, then Unity snaps the position to the top left corner of the display and resizes it to fit.  
  
This API is only supported on Linux, macOS and Windows Standalone.
* * *
