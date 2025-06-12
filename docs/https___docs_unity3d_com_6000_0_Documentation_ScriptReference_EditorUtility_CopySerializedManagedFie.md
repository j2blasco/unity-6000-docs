* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.CopySerializedManagedFieldsOnly.html

#  [EditorUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.html).CopySerializedManagedFieldsOnly
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
## Declaration
public static void CopySerializedManagedFieldsOnly(object source, object dest); 
### Parameters
Parameter | Description  
---|---  
source | The object to copy data from.  
dest | The object to copy data to.  
### Description
Copies the serializable fields from one managed object to another.
This is similar to CopySerialized, but you can use it with any two managed objects, rather than two instances of the same Object subclass.  
  
`CopySerializedManagedFieldsOnly` copies all fields supported by the Unity serializer. If the destination object is not of the same class as the source object, then the function matches fields by name, or by using the FormerlySerializedAs attribute. The function does not modify any fields on the destination object which are not serializable, or which do not have corresponding fields in the source object.  
  
If the source object implements the [ISerializationCallbackReceiver](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ISerializationCallbackReceiver.html) interface, then its OnBeforeSerialize method is called before any data is read. Similarly, if the destination object implements the [ISerializationCallbackReceiver](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ISerializationCallbackReceiver.html), then its OnAfterDeserialize method is called after data has been copied into its fields.  
  
`CopySerializedManagedFieldsOnly` only copies fields defined in managed code. This means that if you attempt to copy engine objects such as [Transform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) or [Light](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light.html), `CopySerializedManagedFieldsOnly` does not copy any data, since all of their serializable fields are defined in native code.
* * *
