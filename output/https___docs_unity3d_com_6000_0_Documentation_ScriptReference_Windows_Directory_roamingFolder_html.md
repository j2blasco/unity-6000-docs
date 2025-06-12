* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.Directory-roamingFolder.html

#  [Directory](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.Directory.html).roamingFolder
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
roamingFolder; 
### Description
Returns a path to roaming folder.
On Windows Store Apps, it will be <main drive>:\Users\<user name>\AppData\Local\Packages\<package id>\RoamingState, directory is writeable, so you can create, read and write files to it. In Editor, it will be <your project path>\RoamingState.  
  
**Note:** This property is only available on the Universal Windows Platform.
* * *
