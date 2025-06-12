* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application.GetStreamProgressForLevel.html

**Method group is Obsolete**   

#  [Application](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application.html).GetStreamProgressForLevel
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
**Obsolete** Streaming was a Unity Web Player feature, and is removed. This function is deprecated and always returns 1.0 for valid level indices.
## Declaration
public static float GetStreamProgressForLevel(int levelIndex); 
### Description
How far has the download progressed? [0...1].
In the webplayer this returns the progress of this level.  
  
Additional resources: [CanStreamedLevelBeLoaded](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application.CanStreamedLevelBeLoaded.html) function.  
  
Webplayer support is not part of 5.4.0 and later.
* * *
**Obsolete** Streaming was a Unity Web Player feature, and is removed. This function is deprecated and always returns 1.0.
## Declaration
public static float GetStreamProgressForLevel(string levelName); 
### Description
How far has the download progressed? [0...1].
In the webplayer this returns the progress of this level.  
  
Additional resources: [CanStreamedLevelBeLoaded](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application.CanStreamedLevelBeLoaded.html) function.  
  
Webplayer support is not part of 5.4.0 and later.
* * *
