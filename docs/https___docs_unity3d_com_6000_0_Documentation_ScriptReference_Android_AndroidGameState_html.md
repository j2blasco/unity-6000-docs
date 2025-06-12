* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidGameState.html

# AndroidGameState
enumeration
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
Options for the available [game states](https://developer.android.com/reference/android/app/GameState#constants_1) that you can pass to [AndroidGame.SetGameState](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidGame.SetGameState.html) or you can set as a current game state mode to be used for [Automated game state hinting in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/android-game-state-hinting.html) using [AndroidGame.Automatic.SetGameState](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidGame.Automatic.SetGameState.html) method.
### Properties
Property | Description  
---|---  
[Unknown](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidGameState.Unknown.html) | Unknown refers to the default game state.  
[None](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidGameState.None.html) | None indicates that the game is not in active play.  
[GamePlayInterruptible](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidGameState.GamePlayInterruptible.html) | Interruptible game state, which indicates that the game is in active, but interruptible, gameplay.  
[GamePlayUninterruptible](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidGameState.GamePlayUninterruptible.html) | Uninterruptible game state, which indicates that the game is in active user play mode, which is real-time and cannot be interrupted  
[Content](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidGameState.Content.html) | Content game state, which indicates that the current content shown is not gameplay related.  
* * *
