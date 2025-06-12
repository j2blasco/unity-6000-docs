* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings-visibleInBackground.html

#  [PlayerSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.html).visibleInBackground
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PlayerSettings.html "Go to PlayerSettings Component in the Manual")
visibleInBackground; 
### Description
On Windows, shows the application in the background if the Fullscreen Windowed mode is used.
This setting lets the Windows Standalone Player running in Fullscreen mode remain visible even if you switch to another app. Typically, doing so with the Alt+Tab shortcut minimizes the initial app, but this setting prevents this behavior and the game window continues to run in Fullscreen even when another app has focus. If you set **visibleInBackground** to false and you Alt+Tab out of the application, it will minimize. However, if you set **visibleInBackground** to true, the application will not minimize and remain visible behind other windows.
**Note:** When set to Fullscreen mode, the Unity app window cannot be minimized with most keyboard shortcuts, especially:
- Alt+Tab to switch to another app window won't minimize the Unity app. 
- Windows+M to minimize the active window. 
- The setting has no effect on ExclusiveFullscreen mode and it will always minimize. 
Additionally, Windows+D shortcut will always force the app to minimize regardless of the **visibleInBackground** setting.
* * *
