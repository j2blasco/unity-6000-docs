* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.ImportPackageCallback.html

#  [AssetDatabase](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.html).ImportPackageCallback
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
public delegate void ImportPackageCallback(string packageName); 
### Description
Delegate to be called from [AssetDatabase.ImportPackage](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.ImportPackage.html) callbacks. **packageName** is the name of the package that raised the callback.
ImportPackageCallback is used by [AssetDatabase.importPackageStarted](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase-importPackageStarted.html), [AssetDatabase.importPackageCompleted](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase-importPackageCompleted.html), and [AssetDatabase.importPackageCancelled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase-importPackageCancelled.html).
* * *
