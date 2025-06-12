* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HashUtilities.QuantisedMatrixHash.html

#  [HashUtilities](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HashUtilities.html).QuantisedMatrixHash
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
public static void QuantisedMatrixHash(ref [Matrix4x4](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.html) value, ref [Hash128](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Hash128.html) hash); 
### Parameters
Parameter | Description  
---|---  
value | The Matrix4x4 to hash.  
hash | The computed hash.  
### Description
Compute a Hash128 of a Matrix4x4.
The Matrix4x4 is quantized before the hashing with a step of 0.0005.
* * *
