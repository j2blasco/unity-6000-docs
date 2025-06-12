* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GlobalObjectId.GlobalObjectIdentifierToInstanceIDSlow.html

#  [GlobalObjectId](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GlobalObjectId.html).GlobalObjectIdentifierToInstanceIDSlow
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
public static int GlobalObjectIdentifierToInstanceIDSlow([GlobalObjectId](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GlobalObjectId.html) id); 
### Parameters
Parameter | Description  
---|---  
id | The `GlobalObjectId` to lookup.  
### Returns
**int** Returns the `InstanceID` of the object. If the `GlobalObjectId` can't be found, or if the scene isn't loaded, returns `0`. 
### Description
Obtains the instance ID of the object from its unique object identifier.
This method is slow. Use it sparingly. If you use this method in a large project within other performance-sensitive contexts such as [ISerializationCallbackReceiver.OnBeforeSerialize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ISerializationCallbackReceiver.OnBeforeSerialize.html) or [ISerializationCallbackReceiver.OnAfterDeserialize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ISerializationCallbackReceiver.OnAfterDeserialize.html), it's strongly recommended to profile the performance impact.  
  
Additional resources: [GlobalObjectId.GlobalObjectIdentifiersToInstanceIDsSlow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GlobalObjectId.GlobalObjectIdentifiersToInstanceIDsSlow.html)
* * *
