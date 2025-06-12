* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.GameObjectRecorder.html

# GameObjectRecorder
class in UnityEditor.Animations
/
Inherits from:[Object](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.html)
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
Records the changing properties of a [GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) as the Scene runs and saves the information into an [AnimationClip](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationClip.html).
This class binds [GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) properties, records their values as they change in the running Scene, and saves the result in an [AnimationClip](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationClip.html). The recorded GameObject is called [root](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.GameObjectRecorder-root.html) in the class, and you can also bind the properties of any child of [root](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.GameObjectRecorder-root.html).  
  
See the following code example on how this class can be implemented and to set what gets recorded.
```
using UnityEngine;
using UnityEditor.Animations;  
  
public class RecordTransformHierarchy : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public AnimationClip[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationClip.html) clip;  
  
    private GameObjectRecorder[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.GameObjectRecorder.html) m_Recorder;  
  
    void Start()
    {
        // Create recorder and record the script GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html).
        m_Recorder = new GameObjectRecorder[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.GameObjectRecorder.html)(gameObject);  
  
        // Bind all the Transforms on the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) and all its children.
        m_Recorder.BindComponentsOfType<Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html)>(gameObject, true);
    }  
  
    void LateUpdate()
    {
        if (clip == null)
            return;  
  
        // Take a snapshot and record all the bindings values for this frame.
        m_Recorder.TakeSnapshot(Time.deltaTime[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-deltaTime.html));
    }  
  
    void OnDisable()
    {
        if (clip == null)
            return;  
  
        if (m_Recorder.isRecording)
        {
            // Save the recorded session to the clip.
            m_Recorder.SaveToClip(clip);
        }
    }
}

```

### Properties
Property | Description  
---|---  
[currentTime](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.GameObjectRecorder-currentTime.html) | Returns the current time of the recording. (Read Only)  
[isRecording](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.GameObjectRecorder-isRecording.html) | Returns true when the recorder is recording. (Read Only)  
[root](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.GameObjectRecorder-root.html) | The GameObject root of the animated hierarchy. (Read Only)  
### Constructors
Constructor | Description  
---|---  
[GameObjectRecorder](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.GameObjectRecorder-ctor.html) | Create a new GameObjectRecorder.  
### Public Methods
Method | Description  
---|---  
[Bind](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.GameObjectRecorder.Bind.html) | Binds a GameObject's property as defined by EditorCurveBinding.  
[BindAll](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.GameObjectRecorder.BindAll.html) | Adds bindings for all of target's properties, and also for all the target's children if recursive is true.  
[BindComponent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.GameObjectRecorder.BindComponent.html) | Adds bindings for all the properties of component.  
[BindComponentsOfType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.GameObjectRecorder.BindComponentsOfType.html) | Adds bindings for all the properties of the first component of type T found in target, and also for all the target's children if recursive is true.  
[GetBindings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.GameObjectRecorder.GetBindings.html) | Returns an array of all the bindings added to the recorder.  
[ResetRecording](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.GameObjectRecorder.ResetRecording.html) | Reset the recording.  
[SaveToClip](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.GameObjectRecorder.SaveToClip.html) | Saves recorded animation to a destination clip.  
[TakeSnapshot](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.GameObjectRecorder.TakeSnapshot.html) | Forwards the animation by dt seconds, then record the values of the added bindings.  
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
### Operators
Operator | Description  
---|---  
[bool](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-operator_Object.html) | Does the object exist?  
[operator !=](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-operator_ne.html) | Compares if two objects refer to a different object.  
[operator ==](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-operator_eq.html) | Compares two object references to see if they refer to the same object.  
* * *
