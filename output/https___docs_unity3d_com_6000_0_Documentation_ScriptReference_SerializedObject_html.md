* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject.html

# SerializedObject
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
SerializedObject and [SerializedProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html) are classes for editing serialized fields on [Unity objects](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.html) in a completely generic way. These classes automatically handle dirtying individual serialized fields so they will be processed by the [Undo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Undo.html) system and styled correctly for Prefab overrides when drawn in the Inspector.
In many cases, you may create tools to modify objects in your project. For instance, the following script example creates a menu item that resets the local position of all GameObjects currently selected. Put it in a file called Example1.cs in a folder called Editor:
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;  
  
static class Example1
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Edit/Reset Selected Objects Position[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Position.html) (No Undo[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Undo.html))")]
    static void ResetPosition()
    {
        // this action will not be undoable
        foreach (var go in Selection.gameObjects[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection-gameObjects.html))
            go.transform.localPosition = Vector3.zero[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-zero.html);
    }
}

```

Although you can edit objects via their API points in this way, you would also have to use other editor APIs to specify which components have been dirtied so that this action would be undoable and would be detected as a change the next time the Scene is saved, and so on. In contrast, using SerializedObject handles this process automatically. The following script example has the same effect as the previous one, but is also undoable and is tracked as a change in the Scene. Put it in a file called Example2.cs in a folder called Editor:
```
using System.Linq;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;  
  
static class Example2
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Edit/Reset Selected Objects Position[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Position.html)")]
    static void ResetPosition()
    {
        var transforms = Selection.gameObjects.Select(go => go.transform).ToArray();
        var so = new SerializedObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject.html)(transforms);
        // you can Shift+Right Click on property names in the Inspector to see their paths
        so.FindProperty("m_LocalPosition").vector3Value = Vector3.zero[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-zero.html);
        so.ApplyModifiedProperties();
    }
}

```

SerializedObject opens a data stream to one or more target [Unity objects](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.html) at a time, which allows you to simultaneously edit serialized data that the objects share in common. For example, if you have several [Behaviours](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Behaviour.html) of different types in the data stream, the only property they have in common may be 'm_Enabled'.  
  
When you first create a SerializedObject instance it is up-to-date. Any changes that you make to a [SerializedProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html) accessed within this data stream must ultimately be flushed via the [SerializedObject.ApplyModifiedProperties](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject.ApplyModifiedProperties.html) method. If you keep a reference to a SerializedObject instance for more than one frame, you must make sure to manually call its [SerializedObject.Update](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject.Update.html) method before you read any data from it, as one or more target objects may have been modified elsewhere, such as from a separate SerializedObject stream. Respectively, note that two different SerializedObject streams with the same target objects are independent from one another and you must manually synchronize them in this fashion if one or more of them is maintained over the course of several frames.  
  
One of the most common uses of the SerializedObject and [SerializedProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html) classes is when creating custom [Editors](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html), where using SerializedObject is the recommended approach as opposed to modifying inspected target objects directly.  
  
The following example script defines a component that animates an object’s local position using a sine function. Put it in a script called SineAnimation.cs:
```
using UnityEngine;  
  
public class SineAnimation : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) axis { get { return m_Axis; } set { m_Axis = value; } }
    [SerializeField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializeField.html)]
    private Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) m_Axis = Vector3.up[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-up.html);  
  
    public float period { get { return m_Period; } set { m_Period = value; } }
    [SerializeField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializeField.html)]
    private float m_Period = 1f / Mathf.PI[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.PI.html);  
  
    public float amplitude { get { return m_Amplitude; } set { m_Amplitude = value; } }
    [SerializeField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializeField.html)]
    private float m_Amplitude = 1f;  
  
    public float phaseShift { get { return m_PhaseShift; } set { m_PhaseShift = Mathf.Clamp01[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.Clamp01.html)(value); } }
    [SerializeField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializeField.html), Range(0f, 1f)]
    private float m_PhaseShift;  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        transform.localPosition = m_Axis * m_Amplitude * Mathf.Sin[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.Sin.html)((Time.time[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-time.html) + m_PhaseShift) / m_Period);
    }  
  
    void OnValidate()
    {
        m_PhaseShift = Mathf.Clamp01[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.Clamp01.html)(m_PhaseShift);
    }
}

```

The following example script defines a custom [Editor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html) for SineAnimation that adds a button after the default controls to randomize the sine function parameters. Put it in a file called SineAnimationEditor.cs in a folder called Editor:
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;  
  
[CustomEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CustomEditor.html)(typeof(SineAnimation)), CanEditMultipleObjects[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CanEditMultipleObjects.html)]
public class SineAnimationEditor : Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html)
{
    public override void OnInspectorGUI()
    {
        base.OnInspectorGUI();
        if (GUILayout.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Button.html)("Randomize Sine Function", EditorStyles.miniButton[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorStyles-miniButton.html)))
        {
            serializedObject.FindProperty("m_Period").floatValue = Random.Range[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Random.Range.html)(0f, 10f);
            serializedObject.FindProperty("m_Amplitude").floatValue = Random.Range[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Random.Range.html)(0f, 10f);
            serializedObject.FindProperty("m_PhaseShift").floatValue = Random.Range[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Random.Range.html)(0f, 1f);
            serializedObject.ApplyModifiedProperties();
        }
    }
}

```

The [Editor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html) class has a [serializedObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor-serializedObject.html) property that provides a stream to all of the inspected targets (SineAnimation components in this case), which makes it easy to support editing multiple objects at the same time. Because this SerializedObject instance persists for the lifetime of the [Editor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html) instance, the base implementation of OnInspectorGUI handles calling Update before drawing any controls, as well as calling ApplyModifiedProperties after any user interaction. As such, modifications made when pressing the button added to this inspector must all be flushed via ApplyModifiedProperties before the method exits, or they will be lost the next time the base implementation of [Editor.OnInspectorGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.OnInspectorGUI.html) calls the [SerializedObject.Update](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject.Update.html) method on the [serializedObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor-serializedObject.html) instance.  
  
Note that flushing data to a Unity object via [SerializedObject.ApplyModifiedProperties](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject.ApplyModifiedProperties.html) will not respect any data validation logic you may have in property setters associated with the serialized fields. In this example, the value of the 'm_PhaseShift' field is clamped between 0 and 1, both in the phaseShift property setter and in the UI (via the RangeAttribute). Because users can access 'm_PhaseShift' via [SerializedProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html) (as well as by editing the asset on disk) and not only via the 'phaseShift' API or the UI, it is necessary to also clamp it to the valid range in the [MonoBehaviour.OnValidate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.OnValidate.html) callback, which will sanitize the data when the [Unity object](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.html) is loaded.  
  
Also note that although SerializedObject is designed to work with multiple targets, the value getter properties on the SerializedProperty class (e.g., [floatValue](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty-floatValue.html), [vector3Value](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty-vector3Value.html)) are not multi-select friendly. As such, assigning a value to them will affect all targets, but reading a value from them only returns the value associated with the first target in the list.  
  
Additional resources: [SerializedProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html), [SerializeField](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializeField.html), [Editor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html), [MonoBehaviour.OnValidate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.OnValidate.html), [hasMultipleDifferentValues](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty-hasMultipleDifferentValues.html).
### Properties
Property | Description  
---|---  
[context](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject-context.html) | The context used to store and resolve ExposedReference types. This is set by the SerializedObject constructor.  
[forceChildVisibility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject-forceChildVisibility.html) | Controls the visibility of the child hidden fields.  
[hasModifiedProperties](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject-hasModifiedProperties.html) | Is true when the SerializedObject has a modified property that has not been applied.  
[isEditingMultipleObjects](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject-isEditingMultipleObjects.html) | Does the serialized object represents multiple objects due to multi-object editing? (Read Only)  
[maxArraySizeForMultiEditing](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject-maxArraySizeForMultiEditing.html) | Defines the maximum size beyond which arrays cannot be edited when multiple objects are selected.  
[targetObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject-targetObject.html) | The inspected object (Read Only).  
[targetObjects](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject-targetObjects.html) | The inspected objects (Read Only).  
### Constructors
Constructor | Description  
---|---  
[SerializedObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject-ctor.html) | Create SerializedObject for inspected object.  
### Public Methods
Method | Description  
---|---  
[ApplyModifiedProperties](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject.ApplyModifiedProperties.html) | Apply property modifications.  
[ApplyModifiedPropertiesWithoutUndo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject.ApplyModifiedPropertiesWithoutUndo.html) | Applies property modifications without registering an undo operation.  
[CopyFromSerializedProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject.CopyFromSerializedProperty.html) | Copies a value from a SerializedProperty to the corresponding serialized property on the serialized object.  
[CopyFromSerializedPropertyIfDifferent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject.CopyFromSerializedPropertyIfDifferent.html) | Copies a changed value from a SerializedProperty to the corresponding serialized property on the serialized object.  
[FindProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject.FindProperty.html) | Find serialized property by name.  
[GetIterator](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject.GetIterator.html) | Get the first serialized property.  
[SetIsDifferentCacheDirty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject.SetIsDifferentCacheDirty.html) | Update hasMultipleDifferentValues cache on the next /Update()/ call.  
[Update](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject.Update.html) | Update serialized object's representation.  
[UpdateIfRequiredOrScript](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject.UpdateIfRequiredOrScript.html) | Update serialized object's representation, only if the object has been modified since the last call to Update or if it is a script.  
* * *
