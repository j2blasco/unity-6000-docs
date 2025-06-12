* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GlobalObjectId.TryParse.html

#  [GlobalObjectId](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GlobalObjectId.html).TryParse
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
public static bool TryParse(string stringValue, out [GlobalObjectId](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GlobalObjectId.html) id); 
### Parameters
Parameter | Description  
---|---  
stringValue | The string representation of a `GlobalObjectId`.  
  
The following is an example of the string representation: `GlobalObjectId_V1-2-74c253e3f16be4776bb2d88e01f77c8a-902906726-0`. For more information on the composition, refer to [GlobalObjectId](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GlobalObjectId.html).  
id | The `GlobalObjectId` struct to populate with the parsed values.  
### Returns
**bool** Returns `true` if the string representation is successfully parsed. Otherwise, returns `false`
### Description
Tries to parse the string representation of a GlobalObjectId into a GlobalObjectId struct.
This method takes the string representation of a unique object identifier and converts it to a `GlobalObjectId` struct.  
  
Calling this method sets the state of the provided `GlobalObjectId`, but doesn't attempt to resolve it to an object reference. A return value of `true` doesn't guarantee that a call to [GlobalObjectId.GlobalObjectIdentifierToObjectSlow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GlobalObjectId.GlobalObjectIdentifierToObjectSlow.html) or similar method will succeed.  
  
Additional resources: [GlobalObjectId.ToString](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GlobalObjectId.ToString.html)
* * *
