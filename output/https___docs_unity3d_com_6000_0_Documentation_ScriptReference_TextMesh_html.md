* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextMesh.html

# TextMesh
class in UnityEngine
/
Inherits from:[Component](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.html)
/
Implemented in:[UnityEngine.TextRenderingModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.TextRenderingModule.html)
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextMesh.html "Go to TextMesh Component in the Manual")
### Description
A script interface for the [text mesh component](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextMesh.html).
Additional resources: [text mesh component](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextMesh.html).
### Properties
Property | Description  
---|---  
[alignment](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextMesh-alignment.html) | How lines of text are aligned (Left, Right, Center).  
[anchor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextMesh-anchor.html) | Which point of the text shares the position of the Transform.  
[characterSize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextMesh-characterSize.html) | The size of each character (This scales the whole text).  
[color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextMesh-color.html) | The color used to render the text.  
[font](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextMesh-font.html) | The Font used.  
[fontSize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextMesh-fontSize.html) | The font size to use (for dynamic fonts).  
[fontStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextMesh-fontStyle.html) | The font style to use (for dynamic fonts).  
[lineSpacing](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextMesh-lineSpacing.html) | How much space will be in-between lines of text.  
[offsetZ](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextMesh-offsetZ.html) | How far should the text be offset from the transform.position.z when drawing.  
[richText](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextMesh-richText.html) | Enable HTML-style tags for Text Formatting Markup.  
[tabSize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextMesh-tabSize.html) | How much space will be inserted for a tab '\t' character. This is a multiplum of the 'spacebar' character offset.  
[text](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextMesh-text.html) | The text that is displayed.  
### Inherited Members
### Properties
Property | Description  
---|---  
[gameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component-gameObject.html) | The game object this component is attached to. A component is always attached to a game object.  
[tag](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component-tag.html) | The tag of this game object.  
[transform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component-transform.html) | The Transform attached to this GameObject.  
[hideFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-hideFlags.html) | Should the object be hidden, saved with the Scene or modifiable by the user?  
[name](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-name.html) | The name of the object.  
### Public Methods
Method | Description  
---|---  
[BroadcastMessage](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.BroadcastMessage.html) | Calls the method named methodName on every MonoBehaviour in this game object or any of its children.  
[CompareTag](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.CompareTag.html) | Checks the GameObject's tag against the defined tag.  
[GetComponent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.GetComponent.html) | Gets a reference to a component of type T on the same GameObject as the component specified.  
[GetComponentInChildren](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.GetComponentInChildren.html) | Gets a reference to a component of type T on the same GameObject as the component specified, or any child of the GameObject.  
[GetComponentIndex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.GetComponentIndex.html) | Gets the index of the component on its parent GameObject.  
[GetComponentInParent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.GetComponentInParent.html) | Gets a reference to a component of type T on the same GameObject as the component specified, or any parent of the GameObject.  
[GetComponents](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.GetComponents.html) | Gets references to all components of type T on the same GameObject as the component specified.  
[GetComponentsInChildren](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.GetComponentsInChildren.html) | Gets references to all components of type T on the same GameObject as the component specified, and any child of the GameObject.  
[GetComponentsInParent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.GetComponentsInParent.html) | Gets references to all components of type T on the same GameObject as the component specified, and any parent of the GameObject.  
[SendMessage](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.SendMessage.html) | Calls the method named methodName on every MonoBehaviour in this game object.  
[SendMessageUpwards](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.SendMessageUpwards.html) | Calls the method named methodName on every MonoBehaviour in this game object and on every ancestor of the behaviour.  
[TryGetComponent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.TryGetComponent.html) | Gets the component of the specified type, if it exists.  
[GetInstanceID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.GetInstanceID.html) | Gets the instance ID of the object.  
[ToString](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.ToString.html) | Returns the name of the object.  
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
### Operators
Operator | Description  
---|---  
[bool](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-operator_Object.html) | Does the object exist?  
[operator !=](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-operator_ne.html) | Compares if two objects refer to a different object.  
[operator ==](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-operator_eq.html) | Compares two object references to see if they refer to the same object.  
* * *
