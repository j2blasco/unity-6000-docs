* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GlobalObjectId.GetGlobalObjectIdSlow.html

#  [GlobalObjectId](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GlobalObjectId.html).GetGlobalObjectIdSlow
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
public static [GlobalObjectId](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GlobalObjectId.html) GetGlobalObjectIdSlow([Object](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.html) targetObject); 
### Parameters
Parameter | Description  
---|---  
targetObject | The object to obtain the unique identifier for.  
### Returns
**GlobalObjectId** The `GlobalObjectId` for the object. If the conversion is unsuccessful, then the `GlobalObjectId` is set to the default null ID. The null ID has the string representation `GlobalObjectId_V1-0-00000000000000000000000000000000-0-0`
### Description
Obtains the unique object identifiers based on an object reference.
This method is slow. Use it sparingly. To get unique identifiers for multiple objects, it's recommended to use [GlobalObjectId.GetGlobalObjectIdsSlow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GlobalObjectId.GetGlobalObjectIdsSlow.html) instead of making multiple calls to this method. If you use this method in a large project within other performance-sensitive contexts such as [ISerializationCallbackReceiver.OnBeforeSerialize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ISerializationCallbackReceiver.OnBeforeSerialize.html) or [ISerializationCallbackReceiver.OnAfterDeserialize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ISerializationCallbackReceiver.OnAfterDeserialize.html), it's strongly recommended to profile the performance impact.  
  
Additional resources: [GlobalObjectId.GetGlobalObjectIdsSlow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GlobalObjectId.GetGlobalObjectIdsSlow.html), [Object.GetInstanceID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.GetInstanceID.html)
* * *
## Declaration
public static [GlobalObjectId](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GlobalObjectId.html) GetGlobalObjectIdSlow(int instanceId); 
### Parameters
Parameter | Description  
---|---  
instanceId | The instance ID of the object to obtain the unique identifier for.  
### Returns
**GlobalObjectId** The `GlobalObjectId` for the object. If the conversion is unsuccessful, then the `GlobalObjectId` is set to the default null ID. The null ID has the string representation `GlobalObjectId_V1-0-00000000000000000000000000000000-0-0`
### Description
Obtains the unique object identifiers based on an instance ID.
This method is slow. Use it sparingly. To get unique identifiers for multiple objects, it's recommended to use [GlobalObjectId.GetGlobalObjectIdsSlow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GlobalObjectId.GetGlobalObjectIdsSlow.html) instead of making multiple calls to this method. If you use this method in a large project within other performance-sensitive contexts such as [ISerializationCallbackReceiver.OnBeforeSerialize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ISerializationCallbackReceiver.OnBeforeSerialize.html) or [ISerializationCallbackReceiver.OnAfterDeserialize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ISerializationCallbackReceiver.OnAfterDeserialize.html), it's strongly recommended to profile the performance impact.  
  
Additional resources: [GlobalObjectId.GetGlobalObjectIdsSlow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GlobalObjectId.GetGlobalObjectIdsSlow.html), [Object.GetInstanceID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.GetInstanceID.html)
* * *
