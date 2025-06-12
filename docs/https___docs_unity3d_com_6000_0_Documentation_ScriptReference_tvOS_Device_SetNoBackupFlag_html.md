* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/tvOS.Device.SetNoBackupFlag.html

#  [Device](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/tvOS.Device.html).SetNoBackupFlag
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
public static void SetNoBackupFlag(string path); 
### Description
Set file flag to be excluded from iCloud/iTunes backup.
As a side-effect, if it was located in Caches folder, it won't be deleted by OS.
* * *
