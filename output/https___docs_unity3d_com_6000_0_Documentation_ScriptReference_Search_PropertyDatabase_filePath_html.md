* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.PropertyDatabase-filePath.html

#  [PropertyDatabase](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.PropertyDatabase.html).filePath
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
filePath; 
### Description
The file on which this [PropertyDatabase](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.PropertyDatabase.html) is opened.
Multiple [PropertyDatabase](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.PropertyDatabase.html)s can be opened on different files, but only a single [PropertyDatabase](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.PropertyDatabase.html) can be opened on a single file. You can do concurrent operations on a single instance of a [PropertyDatabase](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.PropertyDatabase.html), but for performance reasons you should use a view (see [PropertyDatabase.GetView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.PropertyDatabase.GetView.html) and [IPropertyDatabaseView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.IPropertyDatabaseView.html)).
* * *
