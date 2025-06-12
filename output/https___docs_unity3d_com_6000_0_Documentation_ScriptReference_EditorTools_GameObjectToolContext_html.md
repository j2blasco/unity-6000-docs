* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.GameObjectToolContext.html

# GameObjectToolContext
class in UnityEditor.EditorTools
/
Inherits from:[EditorTools.EditorToolContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.EditorToolContext.html)
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
This class represents the default context for manipulation tools. When [GameObjectToolContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.GameObjectToolContext.html) is active, manipulation tools affect the transform property of GameObjects in the [SceneView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView.html) [Selection](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection.html).
### Inherited Members
### Properties
Property | Description  
---|---  
[target](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.EditorToolContext-target.html) | The object being inspected.  
[targets](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.EditorToolContext-targets.html) | An array of the objects being inspected.  
[hideFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-hideFlags.html) | Should the object be hidden, saved with the Scene or modifiable by the user?  
[name](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-name.html) | The name of the object.  
### Public Methods
Method | Description  
---|---  
[GetAdditionalToolTypes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.EditorToolContext.GetAdditionalToolTypes.html) | Get an additional collection of tools to display in the same category as the built-in transform tools.  
[OnActivated](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.EditorToolContext.OnActivated.html) | Invoked after this EditorToolContext becomes the active tool context.  
[OnToolGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.EditorToolContext.OnToolGUI.html) | Implements any common functionality for the set of manipulation tools available for this context.  
[OnWillBeDeactivated](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.EditorToolContext.OnWillBeDeactivated.html) | Invoked before this EditorToolContext stops being the active tool context.  
[PopulateMenu](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.EditorToolContext.PopulateMenu.html) | Adds menu items to the Scene view context menu.  
[ResolveTool](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.EditorToolContext.ResolveTool.html) | Returns the matching EditorTool type for the specified Tool given the context.  
[GetInstanceID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.GetInstanceID.html) | Gets the instance ID of the object.  
[ToString](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.ToString.html) | Returns the name of the object.  
### Protected Methods
Method | Description  
---|---  
[GetEditorToolType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.EditorToolContext.GetEditorToolType.html) | Defines the EditorTool type for a given Tool.  
### Static Methods
Method | Description  
---|---  
[Destroy](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.Destroy.html) | Removes a GameObject, component or asset.  
[DestroyImmediate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.DestroyImmediate.html) | Destroys the object obj immediately. You are strongly recommended to use Destroy instead.  
[DontDestroyOnLoad](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.DontDestroyOnLoad.html) | Do not destroy the target Object when loading a new Scene.  
[FindAnyObjectByType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.FindAnyObjectByType.html) | Retrieves any active loaded object of Type type.  
[FindFirstObjectByType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.FindFirstObjectByType.html) | Retrieves the first active loaded object of Type type.  
[FindObjectsByType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.FindObjectsByType.html) | Retrieves a list of all loaded objects of Type type.  
[Instantiate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.Instantiate.html) | Clones the object original and returns the clone.  
[InstantiateAsync](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.InstantiateAsync.html) | Captures a snapshot of the original object (that must be related to some GameObject) and returns the AsyncInstantiateOperation.  
[CreateInstance](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.CreateInstance.html) | Creates an instance of a scriptable object.  
### Operators
Operator | Description  
---|---  
[bool](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-operator_Object.html) | Does the object exist?  
[operator !=](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-operator_ne.html) | Compares if two objects refer to a different object.  
[operator ==](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-operator_eq.html) | Compares two object references to see if they refer to the same object.  
### Messages
Message | Description  
---|---  
[Awake](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.Awake.html) | Called when an instance of ScriptableObject is created.  
[OnDestroy](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.OnDestroy.html) | This function is called when the scriptable object will be destroyed.  
[OnDisable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.OnDisable.html) | This function is called when the scriptable object goes out of scope.  
[OnEnable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.OnEnable.html) | This function is called when the object is loaded.  
[OnValidate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.OnValidate.html) | Editor-only function that Unity calls when the script is loaded or a value changes in the Inspector.  
[Reset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.Reset.html) | Reset to default values.  
* * *
