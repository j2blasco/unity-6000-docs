* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GlobalObjectId.GetGlobalObjectIdsSlow.html

#  [GlobalObjectId](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GlobalObjectId.html).GetGlobalObjectIdsSlow
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
public static void GetGlobalObjectIdsSlow(Object[] objects, out GlobalObjectId[] outputIdentifiers); 
### Parameters
Parameter | Description  
---|---  
objects | Array of objects to obtain unique identifiers for.  
outputIdentifiers | Array of `GlobalObjectId` objects to write to.  
### Description
Creates an array of unique object identifiers based on an array of objects.
For each item in `objects`, this method obtains its unique `GlobalObjectId` and writes it to the corresponding element in `outputIdentifiers`. Both arrays must be the same size.  
  
This method is slow. Use it sparingly and avoid making multiple calls.  
  
Additional resources: [GlobalObjectId.GetGlobalObjectIdSlow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GlobalObjectId.GetGlobalObjectIdSlow.html), [Object.GetInstanceID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.GetInstanceID.html)
* * *
## Declaration
public static void GetGlobalObjectIdsSlow(int[] instanceIds, out GlobalObjectId[] outputIdentifiers); 
### Parameters
Parameter | Description  
---|---  
outputIdentifiers | Array of `GlobalObjectId` objects to write to.  
instanceIds | Array of instance IDs of the objects to obtain unique identifiers for.  
### Description
Creates an array of unique object identifiers based on an array of instance IDs.
For each object identified by an item in `instanceIds`, this method obtains the unique `GlobalObjectId` and writes it to the corresponding element in `outputIdentifiers`. Both arrays must be the same size.  
  
This method is slow. Use it sparingly and avoid making multiple calls.  
  
Additional resources: [GlobalObjectId.GetGlobalObjectIdSlow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GlobalObjectId.GetGlobalObjectIdSlow.html), [Object.GetInstanceID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.GetInstanceID.html)
* * *
