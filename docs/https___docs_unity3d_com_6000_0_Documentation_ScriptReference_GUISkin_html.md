* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUISkin.html

# GUISkin
class in UnityEngine
/
Inherits from:[ScriptableObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.html)
/
Implemented in:[UnityEngine.IMGUIModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.IMGUIModule.html)
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GUISkin.html "Go to GUISkin Component in the Manual")
### Description
Defines how GUI looks and behaves.
GUISkin contains GUI settings and a collection of [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) objects that together specify GUI skin.  
  
Active GUI skin is get and set through [GUI.skin](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI-skin.html).
### Properties
Property | Description  
---|---  
[box](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUISkin-box.html) | Style used by default for GUI.Box controls.  
[button](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUISkin-button.html) | Style used by default for GUI.Button controls.  
[customStyles](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUISkin-customStyles.html) | Array of GUI styles for specific needs.  
[font](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUISkin-font.html) | The default font to use for all styles.  
[horizontalScrollbar](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUISkin-horizontalScrollbar.html) | Style used by default for the background part of GUI.HorizontalScrollbar controls.  
[horizontalScrollbarLeftButton](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUISkin-horizontalScrollbarLeftButton.html) | Style used by default for the left button on GUI.HorizontalScrollbar controls.  
[horizontalScrollbarRightButton](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUISkin-horizontalScrollbarRightButton.html) | Style used by default for the right button on GUI.HorizontalScrollbar controls.  
[horizontalScrollbarThumb](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUISkin-horizontalScrollbarThumb.html) | Style used by default for the thumb that is dragged in GUI.HorizontalScrollbar controls.  
[horizontalSlider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUISkin-horizontalSlider.html) | Style used by default for the background part of GUI.HorizontalSlider controls.  
[horizontalSliderThumb](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUISkin-horizontalSliderThumb.html) | Style used by default for the thumb that is dragged in GUI.HorizontalSlider controls.  
[label](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUISkin-label.html) | Style used by default for GUI.Label controls.  
[scrollView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUISkin-scrollView.html) | Style used by default for the background of ScrollView controls (see GUI.BeginScrollView).  
[settings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUISkin-settings.html) | Generic settings for how controls should behave with this skin.  
[textArea](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUISkin-textArea.html) | Style used by default for GUI.TextArea controls.  
[textField](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUISkin-textField.html) | Style used by default for GUI.TextField controls.  
[toggle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUISkin-toggle.html) | Style used by default for GUI.Toggle controls.  
[verticalScrollbar](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUISkin-verticalScrollbar.html) | Style used by default for the background part of GUI.VerticalScrollbar controls.  
[verticalScrollbarDownButton](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUISkin-verticalScrollbarDownButton.html) | Style used by default for the down button on GUI.VerticalScrollbar controls.  
[verticalScrollbarThumb](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUISkin-verticalScrollbarThumb.html) | Style used by default for the thumb that is dragged in GUI.VerticalScrollbar controls.  
[verticalScrollbarUpButton](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUISkin-verticalScrollbarUpButton.html) | Style used by default for the up button on GUI.VerticalScrollbar controls.  
[verticalSlider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUISkin-verticalSlider.html) | Style used by default for the background part of GUI.VerticalSlider controls.  
[verticalSliderThumb](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUISkin-verticalSliderThumb.html) | Style used by default for the thumb that is dragged in GUI.VerticalSlider controls.  
[window](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUISkin-window.html) | Style used by default for Window controls (Additional resources: GUI.Window).  
### Public Methods
Method | Description  
---|---  
[FindStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUISkin.FindStyle.html) | Try to search for a GUIStyle. This functions returns NULL and does not give an error.  
[GetStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUISkin.GetStyle.html) | Get a named GUIStyle.  
### Inherited Members
### Properties
Property | Description  
---|---  
[hideFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-hideFlags.html) | Should the object be hidden, saved with the Scene or modifiable by the user?  
[name](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-name.html) | The name of the object.  
### Public Methods
Method | Description  
---|---  
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
