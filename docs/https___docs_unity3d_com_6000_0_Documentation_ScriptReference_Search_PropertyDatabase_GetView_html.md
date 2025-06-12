* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.PropertyDatabase.GetView.html

#  [PropertyDatabase](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.PropertyDatabase.html).GetView
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
public [Search.IPropertyDatabaseView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.IPropertyDatabaseView.html) GetView(bool delayedSync); 
### Parameters
Parameter | Description  
---|---  
delayedSync | Boolean indicating if the sync between views should only happen when the view is disposed, or for every operation.  
### Returns
**IPropertyDatabaseView** The [PropertyDatabase](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.PropertyDatabase.html) view. 
### Description
Opens a view on the [PropertyDatabase](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.PropertyDatabase.html).
The view handles all the internal file operations and concurrent accesses. All operations on the [PropertyDatabase](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.PropertyDatabase.html) create a view, so for performance reasons you should get a view with [PropertyDatabase.GetView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.PropertyDatabase.GetView.html) and do all your operations with it.  
  
Additional resources: [IPropertyDatabaseView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.IPropertyDatabaseView.html)
* * *
