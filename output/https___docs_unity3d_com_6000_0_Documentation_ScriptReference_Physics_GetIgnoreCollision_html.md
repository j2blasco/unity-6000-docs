* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.GetIgnoreCollision.html

#  [Physics](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.html).GetIgnoreCollision
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
public static bool GetIgnoreCollision([Collider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html) collider1, [Collider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html) collider2); 
### Parameters
Parameter | Description  
---|---  
collider1 | The first collider to compare to `collider2`.  
collider2 | The second collider to compare to `collider1`.  
### Returns
**bool** Whether the collision detection system will ignore all collisions/triggers between `collider1` and `collider2` or not. 
### Description
Checks whether the collision detection system will ignore all collisions/triggers between `collider1` and `collider2` or not.
* * *
