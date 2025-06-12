* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchMonitor.html

# SearchMonitor
class in UnityEditor.Search
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
The search monitor is responsible to track any changes that occurs in Unity in order to update search indexes or other search data structure at runtime.
### Static Properties
Property | Description  
---|---  
[pending](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchMonitor-pending.html) | Indicates if the changes still need to be processed by the search backend.  
### Static Methods
Method | Description  
---|---  
[GetDiff](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchMonitor.GetDiff.html) | Returns the assets that changed since a point in time.  
[GetView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchMonitor.GetView.html) | Returns a SearchMonitorView to access Search's main PropertyDatabases.  
[RaiseContentRefreshed](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchMonitor.RaiseContentRefreshed.html) | Mark content to be refreshed.  
[Reset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchMonitor.Reset.html) | Reset the search property database content, invalidating all caches.  
### Events
Event | Description  
---|---  
[contentRefreshed](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchMonitor-contentRefreshed.html) | Event invoked when some content has changed.  
[documentsInvalidated](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchMonitor-documentsInvalidated.html) | Event raised when documents get invalidated.  
[objectChanged](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchMonitor-objectChanged.html) | Event raised when an UnityEngine.Object changed.  
[sceneChanged](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchMonitor-sceneChanged.html) | Event raised when the current loaded scene changes that might affect search results.  
* * *
