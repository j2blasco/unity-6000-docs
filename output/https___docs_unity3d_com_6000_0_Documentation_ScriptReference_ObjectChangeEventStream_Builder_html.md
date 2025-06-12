* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ObjectChangeEventStream.Builder.html

# Builder
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
Provides a way to construct an instance of [ObjectChangeEventStream](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ObjectChangeEventStream.html).
### Properties
Property | Description  
---|---  
[eventCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ObjectChangeEventStream.Builder-eventCount.html) | The number of events that have been recorded in this instance so far.  
### Constructors
Constructor | Description  
---|---  
[ObjectChangeEventStream.Builder](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ObjectChangeEventStream.Builder-ctor.html) | Constructs a new instance.  
### Public Methods
Method | Description  
---|---  
[Dispose](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ObjectChangeEventStream.Builder.Dispose.html) | Releases the memory associated with this instance.  
[PushChangeAssetObjectPropertiesEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ObjectChangeEventStream.Builder.PushChangeAssetObjectPropertiesEvent.html) | Adds an ChangeAssetObjectPropertiesEventArgs to the end of the stream.  
[PushChangeGameObjectOrComponentPropertiesEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ObjectChangeEventStream.Builder.PushChangeGameObjectOrComponentPropertiesEvent.html) | Adds an ChangeGameObjectOrComponentPropertiesEventArgs to the end of the stream.  
[PushChangeGameObjectParentEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ObjectChangeEventStream.Builder.PushChangeGameObjectParentEvent.html) | Adds an ChangeGameObjectParentEventArgs to the end of the stream.  
[PushChangeGameObjectStructureEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ObjectChangeEventStream.Builder.PushChangeGameObjectStructureEvent.html) | Adds an ChangeGameObjectStructureEventArgs to the end of the stream.  
[PushChangeGameObjectStructureHierarchyEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ObjectChangeEventStream.Builder.PushChangeGameObjectStructureHierarchyEvent.html) | Adds an ChangeGameObjectStructureHierarchyEventArgs to the end of the stream.  
[PushChangeSceneEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ObjectChangeEventStream.Builder.PushChangeSceneEvent.html) | Adds an ChangeSceneEventArgs to the end of the stream.  
[PushCreateAssetObjectEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ObjectChangeEventStream.Builder.PushCreateAssetObjectEvent.html) | Adds an CreateAssetObjectEventArgs to the end of the stream.  
[PushCreateGameObjectHierarchyEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ObjectChangeEventStream.Builder.PushCreateGameObjectHierarchyEvent.html) | Adds an CreateGameObjectHierarchyEventArgs to the end of the stream.  
[PushDestroyAssetObjectEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ObjectChangeEventStream.Builder.PushDestroyAssetObjectEvent.html) | Adds an DestroyAssetObjectEventArgs to the end of the stream.  
[PushDestroyGameObjectHierarchyEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ObjectChangeEventStream.Builder.PushDestroyGameObjectHierarchyEvent.html) | Adds an DestroyGameObjectHierarchyEventArgs to the end of the stream.  
[PushUpdatePrefabInstancesEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ObjectChangeEventStream.Builder.PushUpdatePrefabInstancesEvent.html) | Adds an UpdatePrefabInstancesEventArgs to the end of the stream.  
[ToStream](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ObjectChangeEventStream.Builder.ToStream.html) | Copies the data collected in this instance into a new ObjectChangeEventStream instance.  
* * *
