* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.SplashScreen.html

# SplashScreen
class in UnityEngine.Rendering
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
Provides an interface to the Unity splash screen.
### Static Properties
Property | Description  
---|---  
[isFinished](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.SplashScreen-isFinished.html) | Returns true once the splash screen has finished. This is once all logos have been shown for their specified duration.  
### Static Methods
Method | Description  
---|---  
[Begin](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.SplashScreen.Begin.html) | Initializes the splash screen so it is ready to begin drawing. Call this before you start calling SplashScreen.Draw. Internally this function resets the timer and prepares the logos for drawing.  
[Draw](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.SplashScreen.Draw.html) | Immediately draws the splash screen. Ensure you have called SplashScreen.Begin before you start calling this.  
[Stop](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.SplashScreen.Stop.html) | Stop the SplashScreen rendering.  
* * *
