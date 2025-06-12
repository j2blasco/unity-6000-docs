* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.GetAdditionalIl2CppArgs.html

#  [PlayerSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.html).GetAdditionalIl2CppArgs
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
## Declaration
public static string GetAdditionalIl2CppArgs(); 
### Returns
**string** Additional arguments passed to the IL2CPP compiler during the build process. 
### Description
Obtain the additional arguments passed to the IL2CPP compiler during the player build process.
Returns a string of the additional arguments set for an IL2CPP build. The Unity editor normally passes a number of command line arguments to IL2CPP as part of the build process. This method returns any additional arguments that have been provided via the SetAdditionalIl2CppArgs method.  
  
This method is only useful for advanced uses cases. For most projects, there is no need to add provide to IL2CPP with additional arguments.
* * *
