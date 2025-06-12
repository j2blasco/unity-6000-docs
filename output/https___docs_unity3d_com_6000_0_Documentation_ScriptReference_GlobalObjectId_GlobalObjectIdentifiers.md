* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GlobalObjectId.GlobalObjectIdentifiersToObjectsSlow.html

#  [GlobalObjectId](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GlobalObjectId.html).GlobalObjectIdentifiersToObjectsSlow
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
public static void GlobalObjectIdentifiersToObjectsSlow(GlobalObjectId[] identifiers, out Object[] outputObjects); 
### Parameters
Parameter | Description  
---|---  
identifiers | Array of GlobalObjectIds to convert to object references.  
outputObjects | Array of `Objects` to write object references to.  
### Description
Creates an array of object references based on an array of unique object identifiers.
For each item in `identifiers`, this method obtains a reference to the underlying object and writes it to the corresponding element in `outputObjects`. Both arrays must be the same size.  
  
Any `GlobalObjectIds` in the `identifiers` array that can't be resolved are given a value of `null` in the output `outputObjects` array. This method is slow. Use it sparingly. If you use this method in a large project within other performance-sensitive contexts such as [ISerializationCallbackReceiver.OnBeforeSerialize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ISerializationCallbackReceiver.OnBeforeSerialize.html) or [ISerializationCallbackReceiver.OnAfterDeserialize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ISerializationCallbackReceiver.OnAfterDeserialize.html), it's strongly recommended to profile the performance impact.  
  
Additional resources: [GlobalObjectId.GlobalObjectIdentifierToObjectSlow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GlobalObjectId.GlobalObjectIdentifierToObjectSlow.html)
* * *
