* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WSA.Launcher.LaunchFile.html

#  [Launcher](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WSA.Launcher.html).LaunchFile
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
## Declaration
public static void LaunchFile([WSA.Folder](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WSA.Folder.html) folder, string relativeFilePath, bool showWarning); 
### Parameters
Parameter | Description  
---|---  
folder | Folder type where the file is located.  
relativeFilePath | Relative file path inside the specified folder.  
showWarning | Shows user a warning that application will be switched.  
### Description
Launches the default app associated with specified file.
Note: if the application associated with file is the same as the one performing the launch, Windows won't open a new application, instead it will simply invoke OnActivated event in App.xaml.[cs/cpp] file.
* * *
