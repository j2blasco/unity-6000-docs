* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Content.ContentNamespace.html

# ContentNamespace
struct in Unity.Content
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
Provides functionality for grouping loaded Archive files into separate namespaces.
You can use the [ContentNamespace.Default](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Content.ContentNamespace.Default.html) namespace, or create your own custom namespace with [ContentNamespace.GetOrCreateNamespace](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Content.ContentNamespace.GetOrCreateNamespace.html).  
  
**Note:** A ContentNamespace name must contain only alphanumeric characters and can't be longer than 16 characters.  
  
Additional resources: [ArchiveFileInterface.MountAsync](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.IO.Archive.ArchiveFileInterface.MountAsync.html). 
### Static Properties
Property | Description  
---|---  
[Default](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Content.ContentNamespace.Default.html) | Default ContentNamespace object.  
### Properties
Property | Description  
---|---  
[IsValid](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Content.ContentNamespace.IsValid.html) | Indicates whether the ContentNamespace still exists.  
### Public Methods
Method | Description  
---|---  
[Delete](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Content.ContentNamespace.Delete.html) | Destroys the specified ContentNamespace object.  
[GetName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Content.ContentNamespace.GetName.html) | Retrieves the name of the ContentNamespace.  
### Static Methods
Method | Description  
---|---  
[GetAll](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Content.ContentNamespace.GetAll.html) | Retrieves all existing ContentNamespace objects.  
[GetOrCreateNamespace](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Content.ContentNamespace.GetOrCreateNamespace.html) | Retrieves or creates the ContentNamespace if it doesn't exist.  
* * *
