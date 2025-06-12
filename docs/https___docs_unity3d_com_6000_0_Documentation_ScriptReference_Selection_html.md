* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection.html

# Selection
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
Access to the selection in the editor.
### Static Properties
Property | Description  
---|---  
[activeContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection-activeContext.html) | Returns the current context object, as was set via SetActiveObjectWithContext.  
[activeGameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection-activeGameObject.html) | Returns the active game object. (The one shown in the inspector).  
[activeInstanceID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection-activeInstanceID.html) | Returns the instanceID of the actual object selection. Includes Prefabs, non-modifiable objects.  
[activeObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection-activeObject.html) | Returns the actual object selection. Includes Prefabs, non-modifiable objects.  
[activeTransform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection-activeTransform.html) | Returns the active transform. (The one shown in the inspector).  
[assetGUIDs](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection-assetGUIDs.html) | Returns the guids of the selected assets.  
[count](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection-count.html) | Returns the number of objects in the Selection.  
[gameObjects](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection-gameObjects.html) | Returns the actual game object selection. Includes Prefabs, non-modifiable objects.  
[instanceIDs](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection-instanceIDs.html) | The actual unfiltered selection from the Scene returned as instance ids instead of objects.  
[objects](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection-objects.html) | The actual unfiltered selection from the Scene.  
[selectionChanged](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection-selectionChanged.html) | Delegate callback triggered when currently active/selected item has changed.  
[transforms](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection-transforms.html) | Returns the top level selection, excluding Prefabs.  
### Static Methods
Method | Description  
---|---  
[Contains](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection.Contains.html) | Returns whether an object is contained in the current selection.  
[GetFiltered](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection.GetFiltered.html) | Returns the current selection filtered by type and mode.  
[GetTransforms](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection.GetTransforms.html) | Allows for fine grained control of the selection type using the SelectionMode bitmask.  
[SetActiveObjectWithContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection.SetActiveObjectWithContext.html) | Selects an object with a context.  
* * *
