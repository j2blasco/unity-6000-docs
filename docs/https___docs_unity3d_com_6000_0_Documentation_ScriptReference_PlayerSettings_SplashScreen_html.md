* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.SplashScreen.html

# SplashScreen
class in UnityEditor
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
### Description
Interface to splash screen player settings.
### Static Properties
Property | Description  
---|---  
[animationBackgroundZoom](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.SplashScreen-animationBackgroundZoom.html) | The target zoom (from 0 to 1) for the background when it reaches the end of the SplashScreen animation's total duration. Only used when animationMode is AnimationMode.Custom.  
[animationLogoZoom](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.SplashScreen-animationLogoZoom.html) | The target zoom (from 0 to 1) for the logo when it reaches the end of the logo animation's total duration. Only used when animationMode is AnimationMode.Custom.  
[animationMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.SplashScreen-animationMode.html) | The type of animation applied during the splash screen.  
[background](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.SplashScreen-background.html) | The background Sprite that is shown in landscape mode. Also shown in portrait mode if backgroundPortrait is null.  
[backgroundColor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.SplashScreen-backgroundColor.html) | Sets the background color of the splash screen when no background image is used. The default background color is dark blue RGB(34.44,54).  
[backgroundPortrait](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.SplashScreen-backgroundPortrait.html) | The background Sprite that is shown in portrait mode.  
[blurBackgroundImage](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.SplashScreen-blurBackgroundImage.html) | Determines whether Unity applies a blur effect to the background Sprite on the Splash Screen.  
[drawMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.SplashScreen-drawMode.html) | Determines how the Unity logo should be drawn, if it is enabled. If no Unity logo exists in [logos] then the draw mode defaults to DrawMode.UnityLogoBelow.  
[logos](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.SplashScreen-logos.html) | The collection of logos that is shown during the splash screen. Logos are drawn in ascending order, starting from index 0, followed by 1, etc etc.  
[overlayOpacity](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.SplashScreen-overlayOpacity.html) | To increase the contrast between the background and logos, you apply an overlay color modifier. Use the overlay opacity to adjust the strength of this effect.  
[show](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.SplashScreen-show.html) | Set this property to true to make the Splash Screen appear when the application is launched. Set this property to false to disable the Splash Screen.  
[showUnityLogo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.SplashScreen-showUnityLogo.html) | Set this to true to show the Unity logo during the Splash Screen. Set it to false to disable the Unity logo.  
[unityLogoStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.SplashScreen-unityLogoStyle.html) | The style to use for the Unity logo during the Splash Screen.  
* * *
