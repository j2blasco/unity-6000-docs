* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cursor.html

# Cursor
class in UnityEngine
/
Implemented in:[UnityEngine.CoreModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.CoreModule.html)
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
Cursor API for setting the cursor (mouse pointer).
Supports hardware cursors on macOS, Windows and Linux. Falls back to software cursors on unsupported platforms.  
  
**Windows Store Apps** : Supports only one hardware cursor, set via [PlayerSettings.defaultCursor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings-defaultCursor.html), cursors created at runtime using [Cursor.SetCursor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cursor.SetCursor.html) are treated as software cursors.  
  
**Android** : Supports custom hardware cursors on version 7.0 and later. There is no hardware or software custom cursor support before 7.0.  
  
Textures used as cursors should be marked as such in their import settings.
### Static Properties
Property | Description  
---|---  
[lockState](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cursor-lockState.html) | Determines whether the hardware pointer is locked to the center of the view, constrained to the window, or not constrained at all.  
[visible](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cursor-visible.html) | Determines whether the hardware pointer is visible or not.  
### Static Methods
Method | Description  
---|---  
[SetCursor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cursor.SetCursor.html) | Sets a custom cursor to use as your cursor.  
* * *
