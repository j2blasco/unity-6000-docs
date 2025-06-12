* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.SplashScreen-logos.html

#  [PlayerSettings.SplashScreen](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.SplashScreen.html).logos
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
logos; 
### Description
The collection of logos that is shown during the splash screen. Logos are drawn in ascending order, starting from index 0, followed by 1, etc etc.
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
public class ExampleScript
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("SplashScreen[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.SplashScreen.html)/AssignLogos")]
    public static void AssignLogos()
    {
        var logos = new PlayerSettings.SplashScreenLogo[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.SplashScreenLogo.html)[2];  
  
        // Company logo
        Sprite[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite.html) companyLogo = (Sprite[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite.html))AssetDatabase.LoadAssetAtPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.LoadAssetAtPath.html)("Assets/SplashScreen[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.SplashScreen.html)/company logo.jpg", typeof(Sprite[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite.html)));
        logos[0] = PlayerSettings.SplashScreenLogo.Create[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.SplashScreenLogo.Create.html)(2.5f, companyLogo);  
  
        // Set the Unity logo to be drawn after the company logo.
        logos[1] = PlayerSettings.SplashScreenLogo.CreateWithUnityLogo[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.SplashScreenLogo.CreateWithUnityLogo.html)();  
  
        PlayerSettings.SplashScreen.logos[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.SplashScreen-logos.html) = logos;
    }
}

```

* * *
