* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings-muteOtherAudioSources.html

#  [PlayerSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.html).muteOtherAudioSources
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
muteOtherAudioSources; 
### Description
Stops or allows audio from other applications to play in the background while your Unity application is running.
This setting is shared between iOS and Android platforms.  
  
Set this to true and your Unity application stops audio from other applications in the background, set to false and audio from background applications continues to play alongside your Unity application.  
  
Unity ignores `PlayerSettings.muteOtherAudioSources` if at least one of the following is true:
  * Unity Audio is disabled. (menu: **Edit** > **Project Settings** > **Audio** > **Disable Unity Audio**)
  * Unity has stripped the AudioManager from the project at build time.


AudioManager is stripped from the project if all of the following are true:
  * There is no audio content in the project.
  * The project uses IL2CPP.
  * [Strip Engine Code](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings-stripEngineCode.html) is enabled.


Note: Starting with Android Marshmallow (6.0), setting this to false mutes the sound of your Unity application during an incoming phone call (while the phone is ringing). If you want to have this behavior on older Android versions, you have to add the READ_PHONE_STATE permission to the manifest. See [the Android documentation](https://developer.android.com/guide/topics/manifest/manifest-intro.html) for more information on build manifests.
* * *
