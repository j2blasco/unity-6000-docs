* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.Equals.html

#  [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html).Equals
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
public bool Equals(object other); 
### Description
Returns true if the given vector is exactly equal to this vector.
Due to floating point inaccuracies, this might return false for vectors which are essentially (but not exactly) equal. Use the [== operator](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-operator_eq.html) to test two vectors for approximate equality.
* * *
