* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input-compositionCursorPos.html

#  [Input](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.html).compositionCursorPos
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
[Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) compositionCursorPos; 
### Description
The current text input position used by IMEs to open windows.
**Note** : This API is part of the legacy Input Manager. The recommended best practice is that you don't use this API in new projects. For new projects, use the Input System package. To learn more about input, refer to [Input](https://docs.unity3d.com/6000.0/Documentation/Manual/Input.html).  
  
Some language IMEs such as Japanese will open windows while the user is typing text, to aid the user in picking the correct input strings. These windows are expected to pop up at the current cursor position, so the IME needs to know where input is displayed. When using Unity's built in GUI system for text input, Unity will take care of setting the cursor position for the IME. However, if you wish to implement your own GUI for text input, you need to set this to the current text input position for IME windows to show up correctly. Additional resources: [Input.imeCompositionMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input-imeCompositionMode.html), [Input.compositionString](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input-compositionString.html).
* * *
