* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ObjectChangeEvents.html

# ObjectChangeEvents
class in UnityEditor
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
Exposes events that allow you to track undoable changes to objects in the editor.
Any undoable change to any object loaded in the editor (both [GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) and assets such as [Material](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html) object) are recorded and exposed as a stream of events. See [ObjectChangeKind](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ObjectChangeKind.html) for more information as to which types of changes are recorded. Undoing and redoing changes also records events. The stream of events is flushed once per frame. User interactions in the editor may map to multiple events in the event stream. 
### Events
Event | Description  
---|---  
[changesPublished](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ObjectChangeEvents-changesPublished.html) | Event that is raised once per frame if any undoable changes have been recorded.  
### Delegates
Delegate | Description  
---|---  
[ObjectChangeEventsHandler](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ObjectChangeEvents.ObjectChangeEventsHandler.html) | The delegate used for the event publishing the object changes.  
* * *
