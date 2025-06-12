* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HashUtilities.QuantisedVectorHash.html

#  [HashUtilities](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HashUtilities.html).QuantisedVectorHash
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
public static void QuantisedVectorHash(ref [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) value, ref [Hash128](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Hash128.html) hash); 
### Parameters
Parameter | Description  
---|---  
hash | The Vector3 to hash.  
value | The computed hash.  
### Description
Compute a Hash128 of a Vector3.
The Vector3 is quantized before the hashing with a step of 0.0005.
* * *
