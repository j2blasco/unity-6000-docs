* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html

# SerializedProperty
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
SerializedProperty and [SerializedObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject.html) are classes for editing properties on objects in a completely generic way that automatically handles undo, multi-object editing and Prefab overrides.
SerializedProperty is primarily used to read or change the value of a property. It can also iterate through the properties of an object using [Next](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.Next.html). Additional resources: [SerializedObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject.html) class, [Editor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html) class.
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
public class MyObject : ScriptableObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.html)
{
    public int myInt = 42;
}  
  
public class SerializedPropertyTest : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        MyObject obj = ScriptableObject.CreateInstance[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.CreateInstance.html)<MyObject>();
        SerializedObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject.html) serializedObject = new UnityEditor.SerializedObject(obj);  
  
        SerializedProperty[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html) serializedPropertyMyInt = serializedObject.FindProperty("myInt");  
  
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("myInt " + serializedPropertyMyInt.intValue);
    }
}

```

### Properties
Property | Description  
---|---  
[animationCurveValue](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty-animationCurveValue.html) | Value of a animation curve property.  
[arrayElementType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty-arrayElementType.html) | Type name of the element in an array property. (Read Only)  
[arraySize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty-arraySize.html) | The number of elements in the array.  
[boolValue](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty-boolValue.html) | Value of a boolean property.  
[boundsIntValue](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty-boundsIntValue.html) | Value of bounds with integer values property.  
[boundsValue](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty-boundsValue.html) | Value of bounds property.  
[boxedValue](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty-boxedValue.html) | Value of the SerializedProperty, boxed as a System.Object.  
[colorValue](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty-colorValue.html) | Value of a color property.  
[contentHash](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty-contentHash.html) | Provides the hash value for the property. (Read Only)  
[depth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty-depth.html) | Nesting depth of the property. (Read Only)  
[displayName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty-displayName.html) | Nice display name of the property. (Read Only)  
[doubleValue](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty-doubleValue.html) | Value of a float property as a double.  
[editable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty-editable.html) | Is this property editable? (Read Only)  
[enumDisplayNames](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty-enumDisplayNames.html) | Display-friendly names of enumeration of an enum property.  
[enumNames](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty-enumNames.html) | Names of enumeration of an enum property.  
[enumValueFlag](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty-enumValueFlag.html) | Int32 representation of an enum property with Mixed Values.  
[enumValueIndex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty-enumValueIndex.html) | Enum index of an enum property.  
[exposedReferenceValue](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty-exposedReferenceValue.html) | A reference to another Object in the Scene. This reference is resolved in the context of the SerializedObject containing the SerializedProperty.  
[fixedBufferSize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty-fixedBufferSize.html) | The number of elements in the fixed buffer. (Read Only)  
[floatValue](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty-floatValue.html) | Value of a float property.  
[gradientValue](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty-gradientValue.html) | Value of a gradient property.  
[hasChildren](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty-hasChildren.html) | Does it have child properties? (Read Only)  
[hash128Value](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty-hash128Value.html) | The value of a Hash128 property.  
[hasMultipleDifferentValues](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty-hasMultipleDifferentValues.html) | Does this property represent multiple different values due to multi-object editing? (Read Only)  
[hasVisibleChildren](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty-hasVisibleChildren.html) | Does it have visible child properties? (Read Only)  
[intValue](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty-intValue.html) | Value of an integer property.  
[isArray](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty-isArray.html) | Is this property an array? (Read Only)  
[isDefaultOverride](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty-isDefaultOverride.html) | Allows you to check whether his property is a default override.Certain properties on Prefab instances are default overrides.See PrefabUtility.IsDefaultOverride for more information.  
[isExpanded](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty-isExpanded.html) | Is this property expanded in the inspector?  
[isFixedBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty-isFixedBuffer.html) | Is this property a fixed buffer? (Read Only)  
[isInstantiatedPrefab](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty-isInstantiatedPrefab.html) | Is property part of a Prefab instance? (Read Only)  
[longValue](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty-longValue.html) | Value of an integer property as a long.  
[managedReferenceFieldTypename](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty-managedReferenceFieldTypename.html) | String corresponding to the value of the managed reference field full type string.  
[managedReferenceFullTypename](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty-managedReferenceFullTypename.html) | String corresponding to the value of the managed reference object (dynamic) full type string.  
[managedReferenceId](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty-managedReferenceId.html) | Id associated with a managed reference.  
[managedReferenceValue](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty-managedReferenceValue.html) | The object assigned to a field with SerializeReference attribute.  
[minArraySize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty-minArraySize.html) | The smallest number of elements in the array across all target objects. (Read Only)  
[name](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty-name.html) | Name of the property. (Read Only)  
[numericType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty-numericType.html) | Return the precise type for Integer and Floating point properties. (Read Only)  
[objectReferenceValue](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty-objectReferenceValue.html) | Value of an object reference property.  
[prefabOverride](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty-prefabOverride.html) | Allows you to check whether a property's value is overriden (i.e. different to the Prefab it belongs to).  
[propertyPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty-propertyPath.html) | Full path of the property. (Read Only)  
[propertyType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty-propertyType.html) | Type of this property (Read Only).  
[quaternionValue](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty-quaternionValue.html) | Value of a quaternion property.  
[rectIntValue](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty-rectIntValue.html) | Value of a rectangle with integer values property.  
[rectValue](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty-rectValue.html) | Value of a rectangle property.  
[serializedObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty-serializedObject.html) |  SerializedObject this property belongs to (Read Only).  
[stringValue](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty-stringValue.html) | Value of a string property.  
[tooltip](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty-tooltip.html) | Tooltip of the property. (Read Only)  
[type](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty-type.html) | Type name of the property. (Read Only)  
[uintValue](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty-uintValue.html) | Value of an integer property as an unsigned int.  
[ulongValue](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty-ulongValue.html) | Value of an integer property as an unsigned long.  
[vector2IntValue](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty-vector2IntValue.html) | Value of a 2D integer vector property.  
[vector2Value](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty-vector2Value.html) | Value of a 2D vector property.  
[vector3IntValue](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty-vector3IntValue.html) | Value of a 3D integer vector property.  
[vector3Value](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty-vector3Value.html) | Value of a 3D vector property.  
[vector4Value](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty-vector4Value.html) | Value of a 4D vector property.  
### Public Methods
Method | Description  
---|---  
[ClearArray](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.ClearArray.html) | Remove all elements from the array.  
[Copy](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.Copy.html) | Returns a copy of the SerializedProperty iterator in its current state.  
[CountInProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.CountInProperty.html) | Count visible children of this property, including this property itself.  
[CountRemaining](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.CountRemaining.html) | Count remaining visible properties.  
[DeleteArrayElementAtIndex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.DeleteArrayElementAtIndex.html) | Delete the element at the specified index in the array.  
[DeleteCommand](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.DeleteCommand.html) | Deletes the array element referenced by the SerializedProperty.  
[DuplicateCommand](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.DuplicateCommand.html) | Duplicates the array element referenced by the SerializedProperty.  
[FindPropertyRelative](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.FindPropertyRelative.html) | Retrieves the SerializedProperty at a relative path to the current property.  
[GetArrayElementAtIndex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.GetArrayElementAtIndex.html) | Returns the element at the specified index in the array.  
[GetEndProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.GetEndProperty.html) | Retrieves the SerializedProperty that defines the end range of this property.  
[GetEnumerator](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.GetEnumerator.html) | Retrieves an iterator for enumerating over the visible child properties of the current property. If the property is an array it will enumerate over the array elements.  
[GetFixedBufferElementAtIndex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.GetFixedBufferElementAtIndex.html) | Returns the element at the specified index in the fixed buffer.  
[InsertArrayElementAtIndex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.InsertArrayElementAtIndex.html) | Insert an new element at the specified index in the array.  
[MoveArrayElement](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.MoveArrayElement.html) | Move an array element from srcIndex to dstIndex.  
[Next](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.Next.html) | Move to next property.  
[NextVisible](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.NextVisible.html) | Move to next visible property.  
[Reset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.Reset.html) | Move to first property of the object.  
### Static Methods
Method | Description  
---|---  
[DataEquals](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.DataEquals.html) | Compares the data for two SerializedProperties. This method ignores paths and SerializedObjects.  
[EqualContents](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.EqualContents.html) | See if contained serialized properties are equal.  
* * *
