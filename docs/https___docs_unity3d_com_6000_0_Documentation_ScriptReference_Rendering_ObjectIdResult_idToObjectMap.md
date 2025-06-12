* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ObjectIdResult-idToObjectMapping.html

#  [ObjectIdResult](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ObjectIdResult.html).idToObjectMapping
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
idToObjectMapping; 
### Description
An array of Objects that can be used to deterimine the object at each pixel in ObjectIdRequest._destination, first by decoding colors from ObjectIdRequest._destination to an index using [ObjectIdResult.DecodeIdFromColor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ObjectIdResult.DecodeIdFromColor.html), and then by looking up this index in this array. 
* * *
