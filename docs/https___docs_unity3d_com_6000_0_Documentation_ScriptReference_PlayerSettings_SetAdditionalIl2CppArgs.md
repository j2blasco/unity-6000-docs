* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.SetAdditionalIl2CppArgs.html

#  [PlayerSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.html).SetAdditionalIl2CppArgs
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
public static void SetAdditionalIl2CppArgs(string additionalArgs); 
### Parameters
Parameter | Description  
---|---  
additionalArgs | The additional arguments passed to the IL2CPP compiler during the build process.  
### Description
Set additional arguments passed to the IL2CPP compiler during the build process.
Sets a string of the additional arguments set for an IL2CPP build. The Unity editor normally passes a number of command line arguments to IL2CPP as part of the build process. This method allows the user to add additional arguments. Arguments should be providied as a single string, with spaces separating each argument. Use the GetAdditionalIl2CppArgs method to determine the argument string previously provided to this method. Pass an empty string to this method to remove any previously provided additional arguments.  
  
This method is only useful for advanced uses cases. For most projects, there is no need to add provide to IL2CPP with additional arguments.
* * *
