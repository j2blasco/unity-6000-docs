* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ObjectChangeEventStream.html

# ObjectChangeEventStream
struct in UnityEditor
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
Represents a stream of events that describes the changes applied to objects in memory over the course of a frame.
### Properties
Property | Description  
---|---  
[isCreated](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ObjectChangeEventStream-isCreated.html) | Indicates whether the ObjectChangeEventStream has an allocated memory buffer.  
[length](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ObjectChangeEventStream-length.html) | The number of events in the stream.  
### Public Methods
Method | Description  
---|---  
[Clone](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ObjectChangeEventStream.Clone.html) | Creates a copy of this stream with the specified allocator.  
[Dispose](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ObjectChangeEventStream.Dispose.html) | Releases the memory associated with this stream.  
[GetChangeAssetObjectPropertiesEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ObjectChangeEventStream.GetChangeAssetObjectPropertiesEvent.html) | Retrieves the event data at the given index as a ChangeAssetObjectPropertiesEventArgs. Throws an exception if the event type requested does not match the event stored in the stream.  
[GetChangeChildrenOrderEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ObjectChangeEventStream.GetChangeChildrenOrderEvent.html) | Retrieves the event data at the given index as a ChangeChildrenOrderEventArgs. Throws an exception if the event type requested does not match the event stored in the stream.  
[GetChangeGameObjectOrComponentPropertiesEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ObjectChangeEventStream.GetChangeGameObjectOrComponentPropertiesEvent.html) | Retrieves the event data at the given index as a ChangeAssetObjectPropertiesEventArgs. Throws an exception if the event type requested does not match the event stored in the stream.  
[GetChangeGameObjectParentEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ObjectChangeEventStream.GetChangeGameObjectParentEvent.html) | Retrieves the event data at the given index as a ChangeGameObjectParentEventArgs. Throws an exception if the event type requested does not match the event stored in the stream.  
[GetChangeGameObjectStructureEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ObjectChangeEventStream.GetChangeGameObjectStructureEvent.html) | Retrieves the event data at the given index as a ChangeGameObjectStructureEventArgs. Throws an exception if the event type requested does not match the event stored in the stream.  
[GetChangeGameObjectStructureHierarchyEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ObjectChangeEventStream.GetChangeGameObjectStructureHierarchyEvent.html) | Retrieves the event data at the given index as a ChangeGameObjectStructureHierarchyEventArgs. Throws an exception if the event type requested does not match the event stored in the stream.  
[GetChangeRootOrderEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ObjectChangeEventStream.GetChangeRootOrderEvent.html) | Retrieves the event data at the given index as a ChangeRootOrderEventArgs. Throws an exception if the event type requested does not match the event stored in the stream.  
[GetChangeSceneEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ObjectChangeEventStream.GetChangeSceneEvent.html) | Retrieves the event data at the given index as a ChangeSceneEventArgs. Throws an exception if the event type requested does not match the event stored in the stream.  
[GetCreateAssetObjectEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ObjectChangeEventStream.GetCreateAssetObjectEvent.html) | Retrieves the event data at the given index as a CreateAssetObjectEventArgs. Throws an exception if the event type requested does not match the event stored in the stream.  
[GetCreateGameObjectHierarchyEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ObjectChangeEventStream.GetCreateGameObjectHierarchyEvent.html) | Retrieves the event data at the given index as a CreateGameObjectHierarchyEventArgs. Throws an exception if the event type requested does not match the event stored in the stream.  
[GetDestroyAssetObjectEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ObjectChangeEventStream.GetDestroyAssetObjectEvent.html) | Retrieves the event data at the given index as a DestroyAssetObjectEventArgs. Throws an exception if the event type requested does not match the event stored in the stream.  
[GetDestroyGameObjectHierarchyEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ObjectChangeEventStream.GetDestroyGameObjectHierarchyEvent.html) | Retrieves the event data at the given index as a DestroyGameObjectHierarchyEventArgs. Throws an exception if the event type requested does not match the event stored in the stream.  
[GetEventType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ObjectChangeEventStream.GetEventType.html) | Returns the type of the event at the specified index.  
[GetUpdatePrefabInstancesEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ObjectChangeEventStream.GetUpdatePrefabInstancesEvent.html) | Retrieves the event data at the given index as a UpdatePrefabInstancesEventArgs. Throws an exception if the event type requested does not match the event stored in the stream.  
* * *
