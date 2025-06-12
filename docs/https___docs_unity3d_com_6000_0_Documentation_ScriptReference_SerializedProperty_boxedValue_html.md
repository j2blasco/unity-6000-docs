* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty-boxedValue.html

#  [SerializedProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html).boxedValue
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
boxedValue; 
### Description
Value of the SerializedProperty, boxed as a System.Object.
This property represents the value of the SerializedProperty as a System.Object which wraps the underlying type.  
  
This property makes it easier to write code that doesn't need the precise type of a SerializedProperty to get or set its value. For example this property can access any numeric type, strings, built-in types like [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) and ManagedReference objects with the same syntax. This property can remove the need for switch-case statements or slow alternatives based on .NET Reflection to determine a SerializedProperty's type.  
  
Wrapping a value type as a heap-based System.Object requires a transformation called "boxing", which adds a performance overhead. In cases where performance is important and you know the type ahead of time, use the appropriate type-specific accessors like [intValue](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty-intValue.html), [stringValue](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty-stringValue.html), or [managedReferenceValue](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty-managedReferenceValue.html) instead of this property. This removes the performance overhead that this property requires for boxing.  
  
When your application sets this property, Unity attempts to unbox and convert the provided System.Object into the property type of the SerializedProperty. If this fails, Unity throws an InvalidCastException error.  
  
boxedValue has some limitations for properties of type [SerializedPropertyType.Generic](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedPropertyType.Generic.html): 
  * Structs and objects serialized by-value can be accessed, unless they contain fixed buffers.
  * The property cannot be an array or list. But accessing a property that is an element of an array or list is supported.
  * Unity built-in Struct types that are categorized in the Generic type cannot be accessed. But built-in types like [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) that have a their own entry in the [SerializedPropertyType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedPropertyType.html) enum do work.


Additional resources: [propertyType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty-propertyType.html).
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;
using System.Collections.Generic;  
  
// To try this example save it as a script called BoxedValueStructExample.cs,
// then create an asset file from the Project Window context menu, then inspect it  
  
[System.Serializable]
public struct Element[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Element.html)
{
    public int m_IntData;
    public Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) m_ColorData;
    public Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) m_Rect;  
  
    public void Change()
    {
        ++m_IntData;
        m_ColorData = new Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html)(Random.Range[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Random.Range.html)(0f, 1f), Random.Range[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Random.Range.html)(0f, 1f), Random.Range[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Random.Range.html)(0f, 1f), 1);
        m_Rect = new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(Random.Range[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Random.Range.html)(0, 100), Random.Range[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Random.Range.html)(0, 100),
            Random.Range[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Random.Range.html)(0, 100), Random.Range[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Random.Range.html)(0, 100));
    }
};  
  
[CreateAssetMenu]
public class BoxedValueStructExample : ScriptableObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.html)
{
    public Element[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Element.html) m_NewItem = new Element[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Element.html)();
    public List<Element[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Element.html)> m_ItemList = new List<Element[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Element.html)>();
}  
  
[CustomEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CustomEditor.html)(typeof(BoxedValueStructExample)), CanEditMultipleObjects[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CanEditMultipleObjects.html)]
public class BoxedValueStructExampleEditor : Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html)
{
    SerializedProperty[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html) m_NewItemProp;
    SerializedProperty[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html) m_ListProp;  
  
    public void OnEnable()
    {
        m_NewItemProp = serializedObject.FindProperty("m_NewItem");
        m_ListProp = serializedObject.FindProperty("m_ItemList");
    }  
  
    public override void OnInspectorGUI()
    {
        EditorGUILayout.PropertyField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.PropertyField.html)(m_NewItemProp);  
  
        GUILayout.Space[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Space.html)(30);  
  
        if (GUILayout.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Button.html)("Add New Item[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.Item.html) to List"))
        {
            // Read full Element[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Element.html) struct
            Element[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Element.html) newItem = (Element[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Element.html))m_NewItemProp.boxedValue;  
  
            // Append a new item to list and set it to the same values as m_NewItem
            m_ListProp.arraySize++;
            m_ListProp.GetArrayElementAtIndex(m_ListProp.arraySize - 1).boxedValue = newItem;  
  
            // Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html) NewItem to some new values
            newItem.Change();
            m_NewItemProp.boxedValue = newItem;  
  
            // Because boxedValue is used, the code above does not need to deal with fields inside the struct,
            // and it would not need to change as fields are added and removed to Element[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Element.html)
        }  
  
        GUILayout.Space[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Space.html)(30);
        EditorGUILayout.PropertyField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.PropertyField.html)(m_ListProp);  
  
        serializedObject.ApplyModifiedProperties();
    }
}

```

```
using System.Text;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;  
  
public class BoxedValueExample
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Example/Log Property Values")]
    static void MenuCallback()
    {
        var log = new StringBuilder();
        var obj = Selection.activeGameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection-activeGameObject.html);
        {
            log.AppendLine($"Contents of {obj.name}");
            LogProperties(obj, log);
        }  
  
        foreach (var comp in obj.GetComponents<Component[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.html)>())
        {
            log.AppendLine();
            log.AppendLine($"Component[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.html) {comp.GetType().ToString()}");
            LogProperties(comp, log);
        }  
  
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(log.ToString());
    }  
  
    static void LogProperties(UnityEngine.Object obj, StringBuilder log)
    {
        using (var so = new SerializedObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject.html)(obj))
        {
            var iterator = so.GetIterator();
            iterator.Next(true); // Move past root property  
  
            // Printing top level propertise only
            do
            {
                log.Append(iterator.name);
                log.Append(" type: ");
                log.Append(iterator.propertyType);
                LogValue(iterator, log);
                log.AppendLine();
            }
            while (iterator.Next(false));
        }
    }  
  
    static void LogValue(SerializedProperty[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html) serializedProperty, StringBuilder log)
    {
        // Don't attempt to print these types as strings
        if (serializedProperty.propertyType == SerializedPropertyType.Generic[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedPropertyType.Generic.html) ||
            serializedProperty.propertyType == SerializedPropertyType.ObjectReference[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedPropertyType.ObjectReference.html) ||
            serializedProperty.propertyType == SerializedPropertyType.ManagedReference[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedPropertyType.ManagedReference.html))
        {
            return;
        }  
  
        log.Append($" value: {serializedProperty.boxedValue}");
    }  
  
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Example/Log Property Values", true)]
    static bool MenuValidation()
    {
        return Selection.activeGameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection-activeGameObject.html) != null;
    }
}

```

This is a recursive version of the example, with more information and formatting, but still relying on boxedValue.
```
using System.Collections.Generic;
using System.Text;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;  
  
public class RecursivePropertyLogExample
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Example/Log Property Values (Recursive)")]
    static void MenuCallback()
    {
        var obj = Selection.activeGameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection-activeGameObject.html);
        {
            var log = new StringBuilder();
            log.AppendLine($"Contents of {obj.name}");
            LogProperties(obj, log);  
  
            // Log separately to avoid reaching the individual message size limit
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(log.ToString());
        }  
  
        foreach (var comp in obj.GetComponents<Component[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.html)>())
        {
            var log = new StringBuilder();
            log.AppendLine($"Component[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.html) {comp.GetType().ToString()} of {obj.name}");
            LogProperties(comp, log);
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(log.ToString());
        }
    }  
  
    static void LogProperties(UnityEngine.Object obj, StringBuilder log)
    {
        using (var so = new SerializedObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject.html)(obj))
        {
            var iterator = so.GetIterator();
            iterator.Next(true); // Move past root property  
  
            // Prevent endless loops if SerializeReference[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializeReference.html) instances form cyclical graphs
            var visitedManagedReferences = new HashSet<long>();  
  
            bool visitChild;
            do
            {
                visitChild = false;  
  
                if (iterator.propertyType == SerializedPropertyType.Generic[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedPropertyType.Generic.html))
                {
                    visitChild = true;
                }
                else if (iterator.propertyType == SerializedPropertyType.ManagedReference[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedPropertyType.ManagedReference.html))
                {
                    long refId = iterator.managedReferenceId;
                    if (visitedManagedReferences.Add(refId))
                        visitChild = true; // First time seeing node, so visit it
                }  
  
                for (int i = 0; i < iterator.depth; i++)
                    log.Append("  ");  
  
                if (iterator.name == "data")
                {
                    // If this is an array element then it is more informative to use the name exposed by
                    // propertyPath, e.g. "data[7]" instead of "data".
                    var stringPos = iterator.propertyPath.LastIndexOf('.');
                    if (stringPos > 0)
                        log.Append(iterator.propertyPath.Substring(stringPos + 1));
                    else
                        log.Append(iterator.name);
                }
                else
                    log.Append(iterator.name);  
  
                LogType[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LogType.html)(iterator, log);
                LogValue(iterator, log);
                log.AppendLine();  
  
                // Skip past the "Array" child inside each property of type array
                if (iterator.isArray)
                    iterator.Next(true);
            }
            while (iterator.Next(visitChild));
        }
    }  
  
    static void LogType[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LogType.html)(SerializedProperty[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html) serializedProperty, StringBuilder log)
    {
        log.Append(" type: ");
        if (serializedProperty.propertyType == SerializedPropertyType.Integer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedPropertyType.Integer.html) ||
            serializedProperty.propertyType == SerializedPropertyType.Float[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedPropertyType.Float.html))
            log.Append(serializedProperty.numericType);
        else if (serializedProperty.propertyType == SerializedPropertyType.Generic[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedPropertyType.Generic.html) && serializedProperty.isArray)
            log.Append("Array");
        else
            log.Append(serializedProperty.propertyType);
    }  
  
    static void LogValue(SerializedProperty[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html) serializedProperty, StringBuilder log)
    {
        // use boxedValue to get and print the value as a string
        // There are a few special cases to improve the quality of the output  
  
        if (serializedProperty.propertyType == SerializedPropertyType.Generic[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedPropertyType.Generic.html) ||
            serializedProperty.propertyType == SerializedPropertyType.AnimationCurve[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedPropertyType.AnimationCurve.html) ||
            serializedProperty.propertyType == SerializedPropertyType.Gradient[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedPropertyType.Gradient.html) ||
            serializedProperty.propertyType == SerializedPropertyType.LayerMask[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedPropertyType.LayerMask.html))
        {
            return;
        }  
  
        if (serializedProperty.propertyType == SerializedPropertyType.ObjectReference[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedPropertyType.ObjectReference.html))
        {
            if (ReferenceEquals(serializedProperty.objectReferenceValue, null))
                log.Append($" value: null");
            else
                log.Append($" instanceID: {serializedProperty.objectReferenceValue.GetInstanceID()}");
        }
        else if (serializedProperty.propertyType == SerializedPropertyType.ManagedReference[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedPropertyType.ManagedReference.html))
        {
            if (ReferenceEquals(serializedProperty.managedReferenceValue, null))
                log.Append($" value: null");
            else
                log.Append($" refId: {serializedProperty.managedReferenceId} ({serializedProperty.managedReferenceFullTypename})");
        }
        else
        {
            log.Append($" value: {serializedProperty.boxedValue.ToString()}");
        }
    }  
  
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Example/Log Property Values (Recursive)", true)]
    static bool ValidateMenuItem()
    {
        return Selection.activeGameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection-activeGameObject.html) != null;
    }
}

```

* * *
