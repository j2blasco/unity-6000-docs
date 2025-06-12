* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.Hand.TryGetFingerBones.html

#  [Hand](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.Hand.html).TryGetFingerBones
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
public bool TryGetFingerBones([XR.HandFinger](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.HandFinger.html) finger, List<Bone> bonesOut); 
### Parameters
Parameter | Description  
---|---  
finger | HandFinger enum value for this finger.  
bonesOut | A list of bones that will be filled out for this finger.  
### Returns
**bool** true if hand can be queried for this finger; otherwise false. 
### Description
Gets a list of the finger bones for a finger on this hand.
* * *
